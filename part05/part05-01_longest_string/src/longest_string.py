# Write your solution here
def longest(list):
    best = ""
    for string in list:
        if len(string) > len(best):
            best = string
    return best


if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))
