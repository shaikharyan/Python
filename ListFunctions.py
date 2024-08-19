a=["Thor","Hulk","Ironman","Captain America","Hulk"]
print(a)

#to find the length of list
print(len(a))  #5

#to count an occurrence of a particular element
print(a.count("Hulk"))  #2

#to add to the list
a.append("Spiderman")   #add in last
print(a)  #['Thor', 'Hulk', 'Ironman', 'Captain America', 'Hulk', 'Spiderman']

#to add to a specific location
a.insert(1,"Vision")
print(a)  #['Thor', 'Vision', 'Hulk', 'Ironman', 'Captain America', 'Hulk', 'Spiderman']

#to remove from the list
a.remove("Hulk")  #remove first occur value
print(a)  #['Thor', 'Vision', 'Ironman', 'Captain America', 'Hulk', 'Spiderman']

#to remove from certain location
print(a.pop(1))
print(a)   #['Thor', 'Ironman', 'Captain America', 'Hulk', 'Spiderman']

#to create a copy of a list
b=a.copy()
print(b)

#to access an element
print(a.index("Ironman"))  #1

#to extend the list
c=["Superman","Batman"]
a.extend(c)
print(a)  #['Thor', 'Ironman', 'Captain America', 'Hulk', 'Spiderman', 'Superman', 'Batman']

#to reverse the list
a.reverse()
print(a)  #['Batman', 'Superman', 'Spiderman', 'Hulk', 'Captain America', 'Ironman', 'Thor']

#to sort the list
a.sort()
print(a)  #['Batman', 'Captain America', 'Hulk', 'Ironman', 'Spiderman', 'Superman', 'Thor']

#to clear all the data
a.clear()
print(a)  #[]