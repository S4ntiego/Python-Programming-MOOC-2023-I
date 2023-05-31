# Write your solution here
def same_chars(string, index_one, index_two):
    if index_one >= (len(string)) or index_one < 0:
        return False
    elif index_two >= (len(string)) or index_one < 0:
        return False
    elif string[index_one] == string[index_two]:
        return True
    else:
        return False


# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("abc", 0, 3))
