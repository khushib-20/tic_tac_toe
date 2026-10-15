from board import Board

class Game:
    def __init__(self, player_x, player_o):
        self.board = Board()
        self.players = {"X": player_x, "O": player_o}
        self.current_mark = "X"

    def switch_turn(self):
        self.current_mark = "O" if self.current_mark == "X" else "X"

    def get_human_move(self):
        while True:
            try:
                raw = input(f"Player {self.current_mark}, enter cell (0-8): ")
                index = int(raw)
                if index in self.board.available_moves():
                    return index
                print("That cell is taken or out of range. Try again.")
            except ValueError:
                print("Please enter a number from 0 to 8.")

    def play(self, verbose=True):
        if verbose:
            self.board.display()

        while not self.board.is_game_over():
            player = self.players[self.current_mark]

            if player == "human":
                move = self.get_human_move()
            else: 
                move = player.best_move(self.board)

            self.board.make_move(move, self.current_mark)

            if verbose:
                self.board.display()

            self.switch_turn()

        winner = self.board.winner()
        if verbose:
            print(f"Player {winner} wins!" if winner else "It's a draw!")

        return winner