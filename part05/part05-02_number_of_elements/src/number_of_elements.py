# Write your solution here
def count_matching_elements(matrix, element):
    matching = 0
    for row in matrix:
        for number in row:
            if number == element:
                matching += 1
    return matching
