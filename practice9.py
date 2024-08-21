#Lists Problems

a=["Ross","Rachel","Monica","Joe"]

#1.Write a program to swap first and fourth element
a[0],a[3]=a[3],a[0]
print(a) #['Joe', 'Rachel', 'Monica', 'Ross']

#2.Write a program to add a new value at second position
a.insert(1,"Phoebe")
print(a) #['Joe', 'Phoebe', 'Rachel', 'Monica', 'Ross']

#3.Write a program to delete value from 3rd position
a.pop(2)
print(a) #['Joe', 'Phoebe', 'Monica', 'Ross']

b=[13,7,12,10]
#1.write a program to multiply all the numbers in the list.
mul=1
for i in b:
    mul*=i
print(mul)  #10920

#2.write a program to get the largest number from the list.
b.sort()
print(b)
print("The largest element is: ",b[-1])  #The largest element is:  13

#3.write a program to get the smallest number from the list.
b.sort()
print(b)
print("The smallest element is: ",b[0])  #The smallest element is:  7