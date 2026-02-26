#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
测试脚本：用于验证各个模块的功能
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from vocabauto import (
    ImageRecognizer,
    AudioListener,
    DoubaoAPI,
    AutomationHandler,
    OverlayUI
)

def test_image_recognition():
    """测试图像识别模块"""
    print("\n=== 测试图像识别模块 ===")
    
    try:
        recognizer = ImageRecognizer()
        print("图像识别模块初始化成功")
        
        # 测试内容提取功能
        test_content = "Wood often ______ when wet.\nshrinks\nswells\ntightens"
        question, options = recognizer.extract_question_options(test_content)
        print(f"提取问题: {question}")
        print(f"提取选项: {options}")
        
        return True
    except Exception as e:
        print(f"图像识别模块测试失败: {e}")
        return False

def test_audio_listener():
    """测试音频监听模块"""
    print("\n=== 测试音频监听模块 ===")
    
    try:
        listener = AudioListener()
        print("音频监听模块初始化成功")
        print("注意：音频监听需要麦克风权限，跳过实际监听测试")
        return True
    except Exception as e:
        print(f"音频监听模块测试失败: {e}")
        return False

def test_doubao_api():
    """测试豆包API模块"""
    print("\n=== 测试豆包API模块 ===")
    
    try:
        doubao = DoubaoAPI()
        print("豆包API模块初始化成功")
        
        # 测试选项匹配功能
        test_answer = "正确答案是 swells"
        test_options = ["shrinks", "swells", "tightens"]
        matched = doubao._match_option(test_answer, test_options)
        print(f"匹配答案 '{test_answer}' 与选项 {test_options}")
        print(f"匹配结果: {matched}")
        
        return True
    except Exception as e:
        print(f"豆包API模块测试失败: {e}")
        return False

def test_automation_handler():
    """测试自动化处理模块"""
    print("\n=== 测试自动化处理模块 ===")
    
    try:
        automation = AutomationHandler()
        print("自动化处理模块初始化成功")
        print("注意：自动化操作需要连接安卓设备，跳过实际点击测试")
        
        return True
    except Exception as e:
        print(f"自动化处理模块测试失败: {e}")
        return False

def test_ui_module():
    """测试UI模块"""
    print("\n=== 测试UI模块 ===")
    
    try:
        ui = OverlayUI()
        print("UI模块初始化成功")
        print("注意：UI界面需要图形环境，跳过实际显示测试")
        
        return True
    except Exception as e:
        print(f"UI模块测试失败: {e}")
        return False

def main():
    """主测试函数"""
    print("开始测试各个模块...")
    
    results = {
        "图像识别": test_image_recognition(),
        "音频监听": test_audio_listener(),
        "豆包API": test_doubao_api(),
        "自动化处理": test_automation_handler(),
        "UI模块": test_ui_module()
    }
    
    print("\n=== 测试结果汇总 ===")
    passed = 0
    total = len(results)
    
    for module, result in results.items():
        status = "✓ 测试通过" if result else "✗ 测试失败"
        print(f"{module}: {status}")
        if result:
            passed += 1
    
    print(f"\n总测试结果: {passed}/{total} 个模块测试通过")
    
    if passed == total:
        print("所有模块测试通过！")
        return 0
    else:
        print("部分模块测试失败，请检查错误信息")
        return 1

if __name__ == "__main__":
    sys.exit(main())
