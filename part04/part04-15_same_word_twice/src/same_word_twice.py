# Write your solution here
word = ""
array = []
while True:
    word = input("Word: ")
    if word in array:
        break
    array.append(word)
    continue
print(f"You typed in {len(array)} different words")
