#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
单词自动化助手包
"""

__version__ = "0.1"
__author__ = ""

from .main import VocabularyAutomation
from .image_recognition import ImageRecognizer
from .audio_listener import AudioListener
from .doubao_api import DoubaoAPI
from .automation import AutomationHandler
from .overlay_ui import OverlayUI

__all__ = [
    "VocabularyAutomation",
    "ImageRecognizer",
    "AudioListener",
    "DoubaoAPI",
    "AutomationHandler",
    "OverlayUI"
]
