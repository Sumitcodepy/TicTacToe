import tkinter as tk
from tkinter import font

class game_board(tk.Tk) :

    def __init__(self) :
        super.__init__()
        self.title("Tic Tac Toe")
        self._cells = {}
        self.board_display()

    def board_display(self) :
        display_main = tk.Frame(master = self)
        display_main.pack(fill = tk.X)
        self.display = tk.Label(
            master = display_main,
            text = "Ready",
            font_text = font.Font(size = "28", weight="bold")
        )

        self.display.pack()

    # def board_grid(self) :
    #     grid_frame = tk.Frame(master = self)
    #     grid_frame.pack()


def main() :
    board = game_board()
    board.mainloop()


if __name__ == "__main__" :
    main()