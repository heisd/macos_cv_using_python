## 项目简介

本仓库用于记录和实践我在学习 OpenCV（Python 版）过程中的代码与示例。每个 `*.py` 文件通常对应一个独立的小练习或功能模块，便于逐步掌握图像读取、处理与保存等核心能力。

> 说明：项目最初在 macOS 上开发与测试，但同样支持 Windows 与 Linux。当前 Python 解释器版本以 3.10 为主。

---

## 功能概览

- 图像读取、显示与保存
- 图像缩放、裁剪、ROI 与像素级操作
- 基于示例图片的入门练习与输出对比

---

## 环境依赖

- Python 3.10+
- 必要库：`opencv-python`
- 操作系统：Windows / macOS / Linux

安装依赖示例：

```powershell
# 建议在虚拟环境中安装（Windows PowerShell）
python -m venv .venv
.\.venv\Scripts\Activate
pip install --upgrade pip
pip install opencv-python
```

```bash
# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install opencv-python
```

如果你不熟悉 Python 虚拟环境，可参考这篇文章：
[python 创建虚拟环境（外部参考）](https://blog.csdn.net/2303_77125642/article/details/151576389?spm=1001.2014.3001.5501)

---

## 快速开始

1. 克隆或下载本仓库。
2. 按上文创建并激活虚拟环境，安装依赖。
3. 进入 `opencv/src` 目录，运行示例脚本（按需替换文件名）：

```powershell
cd opencv/src
python opencv.py
```

---

## 目录结构

```text
opencv/
  image/                 # 示例输入图片
  output/image/          # 处理结果输出目录
  read/readme            # 学习笔记/随记
  src/                   # 源码（独立小模块）
    opencv.py
    opencv_core.py
    opencv_core2.py
    opencv_core3.py
```

- `image` 文件夹包含用于测试的图片，来源参考见下文。
- `output/image` 用于保存脚本的输出结果（如 `ReszieImage.png`、`RIOImage.png` 等）。
- `src` 下的每个 `*.py` 文件对应一个学习模块，可独立运行。

---

## 使用示例

以下仅为示意，具体以脚本实现为准：

```python
# opencv/src/opencv.py（示例：读取并保存图像）
import cv2

image = cv2.imread('../image/image.png')
cv2.imwrite('../output/image/saved_image.png', image)
```

运行后，可在 `opencv/output/image` 下查看输出结果图片。

---

## 参考与致谢

- 示例图片与部分思路参考自：
  [菜鸟教程 · OpenCV 教程](https://www.runoob.com/opencv/opencv-install.html)

欢迎 Issue / PR 指正与改进，一起交流学习！


