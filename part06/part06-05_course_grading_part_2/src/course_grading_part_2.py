# write your solution here
if True:
    students_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exams completed: ")
# else:
#     # now this is the False branch, and is never executed
#     students_info = "students1.csv"
#     exercise_data = "exercises1.csv"
#     exam_data = "exam_points1.csv"

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

exams = {}

with open(exam_data) as new_file:
    for line in new_file:
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        exams[parts[0]] = []
        for exam_grade in parts[1:]:
            exams[parts[0]].append(int(exam_grade))


for id, name in studs.items():
    if id in exercises:
        exercise = exercises[id]
        if sum(exercise) < 10:
            exercise = 0
        else:
            exercise = sum(exercise) // 4

    if id in exams:
        exam = exams[id]

    grade = 0

    if (exercise + sum(exam)) <= 14:
        grade = 0
    elif (exercise + sum(exam)) <= 17:
        grade = 1
    elif (exercise + sum(exam)) <= 20:
        grade = 2
    elif (exercise + sum(exam)) <= 23:
        grade = 3
    elif (exercise + sum(exam)) <= 27:
        grade = 4
    elif (exercise + sum(exam)) >= 28:
        grade = 5

    print(f"{name} {grade}")
