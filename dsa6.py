arr = [5, 2, 8, 1, 9]
key = int(input("Enter the element to search: "))

found = False

for i in range(len(arr)):
    if arr[i] == key:
        print(f"Element {key} found at index {i}")
        found = True
        break

if not found:
    print(f"Element {key} not found in the array")