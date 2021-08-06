aa=input("Enter Your Name : ")
print("Hello", aa, "Welcome to Ankur's Calculator Programme")
a=int(input("Enter Your First Number : "))
b=int(input("Enter Your Secod Number : "))
c=int(input('''Press (1 for Addition)
(2 for Subtraction)
(3 for Multiplication)
(4 for Division) For your preffered result\n'''))
if c==1:
    summ=a+b
    print('On Adding',a,'and',b,'we get',summ)
elif c == 2:
    minus=a-b
    print("On Subtracting",a,'from',b,'we get',minus)
elif c == 3:
    mul=a*b
    print('On Multiplying',a,'with',b,'we get',mul)
elif c == 4:
    div=a/b
    print("On Dividing",a,"with",b,"We get",div)
print('''Thank You For Using Ankur's Calculator Programme
Have A Nice Day Ahead''')