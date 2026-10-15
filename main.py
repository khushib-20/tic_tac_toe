from game import Game
from minimax import MinimaxAI

def main():
    print("Tic-Tac-Toe: You are 'X', the AI is 'O'.")
    print("Cells are numbered 0-8, left to right, top to bottom:")
    print(" 0 | 1 | 2 \n 3 | 4 | 5 \n 6 | 7 | 8 \n")

    ai = MinimaxAI(ai_mark="O", human_mark="X")
    game = Game(player_x="human", player_o=ai)
    game.play()

if __name__ == "__main__":
    main()