def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = list(map(int, input("Enter elements: ").split()))
key = int(input("Enter the element to search: "))

arr.sort()

print(f"Sorted array: {arr}")

result = binary_search(arr, key)
if result != -1:
    print(f"Element {key} found at index {result}")
else:
    print(f"Element {key} not found in the array")