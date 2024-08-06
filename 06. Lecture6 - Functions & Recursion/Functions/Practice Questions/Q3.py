# WAP to find the factorial of n. (n is a parameter)

# USING WHILE LOOP
def calcFact(n):
    fact = 1
    while(n != 1):
        fact *= n
        n -= 1
    return fact

print(calcFact(5))


# USING FOR LOOP
def calcFact1(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

calcFact1(6)