# Write your solution here
def add_student(students: list, name: str):
    students[name] = {"name": {name}, "courses": []}


def add_course(students: dict, name: str, completion: tuple):
    for tuple in students[name]["courses"]:
        if completion[0] == tuple[0]:
            if completion[1] <= tuple[1]:
                return
            else:
                students[name]["courses"].clear()
    if completion[1] == 0:
        return
    else:
        students[name]["courses"].append(completion)


def print_student(students: list, name):
    if name not in students:
        print(f"{name}: no such person in the database")
    elif name in students:
        if students[name]["courses"] == []:
            print(f"{name}: ")
            print(f" no completed courses")
        else:
            length = len(students[name]["courses"])
            print(f"{name}: ")
            print(f" {length} completed courses: ")
            avg = []
            for course in students[name]["courses"]:
                avg.append(course[1])
                print(f"  {course[0]} {course[1]}")
            print(f" average grade {sum(avg)/len(avg)}")


def summary(students):
    print(f"students {len(students)}")
    most = ["", 0]
    for student in students:
        if len(students[student]["courses"]) > most[1]:
            most = [student, len(students[student]["courses"])]
    print(f"most courses completed {most[1]} {most[0]}")
    best_avg_grade = ["", 0]
    for student in students:
        grades = []
        for course in students[student]["courses"]:
            grades.append(course[1])
        if sum(grades) / len(grades) > best_avg_grade[1]:
            best_avg_grade = [student, (sum(grades) / len(grades))]
    print(f"best average grade {best_avg_grade[1]} {best_avg_grade[0]}")
