a={"Ironman","Hulk","Thor","Captain America"}
print(a)  #Always change position of values
#{'Ironman', 'Hulk', 'Captain America', 'Thor'}
print(type(a))

#iteration
for i in a:
    print(i)

#sets functions
#add
a.add("Spiderman")  #add anywhere in set
print(a) #{'Thor', 'Ironman', 'Spiderman', 'Captain America', 'Hulk'}

#pop
a.pop() #randomly pop one value
print(a) #{'Ironman', 'Spiderman', 'Captain America', 'Hulk'}

#remove
a.remove("Hulk")  #remove only one value
print(a) # {'Ironman', 'Spiderman', 'Captain America'}

#discard
a.discard("Thor")  #same as remove no difference
print(a) #{'Ironman', 'Spiderman', 'Captain America'}

#copy
b=a.copy()
print(b)  #{'Ironman', 'Spiderman', 'Captain America'}


x={"Ironman","Hulk","Thor","Captain America"}
y={"Superman","Batman","Wonder"}
z={"Hulk","Thor"}

#isdisjoint
print(x.isdisjoint(y))  #True->No elements are same in x
print(x.isdisjoint(z))  #False->Elements are match with x

#issubset
print(x.issubset(y))  #false
print(z.issubset(x))  #true

#issuperset
print(x.issuperset(y))  #false
print(x.issuperset(z))  #true

#update->add z set in x
x.update(z)
print(x)  #{'Ironman', 'Thor', 'Captain America', 'Hulk'}

#clear->empty set values
#x.clear()
#print(x)  #set()


#union
print(x.union(z))

#difference->Return only X value that are not in Z
print(x.difference(z)) #{'Hulk', 'Captain America', 'Spiderman', 'Ironman', 'Thor'}

#difference update
x.difference_update(z)
print(x) #{'Captain America', 'Spiderman', 'Ironman', 'Thor'}

#intersection->common elements
print(x.intersection(z))

#intersection update
x.intersection_update(z)
print(x)

#symmetric difference->Ignore common elements
c=x.symmetric_difference(z)
print(c) #{'Hulk', 'Thor'}







