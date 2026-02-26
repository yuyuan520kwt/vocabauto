#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

# 读取README.md作为long_description
with open(os.path.join(os.path.dirname(__file__), 'README.md'), 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="vocabauto",
    version="0.1.0",
    description="单词自动化助手 - 用于自动处理单词学习应用的自动化工具",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="",
    author_email="",
    url="",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'vocabauto': ['*.py'],
    },
    install_requires=[
        "kivy>=2.1.0",
        "opencv-python>=4.5.0",
        "requests>=2.25.0",
        "pillow>=8.0.0",
        "appium-python-client>=2.0.0",
        "pytesseract>=0.3.8",
        "speechrecognition>=3.8.1",
        "numpy>=1.20.0",
    ],
    entry_points={
        'console_scripts': [
            'vocabauto = vocabauto.main:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Android",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Topic :: Education",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Topic :: Home Automation",
    ],
    python_requires='>=3.7',
    license="MIT",
    keywords="vocabulary, automation, android, appium, ocr, tesseract, speech-recognition",
    # 使用国内镜像源加速安装
    dependency_links=[
        "https://pypi.tuna.tsinghua.edu.cn/simple/",
        "https://mirrors.aliyun.com/pypi/simple/",
    ],
)
