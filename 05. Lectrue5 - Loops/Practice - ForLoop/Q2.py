# Search for a number x in this tuple using a loop.
# (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
idx = 0
x = int(input("Enter a number to find :"))
for el in tup:
    if(el == x):
        print(x,"is found at index",idx)
        break
    idx += 1
