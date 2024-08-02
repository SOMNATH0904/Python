# WAP to find the greatest of 3 numbers entered by the user.

a = int(input("Enter 1st Number : "))
b = int(input("Enter 2nd Number : "))
c = int(input("Enter 3rd Number : "))

if((a >= b) and (a >= c)):
    print("Number1 :",a,"is Greatest")
elif(b >= c):
    print("Number2 :",b,"is Greatest")
else:
    print("Number3 :",c,"is Greatest")
