# Write your solution here
def oldest_person(people: list):
    return sorted(people, key=lambda tup: tup[1])[0][0]
