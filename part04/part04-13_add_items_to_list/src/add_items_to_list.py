# Write your solution here
items = int(input("How many items: "))
values = []
i = 1
while i <= items:
    item = int(input(f"Item {i}: "))
    values.append(item)
    i += 1
print(values)
