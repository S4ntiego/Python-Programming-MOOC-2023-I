# Write your solution here
from string import ascii_letters, digits


def change_case(orig_string: str):
    return orig_string.swapcase()


def split_in_half(orig_string: str):
    string_length = len(orig_string)
    part_1 = slice(0, string_length // 2)
    part_2 = slice(string_length // 2, string_length)
    string_tuple = (orig_string[part_1], orig_string[part_2])
    return string_tuple


def remove_special_characters(orig_string: str):
    new_string = ""
    for character in orig_string:
        if character == " " or character in ascii_letters or character in digits:
            new_string += character
    return new_string
