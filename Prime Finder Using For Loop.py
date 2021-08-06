num=int(input("Enter the number: "))
for i in range(2,num):
    if num%i==0:
        print("Your Number",num,'is not Prime')
        break
else:
    print("Your Number",num,"is Prime")