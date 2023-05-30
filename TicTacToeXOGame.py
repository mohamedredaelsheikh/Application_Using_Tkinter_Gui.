import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.player = "X"
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.turns = 0
        self.game_over = False
        
    def apply_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.player
            self.turns += 1
            return True
        else:
            return False
        
    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False
    
    def switch_player(self):
        if self.player == "X":
            self.player = "O"
        else:
            self.player = "X"

class TicTacToeGUI:
    def __init__(self):
        self.game = TicTacToe()
        
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.root, text="", font=("Arial", 20), width=5, height=2, command=lambda row=i, col=j: self.button_click(row, col))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)
        
        self.label = tk.Label(self.root, text="Turn: X", font=("Arial", 16))
        self.label.grid(row=3, column=0, columnspan=3)
        
        restart_button = tk.Button(self.root, text="Restart", font=("Arial", 16), command=self.restart_game)
        restart_button.grid(row=4, column=0, columnspan=3)
        
        self.root.mainloop()
    
    def button_click(self, row, col):
        if not self.game.game_over:
            if self.game.apply_move(row, col):
                self.buttons[row][col].config(text=self.game.player)
                if self.game.check_winner():
                    self.game.game_over = True
                    messagebox.showinfo("Game Over", f"Player {self.game.player} wins!")
                elif self.game.turns == 9:
                    self.game.game_over = True
                    messagebox.showinfo("Game Over", "Tie game!")
                else:
                    self.game.switch_player()
                    self.label.config(text=f"Turn: {self.game.player}")
    
    def restart_game(self):
        self.game = TicTacToe()
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")
        self.label.config(text="Turn: X")


game=TicTacToeGUI()