def hello():
    return "Hello World"

print(hello())  #Hello World

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

print(fact(5)) #120