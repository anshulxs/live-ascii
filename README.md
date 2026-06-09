# live-ascii

A lightweight Python app that converts your webcam feed into live ASCII art in real time.

## Requirements

- Python 3.8+
- A webcam

## Installation

**With uv (recommended):**
```bash
git clone https://github.com/anshulxs/live-ascii.git
cd live-ascii
uv sync
```

**With pip:**
```bash
git clone https://github.com/anshulxs/live-ascii.git
cd live-ascii
pip install -r requirements.txt
```

## Usage

**With uv:**
```bash
uv run main.py
```

**With pip:**
```bash
python main.py
```

Press the window's close button to exit cleanly.

## Dependencies

| Package | Purpose |
|--------|---------|
| `opencv-python` | Capturing the webcam feed |
| `Pillow` | Image processing |
| `tkinter` | Desktop display window (included with Python) |

## How it works

Three classes, each with one job:

- **`VideoCapture`** — opens the camera and reads frames
- **`AsciiArt`** — converts a frame into an ASCII string
- **`Window`** — displays the result in a tkinter window

`main.py` wires them together in a live loop.
