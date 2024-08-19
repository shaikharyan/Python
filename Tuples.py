#a=("apple","mango","banana",1,2)
a="apple","mango","banana",1,2
print(a) #('apple', 'mango', 'banana', 1, 2)
print(type(a)) #<class 'tuple'>

b=("ironman",)
print(type(b)) #<class 'tuple'>

#Slicing Tuples
x=("Oneplus","Vivo","Redmi","SumSung","Nokia")
print(x[1:3]) #('Vivo', 'Redmi')
print(x[:3]) #('Oneplus', 'Vivo', 'Redmi')
print(x[2:]) #('Redmi', 'SumSung', 'Nokia')
print(x[::2]) #('Oneplus', 'Redmi', 'Nokia')
print(x[1::2]) #('Vivo', 'SumSung')
print(x[::-1]) #('Nokia', 'SumSung', 'Redmi', 'Vivo', 'Oneplus')
print(x[2::-1])  #('Redmi', 'Vivo', 'Oneplus')

#iteration using for loop
for i in x:
    print(i)

#along with range and length in for loop
for i in range(len(x)):
    print(x[i])

#while loop
i=0
while i<len(x):
    print(x[i])
    i+=1