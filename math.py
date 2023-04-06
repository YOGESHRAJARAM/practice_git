import random
number=range(1,100)
a=random.choice(number)
b=random.choice(number)
addition= a + b
subraction= a - b
multip= a * b
devi=a / b
process=("+","-","*","/")
k=random.choice(process)
print(k)
if k == "+":
    print("add this two numbers :",a ,"+",b)
    qus1=int(input("enter your answers ="))
    if qus1 == addition:
        print("answer correct")
    else:
        print("wrong answer")
        print(" the answer is :",addition)

elif k == "-":
    print("subtract two number :",a ,"-",b)
    qus1=int(input("enter your answers ="))
    if qus1 == subraction:
        print("answer correct")
    else:
        print("wrong answer")
        print("the answer is :",subraction)
elif k == "*":
    print("multiplay two number :",a, "*",b)
    qus1=int(input("enter your answers ="))
    if qus1 == multip:
        print("answer correct")
    else:
        print("wrong answer")
        print("the answer is :",multip)
elif k == "/":
    print("devide two number :",a, "/",b)
    qus1=int(input("enter your answers ="))
    if qus1 == devi:
        print("answer correct")
    else:
        print("wrong answer")
        print("the answer is :",devi)
else:
    print("thank you")

    
    



