# Write your solution here


def line(number, string):
    if len(string) > 0:
        print(number * str(string[0]))
    else:
        print(number * "*")


# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")
