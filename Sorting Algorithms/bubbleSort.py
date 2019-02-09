def bubblesort(list):

# Swap the elements to arrange in order
    for iter_num in range(0,len(list)-1):
        for idx in range(0,len(list)-1):
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp


list = [19,2,31,45,6,11,121,27]
bubblesort(list)
print(list)