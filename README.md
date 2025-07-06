# Conway's Game of Life

A Python implementation of Conway's Game of Life using Pygame, featuring an interactive GUI with real-time simulation controls.

## 🎮 Demo

![Game of Life Demo](demo.mp4)

*Watch the cellular automaton evolve through generations with various patterns and behaviors*

## 📋 Overview

Conway's Game of Life is a cellular automaton devised by mathematician John Horton Conway in 1970. It's a zero-player game where the evolution is determined by its initial state, requiring no further input. This implementation provides an interactive experience where you can:

- Draw initial patterns by clicking on cells
- Start/pause the simulation
- Reset the grid
- Adjust simulation speed
- Watch complex behaviors emerge from simple rules

## 🔬 The Rules

The Game of Life follows four simple rules:

1. **Underpopulation**: Any live cell with fewer than two live neighbors dies
2. **Survival**: Any live cell with two or three live neighbors survives
3. **Overpopulation**: Any live cell with more than three live neighbors dies
4. **Reproduction**: Any dead cell with exactly three live neighbors becomes alive

## 🚀 Features

- **Interactive Grid**: Click to toggle cell states and create initial patterns
- **Real-time Simulation**: Watch generations evolve in real-time
- **Playback Controls**: Start, pause, and reset functionality
- **Speed Control**: Adjust simulation speed with keyboard shortcuts
- **Clean Interface**: Minimalist design focusing on the cellular automaton
- **Smooth Performance**: Optimized rendering for smooth animation

## 🛠️ Installation

### Prerequisites

- Python 3.7+
- Pygame library

### Setup

1. Clone this repository:
```bash
git clone https://github.com/yourusername/game-of-life.git
cd game-of-life

Install dependencies:

bashpip install pygame

Run the game:

bashpython game_of_life.py
🎯 Controls
Key/ActionFunctionLeft ClickToggle cell state (alive/dead)SpaceStart/Pause simulationRReset grid (clear all cells)↑ ArrowIncrease simulation speed↓ ArrowDecrease simulation speedESCExit game
🎨 Usage

Create Initial Pattern: Click on cells to create your starting configuration
Start Simulation: Press Space to begin the evolution
Observe: Watch how your pattern evolves according to the rules
Experiment: Try different initial patterns to see various behaviors
Reset: Press R to clear the grid and start over

📊 Interesting Patterns to Try
Try creating these famous patterns:

Glider: A pattern that moves across the grid
Oscillators: Patterns that cycle through states
Still Lifes: Stable patterns that don't change
Glider Gun: Patterns that continuously generate gliders

🔧 Technical Details

Grid Size: 80x60 cells (configurable)
Cell Size: 10x10 pixels
Window Size: 800x600 pixels
Frame Rate: 60 FPS with adjustable simulation speed
Language: Python 3
Graphics: Pygame library

🏗️ Code Architecture
The implementation consists of several key components:

Game Class: Main game loop and state management
Cell Grid: 2D array representing the cellular automaton
Rendering System: Efficient drawing of cells and UI
Input Handler: Mouse and keyboard event processing
Evolution Engine: Implementation of Conway's rules

🎓 Educational Value
This project demonstrates several computer science concepts:

Cellular Automata: Understanding emergence and complex systems
Game Development: Event loops, rendering, and user interaction
Algorithm Implementation: Efficient neighbor counting and state updates
Data Structures: 2D arrays and grid manipulation
Performance Optimization: Efficient rendering and computation

🚀 Future Enhancements
Potential improvements for future versions:

 Save/load patterns
 Pattern library with famous configurations
 Zoom and pan functionality
 Statistics tracking (generations, population)
 Different rule sets (other cellular automata)
 Color themes and customization
 Pattern detection and analysis

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.
🙏 Acknowledgments

John Horton Conway for creating the Game of Life
The Pygame community for excellent documentation
Mathematics and computer science communities for continued exploration of cellular automata


"The Game of Life is not just a game, but a fascinating example of how complex behavior can emerge from simple rules." - John Conway
