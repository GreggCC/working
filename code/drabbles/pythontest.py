print("hello World!")
print("I'm Gregg")
print(2+3)
def addTwoNumbs(x,y):
    return x+y
print(addTwoNumbs(2,3))
print(addTwoNumbs(addTwoNumbs(2,3),(3+4))+5)
a=int(input("please enter your first number"))
b=int(input("please enter your second number"))
def doubleOrDiff(x,y):
    if(x==y):
     return addTwoNumbs(x,y)
    elif(x>y):
     return x-y
    elif(y>x):
     return y-x
c=doubleOrDiff(a,b)
print(c)
print(doubleOrDiff(a,c))
print(doubleOrDiff(b,c))
print(a)
print(b)
