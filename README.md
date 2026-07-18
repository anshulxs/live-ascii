# live-ascii

A lightweight Python app that converts your webcam feed into a live terminal art stream in real time. Two modes: `ascii` (classic ASCII art) and `color` (colored `@` blocks).

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

```bash
python main.py <mode>
```

Where `<mode>` is one of:

- `ascii` — classic webcam-to-ASCII-art conversion
- `color` — colored output using the `@` symbol for each pixel (no ASCII conversion)

**With uv:**
```bash
uv run main.py ascii
uv run main.py color
```

**With pip:**
```bash
python main.py ascii
python main.py color
```

The output streams directly in the terminal you ran the script from. Press `q` to exit cleanly.

## Dependencies

| Package | Purpose |
|--------|---------|
| `opencv-python` | Capturing the webcam feed |
| `Pillow` | Image processing |
| `rich` | Rendering ASCII/color output to the terminal |

## How it works

Two classes, each with one job:

- **`VideoCapture`** — opens the camera and reads frames
- **`AsciiArt`** — converts a frame into either ASCII (`ascii` mode) or colored `@` blocks (`color` mode)

`main.py` reads the `<mode>` argument and wires everything together in a live loop, using `rich` to print each frame straight to the terminal until `q` is pressed.