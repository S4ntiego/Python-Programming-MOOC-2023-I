# Write your solution here
import math


def read_stations(stations_file: str):
    stations = []
    current_station = {}

    with open(stations_file) as file:
        for line in file:
            parts = line.strip().split(";")
            if parts[0] == "Longitude":
                continue
            current_station["longitude"] = float(parts[0])
            current_station["latitude"] = float(parts[1])
            current_station["fid"] = int(parts[2])
            current_station["name"] = parts[3]
            current_station["total_slot"] = int(parts[4])
            current_station["operative"] = parts[5]
            current_station["id"] = int(parts[6])
            stations.append(current_station)
            current_station = {}
        return stations


def get_station_data(filename: str):
    stations = read_stations(filename)
    found = {}
    for station in stations:
        station_tuple = (station["longitude"], station["latitude"])
        found[station["name"]] = station_tuple
    return found


def distance(station: dict, station1: str, station2: str):
    x_km = (station[station1][0] - station[station2][0]) * 55.26
    y_km = (station[station1][1] - station[station2][1]) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km


def greatest_distance(stations: dict):
    longest = 0
    stat_1 = ""
    stat_2 = ""
    for station1 in stations:
        for station2 in stations:
            dist = distance(stations, station1, station2)
            if dist > longest:
                longest = dist
                stat_1 = station1
                stat_2 = station2
    station_tuple = (stat_1, stat_2, longest)
    return station_tuple


if __name__ == "__main__":
    stations = get_station_data("stations1.csv")
    greatest_distance(stations)
