def buble(list):
    n=len(list)
    while n>1:
        zamien=False
        for i in range(0,n-1):
            if list[i]>list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]
                zamien= True

        n -=1
        print(list)
        if zamien==False:
            break
    return list
print(buble([10,11,8,5,0]))