# Write your solution here
import csv
from datetime import datetime, timedelta


def get_data():
    s_times = {}

    with open("start_times.csv") as start_times:
        for line in csv.reader(start_times, delimiter=";"):
            student = line[0]
            start_time = datetime.strptime(line[1], "%H:%M")
            s_times[student] = {
                "start_time": start_time,
                "stats": {"tasks": [], "points": [], "submissions": []},
            }

    with open("submissions.csv") as submission_times:
        for line in csv.reader(submission_times, delimiter=";"):
            student = line[0]
            task_no = line[1]
            points = line[2]
            submission_time = datetime.strptime(line[3], "%H:%M")
            s_times[student]["stats"]["tasks"].append(task_no)
            s_times[student]["stats"]["points"].append(points)
            s_times[student]["stats"]["submissions"].append(submission_time)

    return s_times


def cheaters():
    data = get_data()
    cheaters = []
    for student in data:
        for hour in data[student]["stats"]["submissions"]:
            if data[student]["start_time"] + timedelta(hours=3) < hour:
                cheaters.append(student)
                break
    return cheaters


def final_points():
    data = get_data()
    final_points = {}
    for student, stats in data.items():
        student_tasks = {}
        start_time = stats["start_time"]
        tasks = stats["stats"]["tasks"]
        points = stats["stats"]["points"]
        submissions = stats["stats"]["submissions"]
        for index, task in enumerate(tasks):
            submission_time = submissions[index]
            point = points[index]
            if submission_time <= start_time + timedelta(hours=3):
                if task not in student_tasks:
                    student_tasks[task] = int(point)
                elif int(point) > student_tasks[task]:
                    student_tasks[task] = int(point)
        final_points[student] = sum(student_tasks.values())
    return final_points


if __name__ == "__main__":
    final_points()

# If there are multiple submissions for the same task, the submission with the highest number of points is taken into account.
# If the submission was made over 3 hours after the start time, the submission is ignored.
# The tasks are numbered 1 to 8, and each submission is graded with 0 to 6 points.

# In the dicionary returned the key should be the name of the student, and the value the total points received by the student.
