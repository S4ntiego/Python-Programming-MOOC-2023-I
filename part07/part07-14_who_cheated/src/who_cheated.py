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
