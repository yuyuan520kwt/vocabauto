#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import speech_recognition as sr
import threading
import time
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AudioListener:
    """音频监听器，用于监听和识别音频内容"""
    
    # 类级别的常量配置
    DEFAULT_LISTEN_DURATION = 5
    DEFAULT_ADJUST_DURATION = 1.5
    DEFAULT_ENERGY_THRESHOLD = 300
    DEFAULT_LANGUAGE = 'en-US'
    
    def __init__(self):
        """初始化音频监听器"""
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.is_listening = False
        self.listen_thread = None
        self.last_recognized = ""
        
        # 配置音频识别参数
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.energy_threshold = self.DEFAULT_ENERGY_THRESHOLD
        
        logger.info("初始化AudioListener")
    
    def listen(self, duration=None, adjust_duration=None):
        """监听音频并识别文字
        
        Args:
            duration (int): 监听时长，单位秒
            adjust_duration (int): 环境噪音调整时长，单位秒
            
        Returns:
            str: 识别出的文字内容
        """
        duration = duration or self.DEFAULT_LISTEN_DURATION
        adjust_duration = adjust_duration or self.DEFAULT_ADJUST_DURATION
        
        try:
            with self.microphone as source:
                logger.info(f"开始监听音频，时长: {duration}秒")
                # 调整环境噪音
                self.recognizer.adjust_for_ambient_noise(source, duration=adjust_duration)
                logger.debug(f"环境噪音调整完成，能量阈值: {self.recognizer.energy_threshold}")
                
                # 监听音频
                audio = self.recognizer.listen(source, timeout=duration, phrase_time_limit=duration-1)
                logger.info("音频采集完成")
                
                # 尝试多种语音识别引擎以提高成功率
                text = self._recognize_with_multiple_engines(audio)
                
                if text:
                    logger.info(f"识别结果: {text}")
                    self.last_recognized = text
                    return text
                
        except sr.WaitTimeoutError:
            logger.warning("监听超时")
        except sr.UnknownValueError:
            logger.warning("无法识别音频内容")
        except sr.RequestError as e:
            logger.error(f"语音识别服务请求错误: {e}")
        except Exception as e:
            logger.error(f"音频监听错误: {e}")
        
        return ""
    
    def _recognize_with_multiple_engines(self, audio):
        """使用多种语音识别引擎尝试识别
        
        Args:
            audio: 音频数据，由speech_recognition库采集
            
        Returns:
            str: 识别出的文字内容
        """
        # 识别引擎配置列表
        engines = [
            (self.recognizer.recognize_google, {'language': self.DEFAULT_LANGUAGE}, "Google"),
            (self.recognizer.recognize_sphinx, {}, "Sphinx"),  # 本地引擎，不需要网络
        ]
        
        for engine_func, params, engine_name in engines:
            try:
                logger.info(f"使用 {engine_name} 引擎识别...")
                text = engine_func(audio, **params)
                if text and len(text.strip()) > 1:
                    logger.debug(f"{engine_name} 引擎识别成功: {text}")
                    return text.strip()
                else:
                    logger.debug(f"{engine_name} 引擎未识别到有效内容")
            except sr.UnknownValueError:
                logger.debug(f"{engine_name} 引擎无法识别音频")
                continue
            except sr.RequestError as e:
                logger.error(f"{engine_name} 引擎请求错误: {e}")
                continue
            except Exception as e:
                logger.error(f"{engine_name} 引擎识别错误: {e}")
                continue
        
        logger.warning("所有语音识别引擎均未成功识别")
        return ""
    
    def start_continuous_listening(self):
        """开始持续监听音频
        
        持续监听音频并识别内容，识别结果保存在last_recognized属性中
        """
        if self.is_listening:
            logger.warning("已经在持续监听中")
            return
            
        self.is_listening = True
        self.listen_thread = threading.Thread(target=self._continuous_listen, daemon=True)
        self.listen_thread.start()
        logger.info("开始持续监听")
    
    def _continuous_listen(self):
        """持续监听的内部方法"""
        while self.is_listening:
            try:
                with self.microphone as source:
                    # 调整环境噪音
                    self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    
                    try:
                        audio = self.recognizer.listen(source, timeout=3, phrase_time_limit=2)
                        
                        # 使用多引擎识别
                        text = self._recognize_with_multiple_engines(audio)
                        
                        if text and len(text.strip()) > 1:
                            logger.info(f"持续监听识别: {text}")
                            self.last_recognized = text
                    except sr.WaitTimeoutError:
                        pass  # 监听超时，继续下一次监听
                    except sr.UnknownValueError:
                        pass  # 无法识别，继续下一次监听
            except Exception as e:
                logger.error(f"持续监听错误: {e}")
            
            time.sleep(0.5)  # 减少等待时间，提高响应速度
    
    def stop(self):
        """停止监听音频
        
        停止持续监听线程，并清理资源
        """
        if self.is_listening:
            self.is_listening = False
            logger.info("停止监听")
            
        if self.listen_thread and self.listen_thread.is_alive():
            logger.debug("等待监听线程结束")
            self.listen_thread.join(2)  # 等待2秒，超时则强制结束
            logger.debug("监听线程已结束")
