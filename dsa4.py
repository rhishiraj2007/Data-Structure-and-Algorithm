def search_employee(ids, key, index = 0 ):
    if index >= len(ids):
        return -1
    if ids[index] == key:
        return index
    return search_employee(ids, key, index + 1)

ids = [101, 102, 103, 104, 105]

key = int(input("Enter the employee ID to search: "))

if search_employee(ids, key) != -1:
    print("Employee ID found")
else:
    print("Employee ID not found")
