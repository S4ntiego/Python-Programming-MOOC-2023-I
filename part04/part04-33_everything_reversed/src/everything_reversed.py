# Write your solution here
def everything_reversed(list: list):
    new_list = []
    i = 0
    for item in list:
        new_list.append(item[::-1])
        i += 1
    return new_list[::-1]
