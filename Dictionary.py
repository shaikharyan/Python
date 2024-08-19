Employee_Data={"name":"john","age":24,"gender":"Male"}
print(Employee_Data) #{'name': 'john', 'age': 24, 'gender': 'Male'}
print(type(Employee_Data)) #<class 'dict'>
print(Employee_Data["gender"])  #Male


#Iteration in Dictionary
#print keys
for i in Employee_Data:
    print(i)

#name
#age
#gender

#print values
for i in Employee_Data:
    print(Employee_Data[i])

#john
#24
#Male


#using value function
for i in Employee_Data.values():
    print(i)
    
#john
#24
#Male

#using items function
for i in Employee_Data.items():
    print(i)

#('name', 'john')
#('age', 24)
#('gender', 'Male')
