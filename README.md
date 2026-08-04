# rogue

A roguelike game built from scratch in Python, using the [python-tcod](https://python-tcod.readthedocs.io/) library for the terminal-style display and event handling.

## Current State

This is early-stage — right now the game renders an `@` player character on an 80x50 grid that you can move around with the arrow keys. It's the foundation the rest of the game (map generation, enemies, combat, etc.) will build on top of.

## Controls

| Key | Action |
|-----|--------|
| ↑ / ↓ / ← / → | Move the player |
| Esc | Quit |

## Tech Stack

- **Python 3**
- **[tcod](https://pypi.org/project/tcod/)** (>=11.13) — handles the console rendering, tileset, and input events
- **numpy** (>=1.18) — tcod dependency, used for console/array operations

## Project Structure

```
rogue/
├── main.py             # Entry point — sets up the console, tileset, and game loop
├── actions.py          # Action classes (MovementAction, EscapeAction)
├── input_handlers.py   # EventHandler — maps key presses to Actions
├── asset.png           # Tilesheet used for rendering
└── requirements.txt
```

## Getting Started

### Prerequisites

- Python 3.9+
- pip

### Installation

```bash
git clone https://github.com/dvyuh/rogue.git
cd rogue
python -m venv .venv
source .venv/bin/activate   # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Run

```bash
python main.py
```

## How It Works

- `main.py` sets up an 80x50 tcod console using `asset.png` as the tileset, and runs the main game loop: render the player, present the frame, then wait for and dispatch input events.
- `input_handlers.py` defines `EventHandler`, a subclass of `tcod.event.EventDispatch`, which listens for key-down events and translates arrow keys into `MovementAction` and Escape into `EscapeAction`.
- `actions.py` defines the `Action` base class along with `MovementAction` (carries a `dx`/`dy` delta) and `EscapeAction`.
