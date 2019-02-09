#Accesing

print("\nAccessing:\n")
T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
for r in T:
    for c in r:
        print(c,end = " ")
    print()


#Insertion
print("\nInsertion at index 2:\n")
T.insert(2, [0,5,11,13,6])

for r in T:
    for c in r:
        print(c,end = " ")
    print()



#Update
print("\nUpdate at index 2 and (0,3):\n")
T[2] = [11,9]
T[0][3] = 7
for r in T:
    for c in r:
        print(c,end = " ")
    print()


#Deletion
print("\nDeletion from index 3:\n")
del T[3]

for r in T:
    for c in r:
        print(c,end = " ")
    print()