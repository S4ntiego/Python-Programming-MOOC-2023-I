# Write your solution here
def invert(dictionary: dict):
    dictionary_swap = dictionary.copy()
    dictionary.clear()
    for i, j in dictionary_swap.items():
        dictionary[j] = i


if __name__ == "__main__":
    invert({1: 10, 2: 20})
