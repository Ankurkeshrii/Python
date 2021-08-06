aa=input("Enter Your Name : ")
print("Hello", aa, "Welcome to Ankur's Calculator Programme")

c=int(input('''Press (1 for Addition)
(2 for Subtraction)
(3 for Multiplication)
(4 for Division) For your preffered result\n'''))

#SUM
if c==1:
    a=int(input("Enter Your First Number : "))
    b=int(input("Enter Your Second Number : "))
    summ=a+b
    print("If u wanna add third number Enter '1' else '0'")
    last=int(input())
    if last==0:
        print('On Adding',a,'and',b,'we get',summ)
    elif last==1:
        z=int(input("Enter Your Third Number : "))
        sum3=summ+z
        print('On Adding',a,',',b,'and',z,'we get',sum3)

#Minus
if c==2:
    a=int(input("Enter Your First(Biggest) Number : "))
    b=int(input("Enter Your Second Number : "))
    minus=a-b
    print("If u wanna subtract third number enter '1' else '0'")
    last=int(input())
    if last==0:
        print("On Subtracting",a,'from',b,'we get',minus)
    elif last==1:
        z=int(input("Enter Your Third Number : "))
        minus3=minus-z
        print('On Subtracting',b,'and',z,'from',a,'we get',minus3)

#Multiplication
if c == 3:
    a=int(input("Enter Your First Number : "))
    b=int(input("Enter Your Second Number : "))
    mul=a*b
    print("Enter 1 if u wanna multiply third number else Enter 0")
    third=int(input())    
    if third==0:
        print('On Multiplying',a,'with',b,'we get',mul)
    elif third==1:
        z=int(input("Enter Your Third Answer : "))
        mul3=mul*z
        print('On Multiplying',a,'with',b,'and',z,'we get',mul3)

#Division
if c==4:
    a=int(input("Enter Your Dividend : "))
    b=int(input("Enter Your Divisor : "))
    div=a/b
    print("Enter 1 if u wanna divide the quotient obtained again with third number else Enter 0")
    third=int(input())
    if third==0:
        print("By Dividing",a,'by',b,'we get',div)
    elif third==1:
        z=int(input("Enter Your third Number : "))
        div3=div/z
        print("By Dividing",a,'by',b,'we get',div)
        print('On Dividing',div,'by',z,'we get',div3)

print('''Thank You For Using Ankur's Calculator Programme
Have A Nice Day Ahead''')