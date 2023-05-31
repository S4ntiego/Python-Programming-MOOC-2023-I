# Write your solution here
def distinct_numbers(list):
    distinct = []
    for number in list:
        if distinct.count(number) <= 0:
            distinct.append(number)
    return sorted(distinct)


if __name__ == "__main__":
    distinct_numbers([1, 2, 3])
