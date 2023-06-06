# Write your solution here
def add_to_dict(dict_file_name, polish, english):
    with open(dict_file_name, "a") as new_file:
        new_file.write(f"{polish}:{english}\n")
        print("Dictionary entry added")


def search_dict(dict_file_name: str, search_term):
    with open(dict_file_name) as file:
        dictionary = {}
        search_terms = []
        for line in file:
            parts = line.strip().split("\n")
            for part in parts:
                if part.split(":")[0] not in dictionary:
                    dictionary[part.split(":")[0]] = part.split(":")[1]
        for item in dictionary.items():
            if search_term in item[0]:
                search_terms.append(f"{item[0]} - {item[1]}")
            elif search_term in item[1]:
                search_terms.append(f"{item[0]} - {item[1]}")
        for term in search_terms:
            print(term)


def main():
    dict_file_name = "dictionary.txt"
    while True:
        print("1 - Add word, 2 - Search, 3 - Quit")
        choice = int(input("Function: "))
        if choice == 1:
            finnish = input("The word in Finnish: ")
            english = input("The word in English: ")
            add_to_dict(dict_file_name, finnish, english)
        elif choice == 2:
            search_term = input("Search term: ")
            search_dict(dict_file_name, search_term)
        elif choice == 3:
            print("Bye!")
            break


main()
