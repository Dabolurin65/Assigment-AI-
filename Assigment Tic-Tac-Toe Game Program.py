import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.player_turn = True  # True for Player X, False for Player O
        self.board = [""] * 9
        self.create_board()

    def create_board(self):
        """Creates the 3x3 grid buttons for the Tic-Tac-Toe game."""
        self.buttons = []
        for i in range(9):
            button = tk.Button(self.root, text="", font=("Arial", 40), height=2, width=5,
                               command=lambda idx=i: self.on_click(idx))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

        # Reset Button
        reset_button = tk.Button(self.root, text="Reset", font=("Arial", 20), command=self.reset_game)
        reset_button.grid(row=3, column=0, columnspan=1)

        # Exit Button
        exit_button = tk.Button(self.root, text="Exit", font=("Arial", 20), command=self.exit_game)
        exit_button.grid(row=3, column=2, columnspan=1)

    def on_click(self, index):
        """Handles the logic when a player clicks a button on the board."""
        if not self.board[index] and not self.check_winner():
            self.board[index] = "X" if self.player_turn else "O"
            self.buttons[index].config(text=self.board[index])

            if self.check_winner():
                self.show_result(f"Player {self.board[index]} wins!")
            elif all(self.board):
                self.show_result("It's a draw!")
            else:
                self.player_turn = not self.player_turn  # Switch turn

    def check_winner(self):
        """Checks if there is a winner."""
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return True
        return False

    def show_result(self, result):
        """Displays the game result and disables further moves."""
        messagebox.showinfo("Game Over", result)
        self.disable_buttons()

    def disable_buttons(self):
        """Disables all buttons on the board after game ends."""
        for button in self.buttons:
            button.config(state="disabled")

    def reset_game(self):
        """Resets the game to its initial state."""
        self.board = [""] * 9
        self.player_turn = True
        for button in self.buttons:
            button.config(text="", state="normal")

    def exit_game(self):
        """Exits the game by closing the window."""
        self.root.quit()  # Closes the application

# Initialize the main window and run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
