# write your solution here
def row_sums():
    with open("matrix.txt") as new_file:
        content = new_file.read()
        rows = content.strip().split("\n")
        matrix = []
        sum = []
        for row in rows:
            matrix.append([int(num) for num in row.split(",")])
        for row in matrix:
            row_sum = 0
            for number in row:
                row_sum += number
            sum.append(row_sum)
        return sum


def matrix_sum():
    with open("matrix.txt") as new_file:
        content = new_file.read()
        rows = content.strip().split("\n")
        matrix = []
        total_sum = 0
        for row in rows:
            matrix.append([int(num) for num in row.split(",")])
        for row in matrix:
            total_sum += sum(row)
        return total_sum


def matrix_max():
    with open("matrix.txt") as new_file:
        content = new_file.read()
        rows = content.strip().split("\n")
        matrix = []
        max_number = 0
        for row in rows:
            matrix.append([int(num) for num in row.split(",")])
            max_number = matrix[0][0]
        for row in matrix:
            for number in row:
                if number > max_number:
                    max_number = number
        return max_number
