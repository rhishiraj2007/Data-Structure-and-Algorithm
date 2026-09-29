def main():
    print("roll no: CSE25147\nname: Rhishiraj Thalakkat\n")
    n = int(input("Enter the size of the array: "))
    arr = []
    for _ in range(n):
        arr.append(int(input("Enter an element: ")))
    sorted_arr = merge_sort(arr)
    print("Sorted array:", sorted_arr)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1

    arr.extend(left[i:])
    arr.extend(right[j:])
    return arr

if __name__ == "__main__":
    main()