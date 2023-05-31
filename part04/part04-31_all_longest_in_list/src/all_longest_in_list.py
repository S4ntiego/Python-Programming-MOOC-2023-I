# Write your solution here
def all_the_longest(my_list: list):
    best = [""]
    for item in my_list:
        if len(item) > len(best[0]):
            best.clear()
            best.append(item)
        elif len(item) == len(best[0]):
            best.append(item)
    return best


if __name__ == "__main__":
    all_the_longest(("Alan", "Steve", "Seymour", "Kim", "Susan"))
