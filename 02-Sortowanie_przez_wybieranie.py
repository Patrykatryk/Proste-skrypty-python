def findSmallest(arr):
    global smallest_index
    smallest_index=0
    samllest=arr[0]
    for i in range(0, len(arr)):
        if arr[i]< samllest:
            smallest = arr[i]
            smallest_index=i
    return smallest_index

# arr1=[-3,5,3,6,2,1,10,-2,-8]
# print(findSmallest(arr1))

def selectionSort(arr):
    newArr=[]
    for i in range (0,len(arr)):
        samllest = findSmallest(arr)
        newArr.append(arr.pop(samllest))
        print(newArr)
    return newArr
arr1=[5,3,6,2,1,10,-3,20,-19]
print(selectionSort(arr1))