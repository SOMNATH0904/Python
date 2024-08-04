'''
WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add
one by one. Use subject name as key & marks as value.
'''

marks = {}

a = int(input("Enter Physics marks : "))
marks.update({"phy": a})

a = int(input("Enter Chemistry marks : "))
marks.update({"chem": a})

a = int(input("Enter Maths marks : "))
marks.update({"math": a})

print(marks)