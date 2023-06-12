# Write your solution here
import random
import string


def generate_password(amount: int):
    generated_password = ""
    letters = string.ascii_lowercase
    for i in range(amount):
        random_number = random.randint(0, len(letters) - 1)
        generated_password += letters[random_number]
    return generated_password
