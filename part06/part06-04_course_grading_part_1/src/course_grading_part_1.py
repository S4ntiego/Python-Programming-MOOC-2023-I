# write your solution here
students_info = input("Student information: ")
exercise_data = input("Exercises completed: ")

studs = {}

with open(students_info) as new_file:
    for line in new_file:
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        studs[parts[0]] = f"{parts[1]} {parts[2]}"

exercises = {}

with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        exercises[parts[0]] = []
        for exercise in parts[1:]:
            exercises[parts[0]].append(int(exercise))

for id, name in studs.items():
    if id in exercises:
        exercise = exercises[id]
        print(f"{name} {sum(exercise)}")
