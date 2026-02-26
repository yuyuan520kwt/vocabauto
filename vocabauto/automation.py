#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 兼容不同版本的appium-python-client
try:
    from selenium.webdriver.common.appiumby import AppiumBy
except ImportError:
    from appium.webdriver.common.appiumby import AppiumBy
import time
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AutomationHandler:
    """自动化操作处理器，用于控制安卓设备的自动操作"""
    
    # 类级别的常量配置
    DEFAULT_TIMEOUT = 10
    DEFAULT_SHORT_TIMEOUT = 5
    
    def __init__(self):
        """初始化自动化操作处理器"""
        self.driver = None
        logger.info("初始化AutomationHandler")
    
    def set_driver(self, driver):
        """设置WebDriver实例
        
        Args:
            driver: Appium WebDriver实例
        """
        self.driver = driver
        logger.info("WebDriver实例已设置")
    
    def click_button(self, button_text, timeout=None):
        """点击指定文本的按钮
        
        Args:
            button_text (str): 按钮文本
            timeout (int): 超时时间，单位秒
            
        Returns:
            bool: 点击是否成功
        """
        timeout = timeout or self.DEFAULT_TIMEOUT
        
        if not self.driver:
            logger.error("WebDriver未初始化")
            return False
        
        if not button_text:
            logger.warning("按钮文本为空")
            return False
            
        logger.info(f"尝试点击按钮: '{button_text}'，超时: {timeout}秒")
        
        # 定位策略列表
        strategies = [
            # 1. 精确文本匹配
            (AppiumBy.XPATH, f"//*[@text='{button_text}']", "精确文本匹配"),
            # 2. 包含文本匹配
            (AppiumBy.XPATH, f"//*[contains(@text, '{button_text}')]", "包含文本匹配"),
            # 3. 内容描述匹配
            (AppiumBy.ANDROID_UIAUTOMATOR, f"new UiSelector().descriptionContains('{button_text}')", "内容描述匹配"),
            # 4. 按钮ID匹配（小写）
            (AppiumBy.ID, f"com.example.vocabulary:id/btn_{button_text.lower()}", "按钮ID匹配（小写）"),
            # 5. 按钮ID匹配（原始）
            (AppiumBy.ID, f"com.example.vocabulary:id/btn_{button_text}", "按钮ID匹配（原始）"),
            # 6. 文本包含（UIAutomator）
            (AppiumBy.ANDROID_UIAUTOMATOR, f"new UiSelector().textContains('{button_text}')", "文本包含（UIAutomator）"),
            # 7. 精确文本（UIAutomator）
            (AppiumBy.ANDROID_UIAUTOMATOR, f"new UiSelector().text('{button_text}')", "精确文本（UIAutomator）"),
            # 8. 资源ID包含
            (AppiumBy.XPATH, f"//*[contains(@resource-id, '{button_text}')]", "资源ID包含")
        ]
        
        # 尝试各种定位策略
        for locator_type, locator, strategy_name in strategies:
            try:
                current_timeout = timeout if locator_type == AppiumBy.XPATH else self.DEFAULT_SHORT_TIMEOUT
                button = WebDriverWait(self.driver, current_timeout).until(
                    EC.element_to_be_clickable((locator_type, locator))
                )
                
                button.click()
                logger.info(f"成功点击按钮 '{button_text}'，使用策略: {strategy_name}")
                return True
                
            except Exception as e:
                logger.debug(f"定位策略 '{strategy_name}' 失败: {e}")
                continue
            
        logger.warning(f"所有定位策略均失败，无法找到按钮: '{button_text}'")
        
        # 作为最后手段，尝试根据坐标点击
        logger.info(f"尝试根据屏幕位置点击按钮: '{button_text}'")
        return self._click_button_by_position(button_text)
    
    def _click_button_by_position(self, button_text):
        """根据屏幕位置点击按钮（作为最后手段）
        
        Args:
            button_text (str): 按钮文本
            
        Returns:
            bool: 点击是否成功
        """
        try:
            # 获取屏幕尺寸
            size = self.driver.get_window_size()
            width = size['width']
            height = size['height']
            
            logger.debug(f"屏幕尺寸: 宽={width}, 高={height}")
            
            # 预定义的按钮位置映射
            position_map = {
                '下一个': (width // 2, height * 0.8),
                '暂不跟读': (width * 0.3, height * 0.6),
                '去跟读': (width * 0.7, height * 0.6),
                '提交': (width // 2, height * 0.8),
                '不休息': (width * 0.3, height * 0.7),
                '休息一下': (width * 0.7, height * 0.7)
            }
            
            if button_text in position_map:
                x, y = position_map[button_text]
                logger.debug(f"根据映射定位按钮 '{button_text}' 到坐标: ({x}, {y})")
                return self.click_coordinates(x, y)
            else:
                logger.warning(f"未找到按钮 '{button_text}' 的位置映射")
        except Exception as e:
            logger.error(f"根据位置点击错误: {e}")
        
        return False
    
    def click_coordinates(self, x, y, duration=500):
        """点击指定坐标
        
        Args:
            x (int): 横坐标
            y (int): 纵坐标
            duration (int): 点击持续时间，单位毫秒
            
        Returns:
            bool: 点击是否成功
        """
        if not self.driver:
            logger.error("WebDriver未初始化")
            return False
            
        try:
            logger.info(f"点击坐标: ({x}, {y})，持续时间: {duration}ms")
            self.driver.tap([(x, y)], duration)
            logger.info(f"成功点击坐标: ({x}, {y})")
            return True
            
        except Exception as e:
            logger.error(f"点击坐标错误: {e}")
            return False
    
    def input_text(self, element_id, text, timeout=None):
        """向输入框输入文本
        
        Args:
            element_id (str): 元素ID
            text (str): 要输入的文本
            timeout (int): 超时时间，单位秒
            
        Returns:
            bool: 输入是否成功
        """
        timeout = timeout or self.DEFAULT_TIMEOUT
        
        if not self.driver:
            logger.error("WebDriver未初始化")
            return False
            
        if not element_id:
            logger.warning("元素ID为空")
            return False
            
        logger.info(f"向元素 '{element_id}' 输入文本: '{text}'，超时: {timeout}秒")
        
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((AppiumBy.ID, element_id))
            )
            
            element.clear()
            element.send_keys(text)
            logger.info(f"成功向元素 '{element_id}' 输入文本: '{text}'")
            return True
            
        except Exception as e:
            logger.error(f"输入文本错误: {e}")
            return False
    
    def swipe(self, start_x, start_y, end_x, end_y, duration=500):
        """滑动屏幕
        
        Args:
            start_x (int): 起始横坐标
            start_y (int): 起始纵坐标
            end_x (int): 结束横坐标
            end_y (int): 结束纵坐标
            duration (int): 滑动持续时间，单位毫秒
            
        Returns:
            bool: 滑动是否成功
        """
        if not self.driver:
            logger.error("WebDriver未初始化")
            return False
            
        logger.info(f"滑动屏幕: ({start_x}, {start_y}) -> ({end_x}, {end_y})，持续时间: {duration}ms")
        
        try:
            self.driver.swipe(start_x, start_y, end_x, end_y, duration)
            logger.info(f"成功滑动屏幕: ({start_x}, {start_y}) -> ({end_x}, {end_y})")
            return True
            
        except Exception as e:
            logger.error(f"滑动屏幕错误: {e}")
            return False
    
    def wait_for_element(self, element_text, timeout=None):
        """等待元素出现
        
        Args:
            element_text (str): 元素文本
            timeout (int): 超时时间，单位秒
            
        Returns:
            bool: 元素是否出现
        """
        timeout = timeout or self.DEFAULT_TIMEOUT
        
        if not self.driver:
            logger.error("WebDriver未初始化")
            return False
            
        if not element_text:
            logger.warning("元素文本为空")
            return False
            
        logger.info(f"等待元素 '{element_text}' 出现，超时: {timeout}秒")
        
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((AppiumBy.XPATH, f"//*[@text='{element_text}']"))
            )
            logger.info(f"元素 '{element_text}' 已出现")
            return True
            
        except Exception as e:
            logger.error(f"等待元素 '{element_text}' 超时: {e}")
            return False
    
    def get_element_text(self, element_id, timeout=None):
        """获取元素文本
        
        Args:
            element_id (str): 元素ID
            timeout (int): 超时时间，单位秒
            
        Returns:
            str: 元素文本
        """
        timeout = timeout or self.DEFAULT_TIMEOUT
        
        if not self.driver:
            logger.error("WebDriver未初始化")
            return ""
            
        if not element_id:
            logger.warning("元素ID为空")
            return ""
            
        logger.info(f"获取元素 '{element_id}' 的文本，超时: {timeout}秒")
        
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((AppiumBy.ID, element_id))
            )
            
            text = element.text
            logger.info(f"成功获取元素 '{element_id}' 的文本: '{text}'")
            return text
            
        except Exception as e:
            logger.error(f"获取元素文本错误: {e}")
            return ""
    
    def is_element_present(self, element_text, timeout=None):
        """检查元素是否存在
        
        Args:
            element_text (str): 元素文本
            timeout (int): 超时时间，单位秒
            
        Returns:
            bool: 元素是否存在
        """
        timeout = timeout or self.DEFAULT_SHORT_TIMEOUT
        
        if not self.driver:
            logger.error("WebDriver未初始化")
            return False
            
        if not element_text:
            logger.warning("元素文本为空")
            return False
            
        logger.debug(f"检查元素 '{element_text}' 是否存在，超时: {timeout}秒")
        
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((AppiumBy.XPATH, f"//*[@text='{element_text}']"))
            )
            logger.debug(f"元素 '{element_text}' 存在")
            return True
        except:
            logger.debug(f"元素 '{element_text}' 不存在")
            return False
