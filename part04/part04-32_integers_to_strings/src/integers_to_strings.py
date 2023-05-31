# Write your solution here
def formatted(list: list):
    new_list = []
    for number in list:
        new_list.append(f"{number:.2f}")
    return new_list
