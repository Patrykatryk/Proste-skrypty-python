def quicksort(array):
    if len(array)<2:
        return array
    else:
        pivot=array[0]
        less=[i for i in array[1:] if i<= pivot]
        print(" ", less)
        greater = [i for i in array[1:] if i > pivot]
        print(greater)
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([4,5,2,6,3,7]))