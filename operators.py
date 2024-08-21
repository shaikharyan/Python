#Arithmetic operator

print(2+3)
print(3-2)
print(2*3)
print(5/2)
print(5**2)
print(8//3)
print(5%2)

#comparison operator
print("Comparison operator")
print(3>2)  #True
print(3<2) #false
print(3==2) #false
print(3!=2) #True
print(3<=2) #false
print(3>=2) #True

#Logical operator
print("logical operator")
print(3==3 and 2==2) #True
print(3>2 or 3<2) #false
print(3!=3) #false
print(not(3==3)) #false

print("Assignment operator")
x=4
print(x)
x+=2
print(x)
x-=2
print(x)
x*=2
print(x)

print("Identity operator")
a=123
b=123
c="123"

print(a is b)  #True
print(a is not c) #True

print("Bitwise operator")
a=10
b=8
print(a&b) #0
print(a|b) #14
print(a^b)  #14
print(a>>1) #5
print(b<<1) #8

print("Membership operator")
a="hello"
print("p" in a) #false
print("e" in a) #true
print("e" not in a) #false


