# 单词自动化助手

这是一个用于自动化处理单词学习应用的程序，能够自动识别不同类型的页面并执行相应操作。

## 功能说明

- **自动识别页面类型**：能够识别单词页面、跟读提示、选择题、音频题等不同类型
- **自动执行操作**：根据页面类型自动点击按钮、选择答案等
- **音频识别**：能够监听并识别音频内容
- **AI辅助答题**：通过豆包API获取选择题答案
- **暂停/退出控制**：提供直观的UI界面进行控制

## 技术栈

- **Python 3.7+**：主要开发语言
- **Appium**：安卓自动化框架
- **OpenCV**：图像处理
- **Tesseract**：OCR文字识别
- **SpeechRecognition**：音频识别
- **Tkinter**：UI界面

## 安装依赖

```bash
# 使用国内镜像源安装依赖
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple appium-python-client opencv-python pytesseract speechrecognition requests pillow
```

## 环境配置

1. **安装Tesseract OCR**：
   - Windows：下载安装 [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
   - Linux：`sudo apt install tesseract-ocr tesseract-ocr-eng tesseract-ocr-chi-sim`
   - macOS：`brew install tesseract tesseract-lang`

2. **配置Tesseract路径**：
   - 在 `image_recognition.py` 中修改 `tesseract_cmd` 路径

3. **安装Appium**：
   - 安装Node.js：`https://nodejs.org/`
   - 安装Appium：`npm install -g appium`
   - 安装Appium驱动：`appium driver install uiautomator2`

4. **配置安卓设备**：
   - 启用开发者选项和USB调试
   - 连接安卓设备到电脑
   - 确保 `adb devices` 能识别设备

## 使用方法

1. **启动Appium服务器**：
   ```bash
   appium
   ```

2. **启动单词应用**：
   - 在安卓设备上打开目标单词应用

3. **运行自动化程序**：
   ```bash
   python main.py
   ```

4. **控制程序**：
   - 使用弹出的UI窗口进行暂停/恢复和退出操作

## 页面类型处理

### 1. 单词页面（第一张图片）
- 识别特征：包含单词和"下一个"按钮
- 自动操作：点击"下一个"按钮

### 2. 跟读提示（第二张图片）
- 识别特征：包含"温馨提示"和"暂不跟读"按钮
- 自动操作：点击"暂不跟读"按钮

### 3. 选择题（第三张图片）
- 识别特征：包含"检测"和多个选项
- 自动操作：识别题目，调用豆包API获取答案，点击正确选项

### 4. 音频题（第四张图片）
- 识别特征：包含耳机图标和多个选项
- 自动操作：监听音频，识别内容，点击匹配选项

### 5. 提交页面
- 识别特征：包含"提交"或"完成"按钮
- 自动操作：点击"提交"按钮

### 6. 休息弹窗
- 识别特征：包含"休息"相关文字
- 自动操作：选择"不休息"选项

## 注意事项

1. **权限要求**：
   - 程序需要麦克风权限进行音频识别
   - 安卓设备需要USB调试权限

2. **兼容性**：
   - 需要安卓5.0以上系统
   - 不同设备可能需要调整屏幕坐标和元素定位

3. **网络要求**：
   - 需要网络连接进行AI答题
   - 音频识别需要网络连接

4. **性能优化**：
   - 建议使用性能较好的设备
   - 避免同时运行过多程序

## 配置调整

可以在 `main.py` 中调整以下配置：

- `desired_caps`：安卓设备和应用配置
- `time.sleep()`：操作间隔时间
- `tesseract_config`：OCR识别参数

## 常见问题

### Q: 无法连接到Appium服务器
A: 确保Appium服务器已启动，端口号正确，设备已连接

### Q: 无法识别页面内容
A: 检查Tesseract配置，确保安装了正确的语言包

### Q: 音频识别失败
A: 检查麦克风权限，确保环境安静

### Q: 豆包API调用失败
A: 检查网络连接，可能需要调整API调用方式

## 开发说明

本程序基于Appium实现，需要在电脑上运行并连接安卓设备。如果需要真正的安卓端应用，建议使用Java/Kotlin或跨平台框架开发。

## 许可证

MIT License
