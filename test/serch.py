
search = int(input("Enter the number to be searched: "))


list1 = list(map(int, input("Enter the list elements: ").strip().split()))

flag = 0


for i in range(len(list1)):
    if list1[i] == search:
        print("Element found at index:", i)
        flag = 1
        break


if flag == 0:
    print("Element not found")
