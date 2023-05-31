# Write your solution here
def length_of_longest(my_list: list):
    best = ""
    for item in my_list:
        if len(item) > len(best):
            best = item
    return len(best)
