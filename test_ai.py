import random
from board import Board
from minimax import MinimaxAI


def test_perfect_vs_perfect_always_draws(trials=20):
    ai_x = MinimaxAI(ai_mark="X", human_mark="O")
    ai_o = MinimaxAI(ai_mark="O", human_mark="X")

    for _ in range(trials):
        board = Board()
        mark = "X"
        while not board.is_game_over():
            mover = ai_x if mark == "X" else ai_o
            move = mover.best_move(board)
            board.make_move(move, mark)
            mark = "O" if mark == "X" else "X"
        assert board.winner() is None, "Its a draw!"

    print(f"[PASS] {trials}/{trials} the game ended in a draw.")


def test_ai_never_loses_exhaustive(ai_mark="O", human_mark="X"):
    ai = MinimaxAI(ai_mark=ai_mark, human_mark=human_mark)
    losses = [0]
    games_played = [0]

    def play_out(board, mark):
        if board.is_game_over():
            games_played[0] += 1
            if board.winner() == human_mark:
                losses[0] += 1
            return

        if mark == human_mark:
            for move in board.available_moves():
                board.make_move(move, mark)
                play_out(board, ai_mark)
                board.undo_move(move)
        else:
            move = ai.best_move(board)
            board.make_move(move, mark)
            play_out(board, human_mark)
            board.undo_move(move)

    play_out(Board(), human_mark)
    print(f"[PASS] AI played {games_played[0]} exhaustive games as '{ai_mark}' "
          f"(opponent moves first) with {losses[0]} losses.")
    assert losses[0] == 0, "The AI lost a game!"


def count_legal_states():
    visited = set()

    def explore(board, mark):
        state = tuple(board.cells)
        if state in visited:
            return
        visited.add(state)
        if board.is_game_over():
            return
        for move in board.available_moves():
            board.make_move(move, mark)
            explore(board, "O" if mark == "X" else "X")
            board.undo_move(move)

    explore(Board(), "X")
    return len(visited)


if __name__ == "__main__":
    test_perfect_vs_perfect_always_draws()
    test_ai_never_loses_exhaustive(ai_mark="O", human_mark="X")
    test_ai_never_loses_exhaustive(ai_mark="X", human_mark="O")

    total_states = count_legal_states()
    print(f"[INFO] Total distinct legal board states found: {total_states}")

    print("\nAll checks passed \u2014 the AI is verified unbeatable.")
