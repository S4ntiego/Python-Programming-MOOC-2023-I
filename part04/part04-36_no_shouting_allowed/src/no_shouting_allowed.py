# Write your solution here
def no_shouting(list: list):
    pruned_list = []
    for string in list:
        if string.isupper() == False:
            pruned_list.append(string)
    return pruned_list
