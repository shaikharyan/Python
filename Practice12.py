#Sets
#write a program to find Max & Min in a set
x={12,56,34,8,90,1,57}
maximum=max(x)
minimum=min(x)
print("The minumum value is : ",maximum) #90
print("The maximum value is: ",minimum) #1

#write a program to find common element in three lists using sets.
a=[1,5,6,8,2]
b=[4,5,6,7]
c=[1,9,6,2,5]
#convert list into set and print
print(set(a)& set(b)& set(c))  #{5, 6}

#write a program to find difference between two sets.
a={1,5,6,8,2}
b={4,5,6,7}
print(a.difference(b))  #{8, 1, 2}

#write a program to remove an item from a set if it is present in the set.
a={1,5,6,8,2}
a.discard(8)
print(a) #{1, 2, 5, 6}

#write a program to check if a set is a subset of another set.
a={1,2,3,4,5,6}
b={2,3,4}
print(a.issubset(b)) #false
print(b.issubset(a)) #true

