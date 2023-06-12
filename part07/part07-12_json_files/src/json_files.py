# Write your solution here
import json


def print_persons(filename: str):
    with open(filename) as json_file:
        data = json_file.read()

        people = json.loads(data)
        for person in people:
            hobbies = ", ".join(person["hobbies"])
            print(f"{person['name']} {person['age']} years ({hobbies})")


if __name__ == "__main__":
    print_persons("file1.json")
