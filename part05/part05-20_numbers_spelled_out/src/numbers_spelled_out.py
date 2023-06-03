# Write your solution here
def dict_of_numbers():
    numbers_dict = {}
    number_words = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
    }

    for num in range(100):
        if num in number_words:
            numbers_dict[num] = number_words[num]
        else:
            tens = num // 10 * 10
            units = num % 10
            numbers_dict[num] = number_words[tens] + "-" + number_words[units]

    return numbers_dict
