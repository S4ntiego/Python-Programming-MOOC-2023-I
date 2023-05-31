# Copy here code of line function from previous exercise


def box_of_hashes(height):
    # You should call function line here with proper parameters
    def line(number, string):
        if len(string) > 0:
            print(number * str(string[0]))
        else:
            print(number * "*")

    i = 0

    while i < height:
        line(10, "#")
        i += 1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
