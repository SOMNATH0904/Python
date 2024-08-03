'''
1st Part: WAP to count the number of students with the "A" grade in the following tuple.
["C", "D", "A", "A", "B", "B", "A"]

2nd Part: Store the above values in a list and sort them from "A" to "D".
'''

#1st Part Ans:
grade = ("C", "D", "A", "A", "B", "B", "A")
print("Students with grade 'A' is :",grade.count("A"))

#2nd Part Ans:
grade = ["C", "D", "A", "A", "B", "B", "A"]
grade.sort()
print(grade)
