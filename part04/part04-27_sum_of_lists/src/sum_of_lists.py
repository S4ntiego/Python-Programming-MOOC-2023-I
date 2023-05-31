# Write your solution here
def list_sum(list_1, list_2):
    sum = []
    i = 0
    while i < len(list_1):
        print(list_1[i])
        sum.append((list_1[i] + list_2[i]))
        i += 1
    return sum
