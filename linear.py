n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)
target = int(input("Enter element to search: "))
found = False
for i in range(n):
    if arr[i] == target:
        print("Element found at index", i)
        found = True
        break
if not found:
    print("Element not found")
