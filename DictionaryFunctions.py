Student={"name":"john","age":24,"gender":"Male"}

#get
x=Student.get("name")
print(x) #john

#item
a=Student.items()
print(a) #dict_items([('name', 'john'), ('age', 24), ('gender', 'Male')])

#keys
b=Student.keys()
print(b) #dict_keys(['name', 'age', 'gender'])

#values
c=Student.values()
print(c) #dict_values(['john', 24, 'Male'])

#copy
y=Student.copy()
print(y) #{'name': 'john', 'age': 24, 'gender': 'Male'}

#setDefault
z=Student.setdefault("name","Aryan")
print(z)

#update

#pop

#popitem

#clear