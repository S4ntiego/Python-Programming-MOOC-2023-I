# Write your solution here
layers = int(input("Layers: "))
letters = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
lay = []
i = 1
for j in range(len(letters)):
    lay.append(i)
    i += 2
if layers != 1:
    pepega = letters[layers] * lay[layers]
    j = 1
    while j <= layers:
        if j > 1:
            k = 1
            while k <= (j - 1):
                print(f"{letters[layers-k]}", end="")
                k += 1
        print(f"{letters[layers - j] * lay[layers - j]}", end="")
        if j > 1:
            k = j - 1
            while k >= 1:
                print(f"{letters[layers-k]}", end="")
                k -= 1
        print()
        j += 1

for j in range(layers - 1, 0, -1):
    if j > 1:
        k = 1
        while k <= (j - 1):
            print(f"{letters[layers-k]}", end="")
            k += 1
    print(f"{letters[layers - j] * lay[layers - j]}", end="")
    if j > 1:
        k = j - 1
        while k >= 1:
            print(f"{letters[layers-k]}", end="")
            k -= 1
    print()
