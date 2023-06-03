# Write your solution here
def who_won(game_board: list):
    empty = 0
    player_one = 0
    player_two = 0
    for row in game_board:
        empty += row.count(0)
        player_one += row.count(1)
        player_two += row.count(2)
    if player_one > player_two:
        return 1
    elif player_two > player_one:
        return 2
    elif player_two == player_one:
        return 0
