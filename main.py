import tkinter as tk
from tkinter import messagebox, simpledialog
import sys


class NaughtsAndCrossesGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()  # Initially hide the main window

    def play_again(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.root.withdraw()  # Hide the window while setting up the new game
        self.setup_new_game()

    def update_button_text(self, x, y, player, buttons, BoardData, WinCon):
        # Update the board data and button text
        BoardData[x][y] = 1 if player == "X" else 2
        buttons[x][y].config(text=player, state="disabled")

        # Check if the game has been won or drawn
        if self.BoardData_Checker(BoardData, WinCon):
            for row in buttons:
                for button in row:
                    button.config(state="disabled")
        else:
            # Toggle player for the next turn
            next_player = "O" if player == "X" else "X"
            # Update all buttons to use the next player
            for i in range(len(BoardData)):
                # Ensure it works for non-square boards
                for j in range(len(BoardData[0])):
                    # If the button is still active
                    if buttons[i][j]['state'] == 'normal':
                        # Update the button command to use the next player
                        buttons[i][j].config(
                            command=lambda x=i, y=j, Player=next_player:
                            self.update_button_text(
                                x, y, Player, buttons, BoardData, WinCon
                            )
                        )

    def create_board_gui(self, BoardData, WinCon):
        self.root.deiconify()  # Show the window if it was previously hidden
        self.root.title("Naughts and Crosses")

        buttons = [
            [None for _ in range(len(BoardData[0]))]
            for _ in range(len(BoardData))
        ]  # Adjust for non-square boards
        for i in range(len(BoardData)):
            for j in range(len(BoardData[0])):  # Adjust for non-square boa`rds
                def action(x=i, y=j, Player="X"):
                    self.update_button_text(x, y, Player, buttons, BoardData,
                                            WinCon)
                buttons[i][j] = tk.Button(self.root, text=" ", font=('normal',
                                          20), height=2, width=5,
                                          command=action)
                buttons[i][j].grid(row=i, column=j)

    def Draw_Check(self, BoardData):
        for row in BoardData:
            if 0 in row:
                return False
        return True

    def Horizontal_Check_Counter(self, BoardData, WinCon):
        for row in BoardData:
            for player in [1, 2]:
                for i in range(len(row) - WinCon + 1):
                    if all(cell == player for cell in row[i:i+WinCon]):
                        return True, player
        return False, 0

    def Vertical_Check_Counter(self, BoardData, WinCon):
        for col in range(len(BoardData[0])):
            for player in [1, 2]:
                for row in range(len(BoardData) - WinCon + 1):
                    if all(
                        BoardData[row+i][col] == player
                            for i in range(WinCon)):
                        return True, player
        return False, 0

    def Diagonal_Check_Counter(self, BoardData, WinCon):
        for player in [1, 2]:
            # Check descending diagonals
            for x in range(len(BoardData) - WinCon + 1):
                for y in range(len(BoardData[0]) - WinCon + 1):
                    if all(
                        BoardData[x+i][y+i] == player
                            for i in range(WinCon)):
                        return True, player
            # Check ascending diagonals
            for x in range(WinCon - 1, len(BoardData)):
                for y in range(len(BoardData[0]) - WinCon + 1):
                    if all(
                        BoardData[x-i][y+i] == player
                            for i in range(WinCon)):
                        return True, player
        return False, 0

    def BoardData_Checker(self, BoardData, WinCon):
        WinCon = int(WinCon)

        checks = [
            self.Horizontal_Check_Counter(BoardData, WinCon),
            self.Vertical_Check_Counter(BoardData, WinCon),
            self.Diagonal_Check_Counter(BoardData, WinCon)
        ]

        for (check, player) in checks:
            if check:
                messagebox.showinfo(
                    "Game Over",
                    "X Won!!!" if player == 1 else "O Won!!!"
                )
                PLAYAG = simpledialog.askstring(
                    "Input",
                    "Want to play again? (Y/N)",
                    parent=self.root
                ).lower()

                if PLAYAG == "y":
                    self.play_again()
                else:
                    messagebox.showinfo("Game Over", "Thank you for playing")
                    sys.exit()
                return True

        if self.Draw_Check(BoardData):
            messagebox.showinfo("Game Over", "No one wins, it is a Draw!!!")
            PLAYAG = simpledialog.askstring(
                    "Input",
                    "Want to play again? (Y/N)",
                    parent=self.root
                ).lower()

            if PLAYAG == "y":
                self.play_again()
            else:
                messagebox.showinfo("Game Over", "Thank you for playing")
                sys.exit()
            return True

        return False

    def PrintBoard(self, BoardData):
        for row in BoardData:
            print(" ".join(
                "X" if cell == 1 else "O" if cell == 2 else "-"
                for cell in row
            ))

    def BoardMaker(self, Size):
        return [[0 for _ in range(Size)] for _ in range(Size)]

    def setup_new_game(self):
        print("Welcome to my Naughts and Crosses Game")
        Size = simpledialog.askinteger(
            "Input",
            "What Size Board do you want?",
            parent=self.root,
            minvalue=3
        )
        if Size is None:
            return  # User cancelled the dialog

        WinCon = simpledialog.askinteger(
            "Input",
            "How many in a row to win?",
            parent=self.root,
            minvalue=3,
            maxvalue=Size
        )
        if WinCon is None:
            return  # User cancelled the dialog

        BoardData = self.BoardMaker(Size)
        self.create_board_gui(BoardData, WinCon)

    def main(self):
        self.root.withdraw()  # Hide the main window initially
        self.setup_new_game()
        self.root.mainloop()  # Keep the application window open


if __name__ == "__main__":
    game = NaughtsAndCrossesGame()
    game.main()
