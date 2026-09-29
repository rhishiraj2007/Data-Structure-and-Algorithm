arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

n = len(arr)

for i in range(n):
    main_index = i

    for j in range(i + 1, n):
        if arr[j] < arr[main_index]:
            main_index = j

    arr[i], arr[main_index] = arr[main_index], arr[i]
print("Sorted list:", arr)