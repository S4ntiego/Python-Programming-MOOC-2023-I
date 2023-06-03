# Write your solution here
def remove_smallest(numbers: list):
    smallest = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] < smallest:
            smallest = numbers[i]
    numbers.remove(smallest)
