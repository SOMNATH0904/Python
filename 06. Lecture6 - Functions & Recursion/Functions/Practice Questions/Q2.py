# WAP to print the elements of a list in a single line. (list is a parameter)

list1 = [1, 2, 3, 4, 5]
heroes = ["thor", "ironman", "captain america", "shaktimaan"]

def printElements(list):
    for i in list:
        print(i,end=" ")
    print()

printElements(list1)
printElements(heroes)