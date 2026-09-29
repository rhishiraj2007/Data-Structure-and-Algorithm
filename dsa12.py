def main():
    print("roll no: CSE25147\nname: Rhishiraj Thalakkat\n")
    n = int(input("Enter the size of the array: "))
    arr = []
    for _ in range(n):
        arr.append(int(input("Enter an element: ")))
    quick_sort(arr, 0, n - 1)
    print("Sorted array:", arr)

def quick_sort(a, low, high):
    if low < high:
        pivot = a[low]
        i = low - 1
        j = high + 1

        while True:
            i += 1
            while a[i] < pivot:
                i += 1
            j -= 1
            while a[j] > pivot:
                j -= 1
            if i >= j:
                break
            a[i], a[j] = a[j], a[i]

        quick_sort(a, low, j)
        quick_sort(a, j + 1, high)

if __name__ == "__main__":
    main()