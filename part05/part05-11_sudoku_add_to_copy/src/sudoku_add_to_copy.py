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


def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    new_sudoku = [row.copy() for row in sudoku]
    new_sudoku[row_no][column_no] = number
    return new_sudoku


if __name__ == "__main__":
    s = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    res = copy_and_add(s, 1, 1, 5)
    print(res)
    print(s)
