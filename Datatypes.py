name=input("Enter name here")
print(name)

age=int(input("Enter age here"))
print(age)

length=float(input("Enter rectange:"))
print(length)

exp1=eval(input("Enter equation here:"))
print(exp1)


#typecasting
a=123
b=1.23
print(type(a))
print(type(b))

c=a+b
print(c)  #124.23
#implicit type conversion
print(type(c))

a="123"
b=1.23
print(type(a))
print(type(b))

#explicit type convertion
a=int(a)
print("type a after convertion",type(a))

c=a+b
print(c)  #124.23
#explicit type conversion
print(type(c))

