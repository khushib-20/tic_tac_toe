class Board:
    WIN_COMBINATIONS = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
        (0, 4, 8), (2, 4, 6),              # diagonals
    ]

    def __init__(self):
        self.cells = [" "] * 9

    def available_moves(self):
        return [i for i, cell in enumerate(self.cells) if cell == " "]

    def make_move(self, index, mark):
        if self.cells[index] != " ":
            raise ValueError(f"Cell {index} is already occupied.")
        self.cells[index] = mark

    def undo_move(self, index):
        self.cells[index] = " "

    def is_full(self):
        return " " not in self.cells

    def winner(self):
        for a, b, c in self.WIN_COMBINATIONS:
            if self.cells[a] != " " and self.cells[a] == self.cells[b] == self.cells[c]:
                return self.cells[a]
        return None

    def is_game_over(self):
        return self.winner() is not None or self.is_full()

    def copy(self):
        new_board = Board()
        new_board.cells = self.cells.copy()
        return new_board

    def display(self):
        rows = []
        for r in range(3):
            row_cells = self.cells[r * 3:(r + 1) * 3]
            rows.append(" | ".join(row_cells))
        print(("\n" + "-" * 9 + "\n").join(rows))
        print()
