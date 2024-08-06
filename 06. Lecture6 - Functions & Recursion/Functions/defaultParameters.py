def checkDef(a, b=1):
    sum = a+b
    return sum

# print(checkDef())     -> This will give as Error (checkDef() missing 2 required positional arguments: 'a' and 'b')
print(checkDef(1, 3))
print(checkDef(8))