# Write your solution here
def anagrams(s1, s2):
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False


if __name__ == "__main__":
    anagrams("pepega", "agepep")
