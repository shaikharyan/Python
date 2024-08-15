#write a program to swap two variable
#method1
x=12
y=13

temp=x
x=y
y=temp

print(x)  #13
print(y)  #12

#method2
a=30
b=20
#swap
a,b=b,a
print(a) #20
print(b) #30


#write a program to convert a float into int

a=1.12

a=int(a)
print(a) #1
print(type(a)) #int

#take details from student ID
name=input("Enter name: ")
age=int(input("Enter age: "))
height=float(input("Enter height: "))
print(name)
print(age)
print(height)

#take an input as int and convert into float
a=int(input("Enter integer: "))
print(a) #2
print(type(a))

a=float(a)
print(a) #2.0
print(type(a))