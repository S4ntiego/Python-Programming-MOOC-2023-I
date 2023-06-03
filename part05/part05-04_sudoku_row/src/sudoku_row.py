# Write your solution here
def row_correct(sudoku, row):
    i = 1
    while i <= 9:
        number_count = sudoku[row].count(i)
        if number_count > 1:
            return False
        i += 1
    return True
