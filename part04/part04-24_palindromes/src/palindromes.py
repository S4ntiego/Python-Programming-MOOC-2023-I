# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
def palindromes(string):
    i = 0
    while string[i] == string[-i - 1]:
        i += 1
        if i > len(string) / 2:
            return True
    return False


def siema():
    while True:
        word = input("Please type in a palindrome: ")
        if palindromes(word):
            print(f"{word} is a palindrome!")
            break
        print("that wasn't a palindrome")


siema()
