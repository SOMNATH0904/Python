'''
WAP to check if a list contains a palindromne of elements.(Hint: use copy() method)
Examples -> [1, 2, 3, 2, 1] or [1, "abc", "abc", 1]
'''

list = [1, 2, 3, 2, 1]
tempList = list.copy()
tempList.reverse()
# print("List :",list)
# print("TempList :",tempList)
if(list == tempList):
    print("List is a Palindrome.")
else:
    print("List is not a Palindrome.")