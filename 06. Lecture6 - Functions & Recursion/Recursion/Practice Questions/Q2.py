# Write a recursive function to print all elements in a list:
# Hint: use list & index as parameters.

def printElements(list, idx):
    if(idx == len(list)):
        return
    print(list[idx])
    printElements(list, idx+1)


fruits = ["apple", "mango", "grapes", "pomogrenate", "orange"]

printElements(fruits, 0)