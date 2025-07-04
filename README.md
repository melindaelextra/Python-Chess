# Python Object-Oriented Chess

A fully functional chess game implemented in Python using object-oriented programming principles, showcasing game logic and board representation. This command-line interface game allows two players to move chess pieces according to basic rules until one player's King is captured.

## Overview

This project focuses on building a simple chess game in Python, leveraging Object-Oriented Programming (OOP) concepts. The primary objectives include understanding and implementing classes and inheritance, creating a playable chess game with fundamental movement rules for each piece, and developing a command-line user interface for game interaction. The game emphasizes core OOP principles and basic game mechanics without delving into advanced chess rules like castling or check/checkmate conditions.

## Features

* **Object-Oriented Design:** Implements a `Piece` base class with subclasses for King, Queen, Rook, Bishop, Knight, and Pawn, each defining its specific movement logic.
* **Board Representation:** Uses an 8x8 2D list to represent the chessboard and store piece positions.
* **Basic Movement Rules:** Adheres to the traditional movement rules for each chess piece type.
* **Turn-Based Gameplay:** Implements a game loop that alternates turns between two players (white and black).
* **Input Handling:** Allows players to input source and destination positions using standard algebraic notation (e.g., `e2`, `h8`).
* **Move Validation:** Validates moves based on piece type, current board state, and ensures players only move their own pieces.
* **Path Blocking (except Knight):** Checks if the path to the destination is blocked by other pieces for Rook, Bishop, Queen, Pawn, and King moves.
* **King Capture Win Condition:** The game ends when one player's King piece is captured.
* **Console Display:** Renders the current board state in a user-friendly format with coordinates.
* **Initial Board Setup:** Automatically sets up the standard starting positions for all pieces.

## Getting Started

### Prerequisites

* Python 3.x installed on your system.
* No external libraries are required beyond standard Python modules (`os`, `time`).

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/Python-OOP-Chess.git](https://github.com/your-username/Python-OOP-Chess.git)
    cd Python-OOP-Chess
    ```
    (Replace `your-username` with your actual GitHub username.)

2.  **Ensure the main script is present:**
    The main script, `Chess.py`, should be in the root directory of the cloned repository.

### Running the Program

Execute the main Python script from your terminal:

```bash
python Chess.py
```

The game will start, display the initial board, and prompt the white player for their move.

## Game Instructions

1.  The board will be displayed, showing piece positions.
    * White pieces are represented by `X1` (e.g., `K1` for White King, `P1` for White Pawn).
    * Black pieces are represented by `X2` (e.g., `K2` for Black King, `P2` for Black Pawn).
    * Empty squares are represented by `.`.
2.  Players will be prompted to enter a "Source Position" and a "Destination Position" using algebraic notation (e.g., `e2` for the square at column 'e', row 2).
3.  The game alternates turns between 'white' and 'black'.
4.  The game ends when a King is captured.

## Project Structure

* `Chess.py`: The main Python script containing all the game logic, including piece classes, board representation, movement rules, validation, and the game loop.
* `Project - OOP Chess.pdf`: The assignment document outlining the project requirements and objectives.

## Movement Logic

Each piece type has its own `move` method, defining its specific movement rules:

* **King:** Moves one square in any direction (horizontally, vertically, or diagonally).
* **Queen:** Moves any number of squares along a row, column, or diagonal.
* **Rook:** Moves any number of squares along a row or column.
* **Bishop:** Moves any number of squares diagonally.
* **Knight:** Moves in an "L" shape (two squares in one cardinal direction, then one square in a perpendicular direction).
* **Pawn:** Moves forward one square (or two from its starting position), and captures diagonally.

## Code Overview

The `Chess.py` script is structured using OOP principles:

* **`Piece` Class:** The base class for all chess pieces, holding common attributes like `owner` (e.g., 'white', 'black') and `position` (a `(col, row)` tuple).
* **Subclasses (King, Queen, Rook, Bishop, Knight, Pawn):** Each subclass inherits from `Piece` and overrides the `move(self, board, destination)` method to implement its unique movement rules.
    * `Pawn` also includes `first_move` to handle its initial two-square move.
* **`Board` Class:** Manages the 8x8 chessboard.
    * `__init__()`: Initializes the board as a 2D list and calls `setup_board()`.
    * `setup_board()`: Places all pieces in their initial positions.
* **`board_display(board)`:** Renders the current state of the chessboard to the console.
* **`convert_input_to_coords(input_str)`:** Converts user input (e.g., "e2") into `(col, row)` integer coordinates.
* **`validation(board, piece, destination, current_player)`:** Performs comprehensive checks to determine if a proposed move is valid, considering piece type, ownership, destination, and path obstructions.
* **`game_loop()`:** The main function that orchestrates the game, handling player turns, input, move execution, and checking for game-ending conditions.

## Exclusions

The current implementation does **not** include:

* Castling functionality.
* Check or checkmate conditions.
* En passant.
* Pawn promotion.

## Contributing

Feel free to fork this repository, make improvements, and submit pull requests.

## License

This project is developed for educational purposes as part of a 5-Week Coding Class.

## Contact

For any questions or feedback, please open an issue in the GitHub repository.
