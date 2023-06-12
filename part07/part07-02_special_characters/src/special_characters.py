# Write your solution here
from string import *


def separate_characters(my_string: str):
    pct = punctuation
    lt = ascii_letters
    part_1 = ""
    part_2 = ""
    part_3 = ""
    for letter in my_string:
        if letter in lt:
            part_1 += letter
        elif letter in pct:
            part_2 += letter
        else:
            part_3 += letter
    tpl = (part_1, part_2, part_3)
    return tpl


if __name__ == "__main__":
    separate_characters("elo")
