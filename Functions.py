def add():
    x=56
    y=23
    print(x+y)
add()  #79

def add(x,y):
    print(x+y)
add(2,3)  #5


#arbitory function
def hello(*name):
    print("hello,my name is",name[1])

hello("John","lisa","peter")  #hello,my name is lisa