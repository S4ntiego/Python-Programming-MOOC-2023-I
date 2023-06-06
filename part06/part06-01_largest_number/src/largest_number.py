# write your solution here
def largest():
    with open("numbers.txt") as new_file:
        contents = new_file.read()
        arr = contents.split("\n")
        arr.remove("")
        for item in arr:
            return int(item)
        return max(arr)
