# Write a recursive function to calculate the sum of first n natural numbers.

def sumNumbers(n):
    if(n == 0):
        return 0
    return sumNumbers(n-1) + n 

print(sumNumbers(5))