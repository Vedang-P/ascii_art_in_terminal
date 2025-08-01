﻿# ascii_art_in_terminal
GPU-Accelerated ASCII Webcam

A real-time ASCII art generator that converts your webcam feed (including phone cameras) into colored ASCII art with advanced AI-powered background removal and GPU acceleration.

![ASCII Webcam Demo](https://imgimg.shields.io/badge/Pythonshields.io/badge/GPU-CUDA%

    🎥 Real-time ASCII conversion - Live webcam feed to colored ASCII art

    🚀 GPU acceleration - CUDA/TensorRT support for faster processing

    🎭 AI background removal - Advanced segmentation using REMBG models

    📱 Phone camera support - Use your phone as a high-quality webcam

    📊 Live progress monitoring - Beautiful terminal UI with real-time stats

    🌈 Full color support - ANSI color codes for vibrant ASCII art

    ⚡ Performance optimized - Background threading and smart frame queuing

🎯 Demo

The application provides:

    Dual camera display: Original feed + AI-processed mask side by side

    Live terminal interface: Progress bars, FPS counter, and GPU status

    High-quality ASCII: Clean background removal with accurate edge detection

🛠️ Installation
Prerequisites

    Python 3.8+ (MediaPipe alternative works with Python 3.13)

    NVIDIA GPU (optional, for acceleration)

    Webcam or phone camera set up as webcam

Quick Install

bash
# Clone or download the script
# Install dependencies with GPU support
pip install onnxruntime-gpu rembg[gpu] opencv-python pillow rich progress tqdm

# Or for CPU-only version
pip install onnxruntime rembg opencv-python pillow rich progress tqdm

Phone Camera Setup (Optional)

Windows 11 Users:

    Install "Link to Windows" app on your Android phone

    Go to Settings > Bluetooth & devices > Mobile devices

    Enable "Allow this PC to access your mobile devices"

    Pair your phone and enable "Use as a connected camera"

Alternative Apps:

    iVCam - High-quality wireless webcam

    DroidCam - Free webcam app

    Camo Studio - Professional features

🚀 Usage
Basic Usage

bash
python gpu_ascii_webcam.py

What You'll See

    Setup Phase:

        GPU acceleration detection

        Camera initialization

        Model loading with progress

    Live Operation:

        Camera window with original + processed feeds

        Terminal interface with live stats

        Real-time colored ASCII art generation

📋 Requirements

text
opencv-python>=4.5.0
numpy>=1.21.0
pillow>=8.0.0
rembg[gpu]>=2.0.0
onnxruntime-gpu>=1.12.0
rich>=12.0.0
progress>=1.6
tqdm>=4.64.0

🎛️ Configuration
Camera Settings

The script automatically detects available cameras. For phone cameras:

python
# Camera will be auto-detected, but you can specify index
camera_index = 0  # Built-in webcam
camera_index = 1  # Usually phone camera when connected

ASCII Art Quality

python
# Adjust ASCII resolution (default: 75-90 characters wide)
ascii_art = frame_to_colored_masked_ascii(frame, mask, width=90)

# ASCII character set (from darkest to lightest)
ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.', ' ']

GPU Configuration

python
# GPU acceleration is automatic, but you can check status
providers = session.inner_session.get_providers()
# Will use: CUDA > TensorRT > CPU (in that order)

🔧 Troubleshooting
Common Issues

GPU Not Detected:

bash
# Verify CUDA installation
nvidia-smi

# Reinstall GPU runtime
pip uninstall onnxruntime onnxruntime-gpu
pip install onnxruntime-gpu

Camera Not Found:

bash
# List available cameras
# The script will automatically try indices 0-4
# Check Windows Device Manager for camera status

Dependencies Missing:

bash
# Complete reinstall
pip install --upgrade --force-reinstall onnxruntime-gpu rembg[gpu] opencv-python pillow rich

Performance Tips

    For better quality: Use phone camera instead of built-in webcam

    For faster processing: Enable GPU acceleration

    For smoother performance: Close other GPU-intensive applications

    For cleaner backgrounds: Ensure good lighting and contrast

🎨 Customization
ASCII Characters

Modify the ASCII_CHARS array to change the visual style:

python
# High contrast
ASCII_CHARS = ['█', '▓', '▒', '░', ' ']

# Classic style
ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.', ' ']

Color Schemes

The application uses full RGB ANSI colors. Terminal compatibility:

    ✅ Windows Terminal

    ✅ PowerShell 7+

    ✅ VS Code Terminal

    ✅ Modern terminals with ANSI support

Background Models

Available REMBG models (in order of quality vs speed):

python
session = new_session('u2net')          # Best quality (default)
session = new_session('u2netp')         # Lighter version
session = new_session('isnet-general')  # Fast processing

📊 Performance Metrics

Typical Performance:

    With GPU: 15-25 FPS at 720p

    CPU Only: 5-10 FPS at 720p

    Memory Usage: 2-4 GB (including GPU VRAM)

    Background Processing: 50-200ms per frame

🤝 Contributing

Feel free to submit issues, suggestions, or pull requests! Some areas for improvement:

    Additional background removal models

    Mobile app integration

    Real-time parameter adjustment

    Export functionality (GIF/video)

    Multiple person detection

📄 License

This project is open source and available under the MIT License.
🙏 Acknowledgments

    REMBG - Excellent background removal library

    OpenCV - Computer vision foundation

    Rich - Beautiful terminal interfaces

    MediaPipe - Alternative AI segmentation (for compatible Python versions)

🔗 Related Projects

    REMBG - Background removal tool

    OpenCV - Computer vision library

    Rich - Rich text and beautiful formatting
