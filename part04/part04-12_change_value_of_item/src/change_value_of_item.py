# Write your solution here
list = [1, 2, 3, 4, 5]
index = 0
while index != -1:
    index = int(input("Index: "))
    if index == -1:
        break
    new_value = int(input("New value: "))
    list[index] = new_value
    print(list)
    continue
