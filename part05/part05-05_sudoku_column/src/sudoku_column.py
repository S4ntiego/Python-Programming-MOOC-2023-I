# Write your solution here
def column_correct(sudoku, column):
    numbers = []
    for row in sudoku:
        if row[column] in numbers and row[column] != 0:
            return False
        numbers.append(row[column])
    return True
