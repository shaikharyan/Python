#it is used when an anonymous function is required for a short period of time.
#it take numerous arguments.
#it can only have one expression.

a=lambda b:b*5
print(a(4)) #20

x=lambda a,b,c:(a+b)*c
print(x(3,7,3))  #30