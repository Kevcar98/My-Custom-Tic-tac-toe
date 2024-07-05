# Naughts and Crosses Game Documentation

## Overview

This Python application implements a customizable Naughts and Crosses (Tic-Tac-Toe) game using the tkinter library for the graphical user interface. The game allows players to specify the size of the board and the number of consecutive symbols needed to win, providing a flexible gaming experience.

## Classes

### NaughtsAndCrossesGame

#### Methods

- `__init__(self)`
  - Initializes the game window and hides it initially.

- `play_again(self)`
  - Resets the game board and starts a new game.

- `update_button_text(self, x, y, player, buttons, BoardData, WinCon)`
  - Updates the board data and button text after a move, checks for a win or draw, and toggles the player.

- `create_board_gui(self, BoardData, WinCon)`
  - Creates the game board GUI with buttons for each cell.

- `Draw_Check(self, BoardData)`
  - Checks if the board is full without any player winning.

- `Horizontal_Check_Counter(self, BoardData, WinCon)`
  - Checks for a horizontal win condition.

- `Vertical_Check_Counter(self, BoardData, WinCon)`
  - Checks for a vertical win condition.

- `Diagonal_Check_Counter(self, BoardData, WinCon)`
  - Checks for a diagonal win condition.

- `BoardData_Checker(self, BoardData, WinCon)`
  - Checks the board data for a win or draw and handles the end of the game.

- `PrintBoard(self, BoardData)`
  - Prints the current state of the board to the console.

- `BoardMaker(self, Size)`
  - Generates a new game board based on the specified size.

- `setup_new_game(self)`
  - Sets up a new game by asking the player for the board size and win condition.

- `main(self)`
  - The main entry point for the game. It initializes the game window and starts the game loop.

## Dependencies

- tkinter: For the GUI components.
- sys: For exiting the application.

## Usage

To start the game, run the script from the command line. The game will prompt you for the board size and the number of symbols in a row needed to win. After these inputs, the game board will be displayed, and you can start playing by clicking on the cells.

## Example

```python
if __name__ == "__main__":
    game = NaughtsAndCrossesGame()
    game.main()