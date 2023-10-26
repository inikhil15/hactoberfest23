def insertionSort(arr): 
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key

lst=[]
print("Enter no. of Elements : ")
n=int(input())
for i in range (0,n):
    print("Enter value no. ",i+1)
    lst.append(int(input()))
print("Unsorted List")
print(lst)
insertionSort(lst)
print("Sorted List")
print(lst)
