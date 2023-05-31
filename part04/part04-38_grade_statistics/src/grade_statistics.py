# Write your solution here
def exercise_points(exercises):
    i = 10
    if exercises < 10:
        return 0
    if exercises == 100:
        return 10
    while i <= 100:
        if exercises >= i and exercises < i + 10:
            return i / 10
        i += 10


def points_exercises():
    points = []
    success = []
    grades = []
    while True:
        user_input = input("Exam points and exercises completed: ")
        if user_input == "":
            break
        exam = int(user_input.split(" ")[0])
        exercises_input = int(user_input.split(" ")[1])
        exercises = exercise_points(exercises_input)
        mark = grade(exam, exercises)
        points.append(exam + exercises)
        grades.append(mark)
        if (exam) < 10:
            success.append(0)
        elif (exam + exercises) <= 14:
            success.append(0)
        else:
            success.append(1)
    return points, success, grades


def grade(exam, exercise):
    if exam < 10:
        return 0
    elif (exam + exercise) <= 14:
        return 0
    elif (exam + exercise) <= 17:
        return 1
    elif (exam + exercise) <= 20:
        return 2
    elif (exam + exercise) <= 23:
        return 3
    elif (exam + exercise) <= 27:
        return 4
    elif (exam + exercise) <= 30:
        return 5


def average(list):
    avg = sum(list) / len(list)
    return avg


# main function
def main():
    pt = points_exercises()
    points = pt[0]
    success = pt[1]
    grades = pt[2]

    avg = round(average(points), 1)
    pass_percentage = round((average(success) * 100), 1)

    i = 0
    ct = []
    string_variable = "*"
    while i <= 5:
        times = grades.count(i)
        ct.append(times)
        i += 1

    print("Statistics: ")
    print(f"Points average: {avg}")
    print(f"Pass percentage: {pass_percentage}")
    print("Grade distribution: ")
    for index, item in reversed(list(enumerate(ct))):
        print(f"  {index}: {item * string_variable}")


# run the main function
# main()
main()
