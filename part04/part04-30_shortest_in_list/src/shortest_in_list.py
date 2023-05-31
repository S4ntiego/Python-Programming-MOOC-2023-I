# Write your solution here
# Write your solution here
def shortest(my_list: list):
    best = my_list[0]
    for item in my_list:
        if len(item) < len(best):
            best = item
    return best
