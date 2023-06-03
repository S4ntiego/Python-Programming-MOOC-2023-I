# Write your solution here
def histogram(word: str):
    histogram = {}
    for letter in word:
        if letter not in histogram:
            histogram[letter] = []
        histogram[letter].append("*")
    for key, value in histogram.items():
        print(f"{key} ", end="")
        for star in value:
            print(f"{star}", end="")
        print()
