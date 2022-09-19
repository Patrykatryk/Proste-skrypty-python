def binary_search(list, item):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = (low + high)
        guess = list[mid]
        if guess == item:
            return mid
        if guess >item:
            high = mid - 1
        else:
            low = mid + 1
            return None


my_list = [1,3,5,7,9,11,13,15]
your_list= [1,2,3,4,5]

print(binary_search(my_list,3))
print(binary_search(your_list,3))







###################################### POWTÓRKA #############################################





def binarane(list,item):
    len=len(list)