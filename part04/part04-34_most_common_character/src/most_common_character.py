# Write your solution here
def most_common_character(string):
    ct = 0
    best = ""
    for character in string:
        count = str(string).count(character)
        print(count)
        print(ct)
        if count > ct:
            ct = count
            best = character
    return best
