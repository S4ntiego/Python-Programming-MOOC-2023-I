# Write your solution here
with open("diary.txt", "a") as new_file:
    while True:
        print("1 - add an entry, 2 - read entries, 0 - quit")
        function_input = int(input("Function: "))
        if function_input == 1:
            diary_input = input("Diary entry: ")
            new_file.write(f"{diary_input}\n")
            print("Diary saved")
            continue
        elif function_input == 2:
            print("Entries:")
            with open("diary.txt") as file:
                for line in file:
                    print(line)
            continue
        else:
            print("Bye now!")
            break
