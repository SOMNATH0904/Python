# Print the multiplication table of a number n.

n = int(input("Enter a Number :"))
i = 1
print("The Multiplication table of a number",n,"is :")
while(i <= 10):
    print(n,"*",i,"=",(n*i))
    i += 1

