# Write your solution here
def older_people(people: list, year: int):
    older = []
    for person in people:
        if person[1] < year:
            older.append(person[0])
    return older
