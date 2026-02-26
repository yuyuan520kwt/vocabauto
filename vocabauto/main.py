#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import threading
import cv2
import numpy as np
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import os

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

from .image_recognition import ImageRecognizer
from .audio_listener import AudioListener
from .doubao_api import DoubaoAPI
from .automation import AutomationHandler
from .overlay_ui import OverlayUI

class VocabularyAutomation:
    """单词自动化助手主类"""
    
    # 类级别的常量配置
    DEFAULT_APPIUM_URL = 'http://localhost:4723/wd/hub'
    
    def __init__(self):
        """初始化单词自动化助手"""
        self.driver = None
        self.image_recognizer = ImageRecognizer()
        self.audio_listener = AudioListener()
        self.doubao_api = DoubaoAPI()
        self.automation_handler = AutomationHandler()
        self.overlay_ui = OverlayUI()
        
        self.is_paused = False
        self.is_running = True
        
        # Appium配置
        self.desired_caps = {
            'platformName': 'Android',
            'platformVersion': '11',
            'deviceName': 'Android Emulator',
            'appPackage': 'com.example.vocabulary',
            'appActivity': '.MainActivity',
            'noReset': True,
            'automationName': 'UiAutomator2'
        }
        
        logger.info("初始化VocabularyAutomation")
    
    def start(self):
        """启动自动化程序"""
        logger.info("启动自动化程序")
        
        try:
            # 连接Appium服务器
            logger.info(f"连接Appium服务器: {self.DEFAULT_APPIUM_URL}")
            self.driver = webdriver.Remote(self.DEFAULT_APPIUM_URL, self.desired_caps)
            self.automation_handler.set_driver(self.driver)
            logger.info("Appium服务器连接成功")
            
            # 启动UI覆盖层
            self.overlay_ui.start(self)
            
            # 主循环
            logger.info("进入主循环")
            while self.is_running:
                if self.is_paused:
                    logger.debug("程序已暂停")
                    time.sleep(1)
                    continue
                
                # 截图识别
                screenshot = self.driver.get_screenshot_as_png()
                img_array = np.frombuffer(screenshot, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                
                # 识别内容
                content = self.image_recognizer.recognize_content(img)
                logger.info(f"识别到内容: {content[:100]}...")
                
                # 根据不同类型执行操作
                if self._is_type1(content):
                    self._handle_type1()
                elif self._is_type2(content):
                    self._handle_type2()
                elif self._is_type3(content):
                    self._handle_type3(content)
                elif self._is_type4(content):
                    self._handle_type4()
                elif self._is_submit_page(content):
                    self._handle_submit()
                elif self._is_rest_popup(content):
                    self._handle_rest_popup()
                
                time.sleep(2)  # 避免操作过快
                
        except webdriver.common.exceptions.WebDriverException as e:
            logger.error(f"WebDriver错误: {e}")
        except cv2.error as e:
            logger.error(f"OpenCV处理错误: {e}")
        except Exception as e:
            logger.error(f"程序运行错误: {e}")
        finally:
            logger.info("程序即将停止")
            self.stop()
    
    def _is_type1(self, content):
        """判断是否为第一张图片类型（单词页面）
        
        Args:
            content (str): 识别到的文字内容
            
        Returns:
            bool: 是否为第一张图片类型
        """
        is_type = "amateur" in content and "下一个" in content
        if is_type:
            logger.debug("识别为第一张图片类型（单词页面）")
        return is_type
    
    def _is_type2(self, content):
        """判断是否为第二张图片类型（跟读提示）
        
        Args:
            content (str): 识别到的文字内容
            
        Returns:
            bool: 是否为第二张图片类型
        """
        is_type = "温馨提示" in content and "暂不跟读" in content
        if is_type:
            logger.debug("识别为第二张图片类型（跟读提示）")
        return is_type
    
    def _is_type3(self, content):
        """判断是否为第三张图片类型（选择题）
        
        Args:
            content (str): 识别到的文字内容
            
        Returns:
            bool: 是否为第三张图片类型
        """
        is_type = "检测" in content and ("shrinks" in content or "swells" in content or "tightens" in content)
        if is_type:
            logger.debug("识别为第三张图片类型（选择题）")
        return is_type
    
    def _is_type4(self, content):
        """判断是否为第四张图片类型（音频题）
        
        Args:
            content (str): 识别到的文字内容
            
        Returns:
            bool: 是否为第四张图片类型
        """
        is_type = "检测" in content and "loss" in content and "loose" in content and "lose" in content
        if is_type:
            logger.debug("识别为第四张图片类型（音频题）")
        return is_type
    
    def _is_submit_page(self, content):
        """判断是否为提交页面
        
        Args:
            content (str): 识别到的文字内容
            
        Returns:
            bool: 是否为提交页面
        """
        is_type = "提交" in content or "完成" in content
        if is_type:
            logger.debug("识别为提交页面")
        return is_type
    
    def _is_rest_popup(self, content):
        """判断是否为休息弹窗
        
        Args:
            content (str): 识别到的文字内容
            
        Returns:
            bool: 是否为休息弹窗
        """
        is_type = "休息" in content or "休息一下" in content
        if is_type:
            logger.debug("识别为休息弹窗")
        return is_type
    
    def _handle_type1(self):
        """处理第一张图片类型（单词页面）"""
        logger.info("处理第一张图片类型: 点击下一个按钮")
        self.automation_handler.click_button("下一个")
    
    def _handle_type2(self):
        """处理第二张图片类型（跟读提示）"""
        logger.info("处理第二张图片类型: 点击暂不跟读")
        self.automation_handler.click_button("暂不跟读")
    
    def _handle_type3(self, content):
        """处理第三张图片类型（选择题）"""
        logger.info("处理第三张图片类型: 识别选择题")
        question, options = self.image_recognizer.extract_question_options(content)
        answer = self.doubao_api.get_answer(question, options)
        self.automation_handler.click_button(answer)
    
    def _handle_type4(self):
        """处理第四张图片类型（音频题）"""
        logger.info("处理第四张图片类型: 监听音频")
        recognized_text = self.audio_listener.listen()
        # 根据识别结果选择答案
        if recognized_text:
            logger.info(f"识别到音频内容: {recognized_text}")
            # 这里需要根据实际情况匹配答案
            self.automation_handler.click_button(recognized_text)
    
    def _handle_submit(self):
        """处理提交页面"""
        logger.info("处理提交页面: 点击提交按钮")
        self.automation_handler.click_button("提交")
    
    def _handle_rest_popup(self):
        """处理休息弹窗"""
        logger.info("处理休息弹窗: 选择不休息")
        self.automation_handler.click_button("不休息")
    
    def pause(self):
        """暂停程序"""
        self.is_paused = True
        logger.info("程序已暂停")
    
    def resume(self):
        """恢复程序"""
        self.is_paused = False
        logger.info("程序已恢复")
    
    def stop(self):
        """停止程序"""
        logger.info("停止程序")
        
        self.is_running = False
        self.is_paused = False
        
        if self.driver:
            logger.info("关闭Appium驱动")
            self.driver.quit()
            
        if self.overlay_ui:
            logger.info("停止UI覆盖层")
            self.overlay_ui.stop()
            
        if self.audio_listener:
            logger.info("停止音频监听")
            self.audio_listener.stop()
            
        logger.info("程序已停止")

def main():
    """主函数，作为命令行入口点"""
    automation = VocabularyAutomation()
    automation.start()

if __name__ == "__main__":
    main()
