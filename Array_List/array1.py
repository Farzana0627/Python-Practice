from array import *


print("Insertion")
array1 = array('i', [10,20,30,40,50])
array1.insert(2,60)

for x in array1:
print(x)


print("Deletion")
array1 = array('i', [10,20,30,40,50])
array1.remove(40)

for x in array1:
print(x)


print("Search")
array1 = array('i', [10,20,30,40,50])

print (array1.index(40))


print("Update")
array1 = array('i', [10,20,30,40,50])

array1[2] = 80

for x in array1:
print(x)