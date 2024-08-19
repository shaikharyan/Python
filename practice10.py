#1.Convert the following dictionary into json Format
import json
Student_data={"name":"David","age":13,"marks":87}
print(type(Student_data)) #<class 'dict'>
data=json.dumps(Student_data)
print(data) #{"name": "David", "age": 13, "marks": 87}
print(type(data)) #<class 'str'>


#Access the value of age from the given data
Student_data="""{"name":"David","age":13,"marks":87}"""
data=json.loads(Student_data)
print(data["age"]) #13

#pretty print following Json data
Student_data={"name":"David","age":13,"marks":87}
data=json.dumps(Student_data,indent=4,separators=(",","="))
print(data)

#O/P:
#{
#    "name"="David",
#    "age"=13,
#    "marks"=87
#}

#sort the following Json Keys and write them into a file
Student_data={"name":"David","age":13,"marks":87}
f=open("demo.json","w")
data=json.dumps(Student_data,indent=4,sort_keys=True)
f.write(data)

print("the data is added in the file")


#Access the nested key marks from the following nested data
student_data="""{"student":
                {"grade":
                {"name":"David","age":13,"marks":87}
                }
            }"""
data=json.loads(student_data)
print(data["student"]["grade"]["marks"])  #87