# Write your solution here
def factorials(n: int):
    dictionary = {}
    for i in range(1, n + 1):
        if i == 1:
            dictionary[i] = 1
        else:
            dictionary[i] = dictionary[i - 1] * (i)
        i += 1
    return dictionary


if __name__ == "__main__":
    factorials(1)
