num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))
num3=int(input("Enter number 3: "))
num4=int(input("Enter number 4: "))

if num1>num4:
    w1=num1
elif num4>num1:
    w1=num4

if num2>num3:
    w2=num2
elif num3>num2:
    w2=num3

if  w1>w2:
    print(w1,"is the largest number")
elif w2>w1:
    print(w2,'is the largest number')
