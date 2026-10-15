class MinimaxAI:
    def __init__(self, ai_mark, human_mark):
        self.ai_mark = ai_mark
        self.human_mark = human_mark

    def best_move(self, board):
        best_score = float("-inf")
        best_index = None

        for move in board.available_moves():
            board.make_move(move, self.ai_mark)
            score = self._minimax(
                board, depth=0, is_maximizing=False,
                alpha=float("-inf"), beta=float("inf"),
            )
            board.undo_move(move)

            if score > best_score:
                best_score = score
                best_index = move

        return best_index

    def _minimax(self, board, depth, is_maximizing, alpha, beta):
        winner = board.winner()
        if winner == self.ai_mark:
            return 10 - depth
        if winner == self.human_mark:
            return depth - 10
        if board.is_full():
            return 0

        if is_maximizing:
            best_score = float("-inf")
            for move in board.available_moves():
                board.make_move(move, self.ai_mark)
                score = self._minimax(board, depth + 1, False, alpha, beta)
                board.undo_move(move)
                best_score = max(best_score, score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
            return best_score
        else:
            best_score = float("inf")
            for move in board.available_moves():
                board.make_move(move, self.human_mark)
                score = self._minimax(board, depth + 1, True, alpha, beta)
                board.undo_move(move)
                best_score = min(best_score, score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break 
            return best_score
