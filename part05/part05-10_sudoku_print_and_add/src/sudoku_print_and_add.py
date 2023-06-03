# Write your solution here
def print_sudoku(sudoku: list):
    for index, row in enumerate(sudoku):
        if index == 3 or index == 6:
            print(" " * 9)
        for index, number in enumerate(row):
            if index == 3 or index == 6:
                print(f" ", end="")
            if number > 0:
                print(f"{number} ", end="")
            else:
                print("_ ", end="")
        print()


def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number
