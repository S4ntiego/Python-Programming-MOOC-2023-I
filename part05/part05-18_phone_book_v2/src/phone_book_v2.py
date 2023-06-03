# Write your solution here
phonebook = {}
while True:
    command = int(input("command (1 search, 2 add, 3 quit): "))
    if command == 1:
        name = input("name: ")
        if name in phonebook:
            for value in phonebook[name]:
                print(value)
        else:
            print("no number")
    elif command == 2:
        name = input("name: ")
        number = input("number: ")
        if name not in phonebook:
            phonebook[name] = []
        phonebook[name].append(number)
        print("ok!")
    elif command == 3:
        print("quitting...")
        break
