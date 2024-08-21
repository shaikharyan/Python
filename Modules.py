#modules are the .py files that contain set of functions you want to include in your program.

#in-built modules
#datetime
import datetime
from math import floor

x=datetime.datetime.now()
print(x)  #2024-08-21 20:07:29.963587

print(x.strftime("%A"))  #Wednesday
print(x.strftime("%B")) #August
print(x.strftime("%m")) #08
print(x.strftime("%Y")) #2024
print(x.strftime("%y")) #24

#Random
import random

a=random.randint(1,10)
print(a)   #6
print(a)   #3

l=["Heads","Tails"]
b=random.choice(l)
print(b)  #Heads


#Math
import math
y=max(13,67,45)
print(y) #67

y=min(13,4,22)
print(y) #4

y=pow(2,4)
print(y) #16

y=math.sqrt(49)
print(y) #7

y=abs(-12)
print(y) #12

y=math.floor(2.4)
print(y) #2

y=math.ceil(2.4)
print(y) #3

