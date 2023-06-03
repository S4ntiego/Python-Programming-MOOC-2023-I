# Write your solution here
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
