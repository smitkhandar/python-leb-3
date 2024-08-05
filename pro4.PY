
elements = [1, 3, 5, 8, 10, 23, 35]

target = 10


found = False
for i in range(len(elements)):
    if elements[i] == target:
        print(f"Element {target} found at index {i}.")
        found = True
        break

if not found:
    print(f"Element {target} not found in the list.")
