# Tic-Tac-Toe AI — Unbeatable Minimax Opponent

A command-line Tic-Tac-Toe game built with Python, featuring an AI opponent powered by the **Minimax algorithm with alpha-beta pruning**. The AI evaluates possible moves recursively to find optimal strategies and is designed to never lose when playing correctly.

## Overview

This project implements the classic 3×3 Tic-Tac-Toe game with a human player (`X`) competing against an AI opponent (`O`). The AI searches through possible game states, evaluates outcomes, and selects the move with the highest score.

The project also includes automated verification tests that explore possible opponent moves to check that the AI does not lose.

## Features

- **Unbeatable AI Strategy** — Uses Minimax to evaluate possible future game states.
- **Alpha-Beta Pruning** — Reduces unnecessary search by pruning branches that cannot improve the decision.
- **Recursive Game-Tree Search** — Explores possible moves until a win, loss, or draw is reached.
- **Terminal-Based Gameplay** — Play directly in your command-line terminal.
- **Input Validation** — Rejects occupied cells and invalid cell selections.
- **Move Evaluation** — Prioritizes faster wins and delays losses when necessary.
- **Board Management** — Supports legal move generation, win detection, draw detection, and undoing moves.
- **AI Verification Tests** — Checks perfect AI play and explores possible opponent strategies.

## Tech Stack

- **Language:** Python 3
- **AI Algorithm:** Minimax
- **Optimization:** Alpha-beta pruning
- **Testing:** Python assertions and exhaustive game-state exploration

## Getting Started

### Prerequisites

Install [Python 3](https://www.python.org/downloads/) if it is not already installed.

Verify your installation:

```bash
python --version
```

### Installation

Clone the repository:

```bash
git clone https://github.com/khushib-20/tic_tac_toe.git
```

Navigate into the project directory:

```bash
cd tic_tac_toe
```

### Run the Game

Execute the main script:

```bash
python main.py
```

You play as `X`, and the AI plays as `O`.

The board positions are numbered from `0` to `8`, moving from left to right and top to bottom:

```text
 0 | 1 | 2
---+---+---
 3 | 4 | 5
---+---+---
 6 | 7 | 8
```

Enter the number corresponding to the cell where you want to place your mark. The game continues until a player wins or the board is full.

## How the AI Works

The AI uses the Minimax algorithm to evaluate possible moves.

1. **Generate moves:** Identify all available cells.
2. **Simulate a move:** Temporarily place the AI's mark on a candidate cell.
3. **Explore future states:** Recursively evaluate the opponent's possible responses.
4. **Score outcomes:** Assign positive scores to AI wins, negative scores to human wins, and zero to draws. Scores also account for how quickly an outcome is reached.
5. **Prune branches:** Use alpha-beta pruning to skip branches that cannot improve the current decision.
6. **Choose the best move:** Select the move with the highest evaluated score.

Because the game tree is finite and the AI searches for optimal outcomes, it can avoid losing against any legal opponent strategy when implemented and executed correctly.

## Project Structure

```text
tic_tac_toe/
├── board.py       # Board representation and win detection
├── game.py        # Game loop, player turns, and input handling
├── main.py        # Application entry point
├── minimax.py     # Minimax AI with alpha-beta pruning
└── test_ai.py     # AI verification and game-state tests
```

## Testing the AI

Run the verification script:

```bash
python test_ai.py
```

The tests are designed to:

- Check that two perfect AI players produce draws.
- Explore possible human moves to verify that the AI does not lose when playing as `X` or `O`.
- Count distinct reachable board states.

The test script uses exhaustive game-tree exploration for the AI verification checks. Test results are printed in the terminal.

## What I Learned

- Implementing recursive decision-making algorithms
- Applying alpha-beta pruning to game-tree search
- Modeling game states and legal transitions
- Designing modular Python applications
- Testing AI behavior across possible game outcomes

## Future Improvements

- Add a graphical user interface using Pygame or Tkinter.
- Allow users to choose between different difficulty levels.
- Support two-human-player gameplay.
- Display the AI's reasoning and candidate move scores.
- Add a continuous integration workflow to run tests automatically.

## Author

**Khushi Bhamare**

GitHub: [@khushib-20](https://github.com/khushib-20)

---

Built with Python to explore adversarial search and optimal decision-making.
