from typing import Callable
from os import system


def print_board(board: list[str]):
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print(f"---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print(f"---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")


def is_winner(board: list[str], side: str) -> bool:
    return (board[0] == board[1] == board[2] == side) or \
           (board[3] == board[4] == board[5] == side) or \
           (board[6] == board[7] == board[8] == side) or \
           (board[0] == board[3] == board[6] == side) or \
           (board[1] == board[4] == board[7] == side) or \
           (board[2] == board[5] == board[8] == side) or \
           (board[0] == board[4] == board[8] == side) or \
           (board[2] == board[4] == board[6] == side)


def player_move(board: list[str]) -> int:
    print_board(board)
    move = -1
    while not (0 <= move <= 9):
        try:
            move = int(input("Enter an open space: ")) - 1
            if not board[move].isnumeric():
                move = -1
        except (ValueError, IndexError):
            move = -1

    return move


def ai_move(board: list[str]) -> int:
    def score_line(line: list[str]) -> int:
        mine = line.count("O")
        yours = line.count("X")
        blank = 2 - mine - yours
        return abs(10*mine - 9*yours + 5*blank)

    def get_lines(cell: int) -> list[list[int]]:
        sets = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        retval = []
        for line in sets:
            if cell not in line:
                continue
            line.remove(cell)
            retval.append(line)
        return retval

    score = [0] * 9
    for index, box in enumerate(board):
        if not box.isnumeric():
            continue

        for line in get_lines(index):
            score[index] += score_line([board[line[0]], board[line[1]]])

    return score.index(max(score))


def turn(board: list[str], mover: list[Callable[[list[str]], int]], player: int = 0, turn_count: int = 0) -> str:
    if player == 0:
        character = "X"
    else:
        character = "O"

    board[mover[player](board)] = character
    print_board(board)
    if is_winner(board, character):
        return f"Player {player+1} wins!!!"
    elif turn_count == 8:
        return "Tie Game!"
    else:
        return turn(board, mover, (player+1) % 2, turn_count+1)


def main():
    print("Welcome to Tic Tac Toe.")
    print("Here are is the key for this game:")

    board = [str(i) for i in range(1, 10)]
    print_board(board)

    game_type = input("Is this a one or two player game? [1/2]: ")
    while game_type != "1" and game_type != "2":
        game_type = input("Invalid response. [1/2]: ")

    player2 = player_move
    if game_type == 1:
        player2 = ai_move

    print(turn(board, [player_move, player2]))


if __name__ == "__main__":
    main()