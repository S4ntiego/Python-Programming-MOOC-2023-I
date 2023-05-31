# Copy here code of line function from previous exercise and use it in your solution
# You can test your function by calling it within the following block
def shape(width, shape, height, filler):
    i = 1
    while i <= width:

        def line(number, string):
            if len(string) > 0:
                print(number * str(string[0]))
            else:
                print(number * "*")

        line(i, shape)
        i += 1
    i = 1
    while i <= height:
        line(width, filler)
        i += 1


if __name__ == "__main__":
    shape(5, "x", 4, "+")
