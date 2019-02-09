def insertionSort(list):
	for i in range(1, len(list)):
		j=i
		while(j>0 and list[j-1]>list[j]):
			temp= list[j]
			list[j]= list[j-1]
			list[j-1]= temp
			j=j-1
		i+=1
	return list

list = [19,2,2,45,6,11,121,0]
print(insertionSort(list))