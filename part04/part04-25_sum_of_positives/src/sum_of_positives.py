# Write your solution here
def sum_of_positives(list):
    positives = []
    for number in list:
        if number > 0:
            positives.append(number)
    return sum(positives)
