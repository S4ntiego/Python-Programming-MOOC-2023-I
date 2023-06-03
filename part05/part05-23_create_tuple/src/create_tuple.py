# Write your solution here
def create_tuple(x: int, y: int, z: int):
    arr = [x, y, z]
    sorted_arr = sorted(arr)
    smallest = sorted_arr[0]
    largest = sorted_arr[-1]
    sorted_sum = sum(sorted_arr)

    tuple = (sorted_arr[0], sorted_arr[-1], sorted_sum)
    return tuple


if __name__ == "__main__":
    create_tuple(1, 2, 3)
