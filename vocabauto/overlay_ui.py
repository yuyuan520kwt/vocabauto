#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import time
import tkinter as tk
from tkinter import ttk
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class OverlayUI:
    """UI覆盖层，用于提供暂停/恢复和退出按钮"""
    
    # 类级别的常量配置
    DEFAULT_WINDOW_TITLE = "单词自动化助手"
    DEFAULT_WINDOW_GEOMETRY = "200x100+10+10"
    DEFAULT_WINDOW_OPACITY = 0.8
    
    def __init__(self):
        """初始化UI覆盖层"""
        self.root = None
        self.automation = None
        self.is_running = False
        self.ui_thread = None
        logger.info("初始化OverlayUI")
    
    def start(self, automation):
        """启动UI覆盖层
        
        Args:
            automation: VocabularyAutomation实例
        """
        if self.is_running:
            logger.warning("UI已经在运行中")
            return
            
        self.automation = automation
        self.is_running = True
        
        # 在新线程中启动UI，避免阻塞主程序
        self.ui_thread = threading.Thread(target=self._create_ui, daemon=True)
        self.ui_thread.start()
        logger.info("UI覆盖层已启动")
    
    def _create_ui(self):
        """创建UI界面"""
        try:
            self.root = tk.Tk()
            self.root.title(self.DEFAULT_WINDOW_TITLE)
            self.root.geometry(self.DEFAULT_WINDOW_GEOMETRY)
            self.root.attributes("-topmost", True)  # 窗口置顶
            self.root.attributes("-alpha", self.DEFAULT_WINDOW_OPACITY)  # 窗口透明度
            self.root.configure(bg="white")
            
            # 设置窗口样式
            style = ttk.Style()
            style.configure("TButton", font=("Arial", 12), padding=10)
            
            # 创建暂停/恢复按钮
            self.pause_button = ttk.Button(
                self.root,
                text="暂停",
                command=self._toggle_pause,
                style="TButton"
            )
            self.pause_button.pack(side=tk.LEFT, padx=10, pady=20, expand=True)
            
            # 创建退出按钮
            self.exit_button = ttk.Button(
                self.root,
                text="退出",
                command=self._exit_program,
                style="TButton"
            )
            self.exit_button.pack(side=tk.RIGHT, padx=10, pady=20, expand=True)
            
            # 启动主循环
            self.root.protocol("WM_DELETE_WINDOW", self._exit_program)
            self.root.mainloop()
        except Exception as e:
            logger.error(f"创建UI界面错误: {e}")
    
    def _toggle_pause(self):
        """切换暂停/恢复状态"""
        if self.automation:
            if self.automation.is_paused:
                self.automation.resume()
                self.pause_button.config(text="暂停")
                logger.info("程序已恢复运行")
            else:
                self.automation.pause()
                self.pause_button.config(text="恢复")
                logger.info("程序已暂停")
    
    def _exit_program(self):
        """退出程序"""
        logger.info("退出程序")
        self.is_running = False
        if self.automation:
            self.automation.stop()
        if self.root:
            self.root.destroy()
    
    def stop(self):
        """停止UI"""
        logger.info("停止UI")
        self.is_running = False
        if self.root:
            self.root.after(0, self.root.destroy)
        if self.ui_thread and self.ui_thread.is_alive():
            logger.debug("等待UI线程结束")
            self.ui_thread.join(timeout=2)  # 等待2秒，超时则强制结束
            logger.debug("UI线程已结束")
