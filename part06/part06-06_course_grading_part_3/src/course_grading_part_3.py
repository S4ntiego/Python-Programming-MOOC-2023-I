# write your solution here
if True:
    students_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exams completed: ")
else:
    # now this is the False branch, and is never executed
    students_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_data = "exam_points1.csv"

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

print(
    f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}"
)
for id, name in studs.items():
    if id in exercises:
        exercise = exercises[id]
        exec_pts = exercises[id]
        if sum(exercise) < 10:
            exec_pts = 0
        else:
            exec_pts = sum(exercise) // 4

    if id in exams:
        exam = exams[id]

    grade = 0

    if (exec_pts + sum(exam)) <= 14:
        grade = 0
    elif (exec_pts + sum(exam)) <= 17:
        grade = 1
    elif (exec_pts + sum(exam)) <= 20:
        grade = 2
    elif (exec_pts + sum(exam)) <= 23:
        grade = 3
    elif (exec_pts + sum(exam)) <= 27:
        grade = 4
    elif (exec_pts + sum(exam)) >= 28:
        grade = 5

    print(
        f"{name:30}{sum(exercise):<10}{exec_pts:<10}{sum(exam):<10}{exec_pts + sum(exam):<10}{grade:<10}"
    )
