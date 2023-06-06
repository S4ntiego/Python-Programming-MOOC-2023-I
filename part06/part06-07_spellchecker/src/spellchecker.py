# write your solution here
if True:
    text = input("Write text: ")
else:
    text = "We use ptython to make a spell checker"

with open("wordlist.txt") as new_file:
    worrds = []
    for line in new_file:
        parts = line.strip().split("\n")
        for word in parts:
            worrds.append(word)
    words = text.split(" ")
    sentence = ""
    for word in words:
        if word.lower() in worrds:
            sentence += f"{word} "
        else:
            word = "*" + word + "*"
            sentence += f"{word} "
    print(sentence)
