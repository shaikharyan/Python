fruits=["apple","mango","banana",12,4.23]
print(fruits)
print(type(fruits))

#slicing List
a=["Ironman","Thor","Captain America","Hulk"]
print(a[2])  #Captain America
print(a[-3]) #Thor
print(a[1]) #Thor
print(a[1:3]) #['Thor', 'Captain America']
print(a[:2]) #['Ironman', 'Thor']
print(a[1:]) #['Thor', 'Captain America', 'Hulk']
print(a[::2]) #['Ironman', 'Captain America']
print(a[-3:-1]) #['Thor', 'Captain America']
print(a[::-1]) #['Hulk', 'Captain America', 'Thor', 'Ironman']
print(a[-1:-4:-1]) #['Hulk', 'Captain America', 'Thor']


#List Iteration using For Loop
for i in a:
    print(i)

#O/P:
#Ironman
#Thor
#Captain America
#Hulk

#iteration using for loop with range and length function
for i in range(len(a)):
    print(a[i])

#O/P:
#Ironman
#Thor
#Captain America
#Hulk


#List Iteration using while Loop
i=0
while i<(len(a)):
    print(a[i])
    i+=1

#O/P:
#Ironman
#Thor
#Captain America
#Hulk

#using Short-hand For Loop
[print(i) for i in a]

#O/P:
#Ironman
#Thor
#Captain America
#Hulk