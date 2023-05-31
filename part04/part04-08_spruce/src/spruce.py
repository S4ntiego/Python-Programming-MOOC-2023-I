# Write your solution here
def spruce(height):
    i = 0
    width = 1
    tree = height - 1
    print("a spruce!")
    while i < height:
        print(" " * tree + "*" * width)
        i += 1
        width += 2
        tree -= 1
    print(" " * (height - 1) + "*")


# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)
