'''
Figure out a way to store 9 & 9.0 as seperate values in the set.
(You can take help of built-in data types)
'''

values = {9, 9.0}
print(values)

values = {9, "9.0"} #1st way
print(values)

values = {"9", 9.0} #2nd way
print(values)

values = {          #3rd way -> pair in the form of tuples
    ("float", 9.0),
    ("int", 9)
}
print(values) 