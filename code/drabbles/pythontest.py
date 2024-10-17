import math
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
def Asin(x, t):
  if abs(x)>1:
    return "error, no arcsine exists"
  if x==0:
    return 0
  else:
    if math.sin(x)-x<t:
      return x
    elif x<(math.sqrt(2)/2):
      a=x+math.sqrt(1-((t/4)*(t/4)))
      return AsinDU(x,t,a)
    else:
      a=1
      return AsinDD(x,t,a)
def AsinDD(x,t,a):
  if math.sin(a)-x<t:
    return a
  else:
    a-=math.sqrt(1-((t/4)*(t/4)))
    return AsinDD(x,t,a)
def AsinDU(x,t,a):
  if math.sin(a)-x<t:
    return a
  else:
    a+=math.sqrt(1-((t/4)*(t/4)))
    return AsinDU(x,t,a)