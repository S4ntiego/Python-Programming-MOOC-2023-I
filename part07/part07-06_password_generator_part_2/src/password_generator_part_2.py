# Write your solution here
import random
import string


def random_letter():
    letters = string.ascii_lowercase
    random_index = random.randint(0, len(letters) - 1)
    return letters[random_index]


def random_number():
    return random.randint(0, 9)


def random_spec():
    print(string.punctuation)
    spec_characters = [
        string.punctuation[0],
        string.punctuation[2],
        string.punctuation[7],
        string.punctuation[8],
        string.punctuation[10],
        string.punctuation[12],
        string.punctuation[18],
    ]
    random_index = random.randint(0, len(spec_characters) - 1)
    return spec_characters[random_index]


def generate_strong_password(amount: int, no: bool, spec: bool):
    generated_password = ""
    no_amount = 0
    spec_amount = 0
    if no == True:
        no_amount = random.randint(1, amount - 2)
        amount = amount - no_amount

    if spec == True:
        spec_amount = random.randint(1, amount - 1)
        amount = amount - spec_amount

    for i in range(no_amount):
        generated_password += str(random_number())
    for i in range(spec_amount):
        generated_password += random_spec()
    for i in range(amount):
        generated_password += random_letter()
    str_password = list(generated_password)
    random.shuffle(str_password)
    return "".join(str_password)


if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(8, True, True))
