# Write your solution here
from datetime import datetime, timedelta


def into_minutes(screen_time_input: str):
    parts = screen_time_input.strip().split(" ")
    int_parts = []
    for time_str in parts:
        int_parts.append(int(time_str.strip()))
    return int_parts


file_to_save = {}
days_to_save = {}
filename = input("Filename: ")
starting_date_input = input("Starting date: ")
starting_date = datetime.strptime(starting_date_input, "%d.%m.%Y")
how_many_days = int(input("How many days: "))
first_day = datetime.strftime(starting_date, "%d.%m.%Y")
last_day = datetime.strftime(
    starting_date + timedelta(days=how_many_days - 1), "%d.%m.%Y"
)
file_to_save["Time period"] = f"{first_day}-{last_day}"
total_time = 0
print("Please type in screen time in minutes on each day (TV computer mobile):")
for i in range(how_many_days):
    converted_date = datetime.strftime(starting_date + timedelta(days=i), "%d.%m.%Y")
    screen_time = input(f"Screen time {converted_date}: ")
    days_to_save[
        converted_date
    ] = f"{into_minutes(screen_time)[0]}/{into_minutes(screen_time)[1]}/{into_minutes(screen_time)[2]}"

    total_time += sum(into_minutes(screen_time))
file_to_save["Total minutes"] = str(total_time)
file_to_save["Average minutes"] = str(total_time / how_many_days)
with open(filename, "w") as new_file:
    for item in file_to_save.items():
        new_file.write(f"{item[0]}: {item[1]}\n")
    for item in days_to_save.items():
        new_file.write(f"{item[0]}: {item[1]}\n")
