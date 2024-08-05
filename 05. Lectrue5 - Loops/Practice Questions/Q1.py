# WAP to find all the sum of first n natural numbers. (Using while)

n = int(input("Enter a number : "))
sum = 0
temp = n
while(temp != 0):
    sum += temp
    temp -= 1
print("Sum of first",n,"natural numbers is :",sum)


'''
USING FOR LOOP

n = 5
sum = 0
for i in range(1, n+1):
    sum += i
print("Total Sum :",sum)
'''