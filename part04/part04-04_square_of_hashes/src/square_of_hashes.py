# Copy here code of line function from previous exercise


def square_of_hashes(size):
    i = 0
    # You should call function line here with proper parameters
    while i < size:

        def line(number, string):
            if len(string) > 0:
                print(number * str(string[0]))
            else:
                print(number * "*")

        line(size, "#")
        i += 1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
