# Write your solution here
array = []
number = 0
while True:
    number = int(input("New item: "))
    if number == 0:
        print("Bye!")
        break
    array.append(number)
    print(f"The list now: {array}")
    print(f"The list in order: {sorted(array)}")
    continue
