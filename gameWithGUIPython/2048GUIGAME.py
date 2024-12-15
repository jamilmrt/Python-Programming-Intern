import random
import tkinter as tk


def initialize_board():
    board = [[0] * 4 for _ in range(4)]
    add_random_tile(board)
    add_random_tile(board)
    return board


def add_random_tile(board):
    empty_cells = [(r, c) for r in range(4) for c in range(4) if board[r][c] == 0]
    if empty_cells:
        r, c = random.choice(empty_cells)
        board[r][c] = random.choice([2, 4])


def slide_row(row):
    # Remove zeros and shift tiles left
    new_row = [tile for tile in row if tile != 0]
    while len(new_row) < 4:
        new_row.append(0)
    return new_row


def merge_row(row):
    # Merge adjacent tiles with the same value
    for i in range(3):
        if row[i] == row[i + 1] and row[i] != 0:
            row[i] *= 2
            row[i + 1] = 0
    return row


def move_left(board):
    for r in range(4):
        board[r] = slide_row(merge_row(slide_row(board[r])))


def move_right(board):
    for r in range(4):
        board[r] = slide_row(merge_row(slide_row(board[r][::-1]))[::-1])


def transpose(board):
    return [list(row) for row in zip(*board)]


def move_up(board):
    board = transpose(board)
    move_left(board)
    board = transpose(board)


def move_down(board):
    board = transpose(board)
    move_right(board)
    board = transpose(board)


def is_win(board):
    return any(2048 in row for row in board)


def is_game_over(board):
    if any(0 in row for row in board):  # Empty space exists
        return False
    # Check if any adjacent tiles can merge
    for r in range(4):
        for c in range(4):
            if (r < 3 and board[r][c] == board[r+1][c]) or (c < 3 and board[r][c] == board[r][c+1]):
                return False
    return True



class Game2048:
    def __init__(self, root):
        self.root = root
        self.board = initialize_board()
        self.tiles = [[None] * 4 for _ in range(4)]
        self.create_gui()
        self.update_gui()

    def create_gui(self):
        self.root.title("2048")
        self.root.bind("<Key>", self.handle_key)
        self.grid = tk.Frame(self.root, bg="black", width=400, height=400)
        self.grid.grid()
        for r in range(4):
            for c in range(4):
                tile = tk.Label(self.grid, text="", bg="lightgray", font=("Helvetica", 20), width=4, height=2)
                tile.grid(row=r, column=c, padx=5, pady=5)
                self.tiles[r][c] = tile

    def update_gui(self):
        for r in range(4):
            for c in range(4):
                value = self.board[r][c]
                self.tiles[r][c].config(text=str(value) if value != 0 else "", bg=self.get_tile_color(value))

    def get_tile_color(self, value):
        colors = {0: "lightgray", 2: "beige", 4: "orange", 8: "gold", 16: "darkorange",
                  32: "red", 64: "darkred", 128: "yellow", 256: "green", 512: "blue", 1024: "purple", 2048: "black"}
        return colors.get(value, "white")

    def handle_key(self, event):
        if event.keysym in ("Left", "Right", "Up", "Down"):
            moves = {"Left": move_left, "Right": move_right, "Up": move_up, "Down": move_down}
            moves[event.keysym](self.board)
            add_random_tile(self.board)
            self.update_gui()
            if is_win(self.board):
                print("You win!")
            elif is_game_over(self.board):
                print("Game over!")

root = tk.Tk()
game = Game2048(root)
root.mainloop()
