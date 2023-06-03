# Write your solution here
phonebook = {}
while True:
    command = int(input("command (1 search, 2 add, 3 quit): "))
    if command == 1:
        name = input("name: ")
        if name in phonebook:
            print(f"{phonebook[name]}")
        else:
            print("no number")
    elif command == 2:
        name = input("name: ")
        number = input("number: ")
        phonebook[name] = number
        print("ok!")
    elif command == 3:
        print("quitting...")
        break
