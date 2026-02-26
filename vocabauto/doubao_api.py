#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import time
import logging
import re
import os

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DoubaoAPI:
    """豆包API客户端，用于获取AI辅助答案"""
    
    # 类级别的常量配置
    DEFAULT_BASE_URL = "https://www.doubao.com/chat/create"
    # 国内镜像源列表，用于提高访问速度和稳定性
    MIRROR_SOURCES = [
        "https://www.doubao.com/chat/create",
        "https://doubao-api.baidu.com/chat/create",  # 示例镜像源，实际需替换为真实可用的
    ]
    
    # 默认请求参数
    DEFAULT_TIMEOUT = 30
    DEFAULT_MAX_RETRIES = 3
    DEFAULT_RETRY_DELAY = 2
    
    def __init__(self, base_url=None, timeout=None, max_retries=None, retry_delay=None):
        """初始化豆包API客户端
        
        Args:
            base_url (str): 豆包API的基础URL
            timeout (int): 请求超时时间，单位秒
            max_retries (int): 最大重试次数
            retry_delay (int): 重试间隔，单位秒
        """
        self.base_url = base_url or os.environ.get('DOUBAO_API_URL', self.DEFAULT_BASE_URL)
        self.timeout = timeout or int(os.environ.get('DOUBAO_TIMEOUT', self.DEFAULT_TIMEOUT))
        self.max_retries = max_retries or int(os.environ.get('DOUBAO_MAX_RETRIES', self.DEFAULT_MAX_RETRIES))
        self.retry_delay = retry_delay or int(os.environ.get('DOUBAO_RETRY_DELAY', self.DEFAULT_RETRY_DELAY))
        
        # 创建会话对象
        self.session = requests.Session()
        
        # 设置默认请求头
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Content-Type": "application/json",
            "Referer": "https://www.doubao.com/"
        }
        
        # 设置会话的默认超时
        self.session.timeout = self.timeout
        
        logger.info(f"初始化DoubaoAPI客户端，基础URL: {self.base_url}")
    
    def get_answer(self, question, options):
        """向豆包API提问并获取答案
        
        Args:
            question (str): 问题内容
            options (list): 选项列表
            
        Returns:
            str: 匹配的选项内容
        """
        if not question or not options:
            logger.warning("问题或选项为空，无法获取答案")
            return options[0] if options else ""
        
        try:
            # 构建问题提示
            prompt = f"请回答下面的英语选择题，只需要返回正确的选项内容，不要解释。\n问题: {question}\n选项: {', '.join(options)}"
            
            logger.info(f"向豆包提问: {prompt[:100]}...")
            
            # 发送请求到豆包API
            response = self._send_request(prompt)
            
            if response:
                # 解析答案
                answer = self._parse_response(response)
                logger.info(f"豆包原始回答: {answer[:50]}...")
                
                # 匹配选项
                matched_option = self._match_option(answer, options)
                logger.info(f"匹配到选项: {matched_option}")
                return matched_option
            
        except Exception as e:
            logger.error(f"豆包API调用错误: {e}")
        
        logger.warning(f"无法获取答案，默认返回第一个选项: {options[0]}")
        return options[0]  # 默认返回第一个选项
    
    def _send_request(self, prompt):
        """发送请求到豆包API，带重试机制和镜像源切换
        
        Args:
            prompt (str): 请求提示内容
            
        Returns:
            dict: API响应结果
        """
        retry_count = 0
        delay = self.retry_delay
        
        # 尝试所有可用的镜像源
        for source_url in [self.base_url] + self.MIRROR_SOURCES:
            if retry_count >= self.max_retries:
                break
                
            try:
                logger.info(f"发送请求到豆包API (源: {source_url}, 重试 {retry_count+1}/{self.max_retries})...")
                
                # 豆包网页版API的实际请求格式（需要根据实际情况调整）
                payload = {
                    "prompt": prompt,
                    "session_id": "",  # 可能需要从网页获取
                    "model": "doubao-pro",
                    "temperature": 0.3,
                    "max_tokens": 100
                }
                
                # 发送POST请求
                response = self.session.post(
                    source_url,
                    headers=self.headers,
                    data=json.dumps(payload),
                    timeout=self.timeout
                )
                
                response.raise_for_status()
                logger.info(f"请求成功，使用源: {source_url}")
                return response.json()
                
            except requests.exceptions.RequestException as e:
                logger.error(f"网络请求错误 (源: {source_url}, 重试 {retry_count+1}/{self.max_retries}): {e}")
                
                retry_count += 1
                
                if retry_count < self.max_retries:
                    logger.info(f"等待 {delay} 秒后重试...")
                    time.sleep(delay)
                    delay *= 2  # 指数退避
                else:
                    logger.error("已达到最大重试次数")
                    break
            except Exception as e:
                logger.error(f"请求处理错误 (源: {source_url}): {e}")
                retry_count += 1
                if retry_count >= self.max_retries:
                    break
        
        logger.error("所有镜像源均请求失败")
        return None
    
    def _parse_response(self, response):
        """解析豆包API的响应
        
        Args:
            response (dict): API响应结果
            
        Returns:
            str: 解析出的答案文本
        """
        if not isinstance(response, dict):
            logger.error("响应不是字典类型")
            return ""
            
        try:
            # 根据豆包API的实际响应格式进行解析
            if "reply" in response:
                return response["reply"].strip()
            elif "content" in response:
                return response["content"].strip()
            elif "data" in response and "answer" in response["data"]:
                return response["data"]["answer"].strip()
            elif "result" in response:
                return response["result"].strip()
            else:
                # 如果无法解析，尝试返回原始文本
                logger.warning(f"无法解析响应结构，返回原始文本: {json.dumps(response)[:100]}...")
                return json.dumps(response)
        except Exception as e:
            logger.error(f"解析响应错误: {e}")
            return ""
    
    def _match_option(self, answer, options):
        """智能匹配豆包回答与选项
        
        Args:
            answer (str): 豆包返回的原始答案
            options (list): 选项列表
            
        Returns:
            str: 匹配的选项内容
        """
        if not answer or not options:
            logger.warning("答案或选项为空，无法匹配")
            return options[0] if options else ""
            
        answer_lower = answer.lower()
        logger.debug(f"智能匹配: 答案='{answer}', 选项={options}")
        
        # 预处理选项
        processed_options = []
        for i, option in enumerate(options):
            # 移除选项标识 (a., b., c., d.)
            processed_opt = option.lower()
            for prefix in ['a.', 'b.', 'c.', 'd.', '1.', '2.', '3.', '4.']:
                if processed_opt.startswith(prefix):
                    processed_opt = processed_opt[len(prefix):].strip()
                    break
            
            # 去除标点符号
            import string
            processed_opt = processed_opt.translate(str.maketrans('', '', string.punctuation))
            
            processed_options.append((option, processed_opt, i))
        
        # 1. 精确匹配
        for original_opt, processed_opt, i in processed_options:
            if processed_opt in answer_lower:
                logger.debug(f"精确匹配到选项: {original_opt}")
                return original_opt
        
        # 2. 检查答案中是否包含选项的字母标识 (如 "答案是 A")
        for original_opt, processed_opt, i in processed_options:
            option_letter = chr(ord('a') + i)  # 假设选项按 a, b, c, d 顺序
            if f"{option_letter}" in answer_lower or f"选项{option_letter}" in answer_lower:
                logger.debug(f"通过字母标识匹配到选项: {original_opt}")
                return original_opt
        
        # 3. 关键词匹配，计算匹配分数
        best_match = None
        highest_score = 0
        
        for original_opt, processed_opt, i in processed_options:
            option_words = set(processed_opt.split())
            answer_words = set(answer_lower.split())
            
            # 计算匹配的单词数量
            matching_words = option_words.intersection(answer_words)
            score = len(matching_words) / len(option_words) if option_words else 0
            
            logger.debug(f"选项 '{original_opt}' 的匹配分数: {score}")
            
            if score > highest_score:
                highest_score = score
                best_match = original_opt
        
        if best_match and highest_score > 0:
            logger.debug(f"通过关键词匹配到最佳选项: {best_match}")
            return best_match
        
        # 4. 检查常见的回答模式
        common_patterns = [
            (r'正确答案是?\s*(\w+)', lambda m: m.group(1)),
            (r'答案应该是?\s*(\w+)', lambda m: m.group(1)),
            (r'选择\s*(\w+)', lambda m: m.group(1)),
            (r'选\s*(\w+)', lambda m: m.group(1)),
        ]
        
        for pattern, extractor in common_patterns:
            match = re.search(pattern, answer_lower)
            if match:
                extracted = extractor(match).lower()
                # 匹配提取的内容与选项
                for original_opt, processed_opt, i in processed_options:
                    if extracted in processed_opt:
                        logger.debug(f"通过常见模式匹配到选项: {original_opt}")
                        return original_opt
        
        # 5. 作为最后的手段，返回第一个选项
        logger.warning(f"无法匹配到选项，默认返回第一个: {options[0]}")
        return options[0]
    
    def get_direct_answer(self, question):
        """直接获取豆包的回答（不匹配选项）
        
        Args:
            question (str): 问题内容
            
        Returns:
            str: 豆包返回的直接答案
        """
        if not question:
            logger.warning("问题为空，无法获取直接答案")
            return ""
            
        try:
            logger.info(f"直接获取豆包回答: {question[:50]}...")
            response = self._send_request(question)
            if response:
                answer = self._parse_response(response)
                logger.info(f"获取直接答案成功: {answer[:50]}...")
                return answer
        except Exception as e:
            logger.error(f"直接获取答案错误: {e}")
        return ""
