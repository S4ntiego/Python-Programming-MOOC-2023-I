# Write your solution here
def first_word(sentence):
    return sentence[: sentence.find(" ")]


def second_word(sentence):
    space = sentence.find(" ")
    sentence = sentence[(space + 1) :]
    space = sentence.find(" ")
    if space > 0:
        sentence = sentence[:(space)]
    else:
        sentence = sentence[:]
    return sentence


def last_word(sentence):
    while sentence.find(" ") != -1:
        space = sentence.find(" ")
        sentence = sentence[(space + 1) :]
    return sentence


# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))
