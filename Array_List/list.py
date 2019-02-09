
print ("Declaring and accessing:\n")

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 8, 7 ]
print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:6])



print ("\n\nDeletion:\n")
list1 = ['physics', 'chemistry', 1997, 2000]
print (list1)
del list1[2]
print ("After deleting value at index 2 : ")
print (list1)


print ("\n\nRepetition:\n")
list1=["hi!"]*4
print(list1)


print ("\n\nMembership:\n")

list1 = ['physics', 'chemistry', 1997, 2000]
trueOrFalse= 1997 in list1
print(trueOrFalse)