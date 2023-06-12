# Write your solution here
import random


def lottery_numbers(amount: int, lower: int, upper: int):
    generated_numbers = list(range(lower, upper))
    chosen_numbers = random.sample(generated_numbers, amount)
    return sorted(chosen_numbers)
