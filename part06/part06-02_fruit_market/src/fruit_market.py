# write your solution here
def read_fruits():
    with open("fruits.csv") as new_file:
        contents = new_file.read()
        arr = contents.split("\n")
        arr.remove("")
        fruits = {}
        for item in arr:
            fruits[item.split(";")[0]] = float(item.split(";")[1])
        return fruits
