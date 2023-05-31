# Copy here code of line function from previous exercise


def triangle(size):
    i = 1
    while i <= size:

        def line(number, string):
            if len(string) > 0:
                print(number * str(string[0]))
            else:
                print(number * "*")

        line(i, "#")
        i += 1
    # You should call function line here with proper parameters


# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
