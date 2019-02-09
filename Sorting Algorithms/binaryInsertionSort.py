def binary_search(arr, val, start, end):
	# we need to distinugish whether we should insert 
    # before or after the left boundary.
	if start==end:
		if arr[start] > val:
			return start
		else:
			return start+1
    # this occurs if we are moving beyond left\'s boundary 
    # meaning the left boundary is the least position to 
    # find a number greater than val 
	if(start>end):
		return start

	mid=(start+end)//2
	if arr[mid]<val:
		return binary_search(arr,val, mid+1, end)
	elif arr[mid]>val:
		return binary_search(arr, val, start, mid-1)
	else:
		return mid

def binary_insertion_sort(arr):
	for x in range (1,len(arr)):
		val= arr[x]
		pos=binary_search(arr, val,0,x-1)
		arr=arr[:pos]+[val]+arr[pos:x]+arr[x+1:] 
		#position x has been compromised. in the position x, the present value exists that has been put in the 'pos' position. so 'arr[pos:x]+arr[x+1:]'
	return arr


# arr=[37,23,0,17,12,72,31,46,100,86,44]
# print(binary_insertion_sort(arr))

