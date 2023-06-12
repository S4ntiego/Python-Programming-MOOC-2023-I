# Write your solution here
import random


def roll(die: str):
    A = [3, 3, 3, 3, 3, 6]
    B = [2, 2, 2, 5, 5, 5]
    C = [1, 4, 4, 4, 4, 4]

    if die == "A":
        return random.choice(A)
    elif die == "B":
        return random.choice(B)
    elif die == "C":
        return random.choice(C)
    else:
        print("wtf mate")


def play(die1: str, die2: str, times: int):
    dice_1 = 0
    dice_2 = 0
    tie = 0
    for i in range(times):
        roll1 = roll(die1)
        roll2 = roll(die2)
        if roll1 > roll2:
            dice_1 += 1
        elif roll2 > roll1:
            dice_2 += 1
        else:
            tie += 1
    return (dice_1, dice_2, tie)


if __name__ == "__main__":
    print(play("A", "B", 100))
