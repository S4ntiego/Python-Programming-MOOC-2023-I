def longest_series_of_neighbours(list: list):
    longest = []
    i = 0
    while i < len(list):
        inner_i = i
        streak = [list[i]]
        while inner_i + 1 <= len(list) - 1 and (
            list[inner_i] == list[inner_i + 1] + 1
            or list[inner_i] == list[inner_i + 1] - 1
        ):
            streak.append(list[inner_i + 1])
            inner_i += 1
        if len(streak) > len(longest):
            longest = streak
        i += 1
    return len(longest)


if __name__ == "__main__":
    longest_series_of_neighbours([1, 2, 3, 0, 1, 2, 3, 4, 5, 3, 4, 5, 1, 2, 3])
