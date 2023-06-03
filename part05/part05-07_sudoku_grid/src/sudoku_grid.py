# Write your solution here
# Write your solution here
def row_correct(sudoku, row):
    i = 1
    while i <= 9:
        number_count = sudoku[row].count(i)
        if number_count > 1:
            return False
        i += 1
    return True


def column_correct(sudoku, column):
    numbers = []
    for row in sudoku:
        if row[column] in numbers and row[column] != 0:
            return False
        numbers.append(row[column])
    return True


def block_correct(sudoku: list, row_no: int, column_no: int):
    i = 0
    j = 0
    numbers = []
    while i < 3:
        while j < 3:
            if (
                sudoku[row_no + i][column_no + j] in numbers
                and sudoku[row_no + i][column_no + j] != 0
            ):
                return False
            numbers.append(sudoku[row_no + i][column_no + j])
            j += 1
        j = 0
        i += 1
    return True


def sudoku_grid_correct(sudoku):
    i = 0
    while i < 9:
        row = row_correct(sudoku, i)
        col = column_correct(sudoku, i)
        if row == False or col == False:
            return False
        i += 1
    j = 0
    k = 0
    while j <= 6:
        while k <= 6:
            block = block_correct(sudoku, j, k)
            if block == False:
                return False
            k += 3
        k = 0
        j += 3
    return True
