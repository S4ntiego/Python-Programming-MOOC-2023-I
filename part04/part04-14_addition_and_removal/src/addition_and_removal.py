# Write your solution here
list = []
print(f"The list is now {list}")
i = 0
while True:
    function = input("a(d)d, (r)emove or e(x)it: ")
    if function == "d":
        list.append(i + 1)
        i += 1
        print(f"The list is now {list}")
    elif function == "r":
        list.pop((len(list) - 1))
        i -= 1
        print(f"The list is now {list}")
    elif function == "x":
        break
print("Bye!")
