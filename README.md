# Breakout Game – Turtle Edition

A classic **Breakout / Arkanoid**-style game implemented using only Python's built-in **`turtle`** module.

Control the paddle with arrow keys, bounce the ball, and destroy all the colored blocks!

## 🎮 Gameplay

- Use **← Left** and **→ Right** arrow keys to move the paddle
- Break all the blocks to win (score increases with each hit)
- If the ball falls below the paddle → reset to starting position
- Game continues until you close the window

## Features

- Colorful block layout (yellow, green, orange, red rows)
- Smooth paddle and ball movement
- Basic collision detection (paddle, walls, blocks)
- Score tracking
- Simple reset when ball is lost
- No external libraries required — pure `turtle`

## Project Structure
├── main.py             # Game loop, screen setup & main logic (this file)
├── paddle.py           # Paddle class & movement logic
├── ball.py             # Ball class, movement & bouncing
├── blocks.py           # Block class for bricks
├── scoreboard.py       # Score display & point system


## Requirements

- **Python 3.x** (any recent version)
- Only built-in **`turtle`** module  
  → No `pip install` needed!

## How to Run

1. Make sure all files are in the same folder:
   - `main.py`
   - `paddle.py`
   - `ball.py`
   - `blocks.py`
   - `scoreboard.py`

2. Run the game:

```bash
python main.py
