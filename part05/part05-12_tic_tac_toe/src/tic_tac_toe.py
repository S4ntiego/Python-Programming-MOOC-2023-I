# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
    if x not in range(len(game_board)):
        return False
    elif y not in range(len(game_board)):
        return False
    elif game_board[y][x] != piece and game_board[y][x] != "O":
        print(game_board)
        game_board[y][x] = piece
        print(game_board)
        return True
    else:
        return False


# else:
#     return False


if __name__ == "__main__":
    game_board = [["X", "O", ""], ["O", "X", "X"], ["", "", ""]]
    play_turn(game_board, 1, 1, "X")
