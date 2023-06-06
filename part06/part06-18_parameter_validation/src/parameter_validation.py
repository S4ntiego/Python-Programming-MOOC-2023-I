# Write your solution here
def new_person(name: str, age: int):
    print(len(name))
    if name == "":
        raise ValueError("name is an empty string")
    elif len(name) > 40:
        raise ValueError("name is longer than 40 characters")
    elif age < 0:
        raise ValueError("age is a negative number")
    elif age > 150:
        raise ValueError("age is greater than 150")
    elif name:
        try:
            name.split(" ")[1]
        except IndexError:
            raise ValueError("name contains less than two words")

    person_tuple = (name, age)
    return person_tuple


if __name__ == "__main__":
    new_person(
        "Sirkka-Liisa Virtanen-Aftenbladet-Totterstrom-Lahtiska-Vanamo-Kullervoinen",
        97,
    )
