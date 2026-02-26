#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import pytesseract
import os
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ImageRecognizer:
    """图像识别器，用于识别图像中的文字内容"""
    
    # 类级别的常量配置
    DEFAULT_TESSERACT_PATH = r'C:\Program Files\Tesseract-OCR\tesseract.exe' if os.name == 'nt' else '/usr/bin/tesseract'
    DEFAULT_TESSERACT_CONFIG = '--psm 6 --oem 3'
    DEFAULT_LANGUAGE = 'eng+chi_sim'
    
    def __init__(self, tesseract_path=None, tesseract_config=None, language=None):
        """初始化图像识别器
        
        Args:
            tesseract_path (str): Tesseract OCR的安装路径
            tesseract_config (str): Tesseract的配置参数
            language (str): 识别语言，如'eng+chi_sim'
        """
        # 从参数或环境变量获取配置
        self.tesseract_path = tesseract_path or os.environ.get('TESSERACT_PATH', self.DEFAULT_TESSERACT_PATH)
        self.tesseract_config = tesseract_config or os.environ.get('TESSERACT_CONFIG', self.DEFAULT_TESSERACT_CONFIG)
        self.language = language or os.environ.get('OCR_LANGUAGE', self.DEFAULT_LANGUAGE)
        
        # 配置Tesseract路径
        pytesseract.pytesseract.tesseract_cmd = self.tesseract_path
        
        # 常见的选项词汇列表
        self.common_options = ['shrinks', 'swells', 'tightens', 'loss', 'loose', 'lose']
        
        logger.info(f"初始化ImageRecognizer，Tesseract路径: {self.tesseract_path}")
    
    def recognize_content(self, img):
        """识别图像中的文字内容
        
        Args:
            img (numpy.ndarray): 输入图像，BGR格式
            
        Returns:
            str: 识别出的文字内容
        """
        if img is None:
            logger.error("输入图像为空")
            return ""
            
        try:
            # 预处理图像
            processed_img = self._preprocess_image(img)
            
            # 使用Tesseract识别文字
            text = pytesseract.image_to_string(processed_img, config=self.tesseract_config, lang=self.language)
            recognized_text = text.strip()
            logger.debug(f"识别到文字: {recognized_text[:50]}...")
            return recognized_text
        except pytesseract.TesseractError as e:
            logger.error(f"Tesseract识别错误: {e}")
        except cv2.error as e:
            logger.error(f"OpenCV处理错误: {e}")
        except Exception as e:
            logger.error(f"图像识别错误: {e}")
        
        return ""
    
    def extract_question_options(self, content):
        """从识别的内容中提取问题和选项
        
        Args:
            content (str): 识别出的文字内容
            
        Returns:
            tuple: (question, options)，其中question是问题字符串，options是选项列表
        """
        if not content:
            logger.warning("输入内容为空，无法提取问题和选项")
            return "", []
            
        lines = content.split('\n')
        question = ""
        options = []
        
        logger.debug(f"开始提取问题和选项，共 {len(lines)} 行内容")
        
        # 提取问题部分
        for i, line in enumerate(lines):
            line = line.strip()
            if line and ('______' in line or '...' in line or any(keyword in line for keyword in ['?', 'when', 'what', 'which', 'who', 'why', 'how'])):
                question = line
                # 检查下一行是否也是问题的一部分
                if i + 1 < len(lines) and not any(opt in lines[i+1].lower() for opt in self.common_options):
                    question += ' ' + lines[i+1].strip()
                logger.debug(f"提取到问题: {question}")
                break
        
        # 提取选项部分
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            # 处理带选项标识的情况 (a., b., c., d.)
            if line.lower().startswith(('a.', 'b.', 'c.', 'd.', '1.', '2.', '3.', '4.')):
                option_text = line.split('.', 1)[1].strip() if '.' in line else line
                options.append(option_text)
            # 处理常见选项词汇
            elif line.lower() in self.common_options:
                options.append(line)
            # 处理可能的选项格式（如只有一个单词）
            elif len(line.split()) == 1 and line.isalpha() and line.lower() not in ['the', 'a', 'an', 'and', 'or', 'but', 'is', 'are', 'was', 'were']:
                options.append(line)
        
        # 去重并保持顺序
        seen = set()
        unique_options = []
        for opt in options:
            if opt.lower() not in seen:
                seen.add(opt.lower())
                unique_options.append(opt)
        
        logger.info(f"提取完成: 问题='{question}', 选项={unique_options}")
        return question, unique_options
    
    def _preprocess_image(self, img):
        """预处理图像以提高识别准确率
        
        Args:
            img (numpy.ndarray): 输入图像，BGR格式
            
        Returns:
            numpy.ndarray: 预处理后的图像，二值化格式
        """
        try:
            # 转换为灰度图
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            logger.debug("转换为灰度图")
            
            # 应用对比度增强
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
            gray = clahe.apply(gray)
            logger.debug("应用对比度增强")
            
            # 根据图像亮度选择合适的阈值处理
            mean_brightness = np.mean(gray)
            logger.debug(f"图像平均亮度: {mean_brightness}")
            
            if mean_brightness > 150:
                # 明亮背景使用普通阈值
                _, thresh = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY_INV)
                logger.debug("使用普通阈值处理")
            else:
                # 暗背景使用自适应阈值
                thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                           cv2.THRESH_BINARY_INV, 15, 5)
                logger.debug("使用自适应阈值处理")
            
            # 去除噪声
            kernel = np.ones((1, 1), np.uint8)
            thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
            logger.debug("去除噪声")
            
            # 强化文本边缘
            kernel_dilate = np.ones((2, 2), np.uint8)
            thresh = cv2.dilate(thresh, kernel_dilate, iterations=1)
            logger.debug("强化文本边缘")
            
            return thresh
        except Exception as e:
            logger.error(f"图像预处理错误: {e}")
            return img
    
    def detect_rectangle(self, img):
        """检测图像中的矩形区域
        
        Args:
            img (numpy.ndarray): 输入图像，BGR格式
            
        Returns:
            list: 矩形区域列表，每个元素为(x, y, w, h)元组
        """
        if img is None:
            logger.error("输入图像为空")
            return []
            
        try:
            # 预处理图像
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (5, 5), 0)
            edges = cv2.Canny(blur, 50, 150)
            logger.debug("图像边缘检测完成")
            
            # 查找轮廓
            contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            logger.debug(f"找到 {len(contours)} 个轮廓")
            
            # 筛选矩形轮廓
            rectangles = []
            for contour in contours:
                approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
                if len(approx) == 4:
                    x, y, w, h = cv2.boundingRect(approx)
                    aspect_ratio = w / float(h)
                    # 筛选合适大小和比例的矩形
                    if 0.5 < aspect_ratio < 2 and w > 100 and h > 100:
                        rectangles.append((x, y, w, h))
            
            logger.info(f"检测到 {len(rectangles)} 个矩形区域")
            return rectangles
        except Exception as e:
            logger.error(f"矩形检测错误: {e}")
            return []
    
    def recognize_rectangle_content(self, img, rect):
        """识别矩形区域内的内容
        
        Args:
            img (numpy.ndarray): 输入图像，BGR格式
            rect (tuple): 矩形区域，格式为(x, y, w, h)
            
        Returns:
            str: 矩形区域内识别出的文字
        """
        if img is None or not rect:
            logger.error("输入图像或矩形区域为空")
            return ""
            
        try:
            x, y, w, h = rect
            roi = img[y:y+h, x:x+w]
            logger.debug(f"识别矩形区域内容: x={x}, y={y}, w={w}, h={h}")
            return self.recognize_content(roi)
        except Exception as e:
            logger.error(f"矩形区域识别错误: {e}")
            return ""
