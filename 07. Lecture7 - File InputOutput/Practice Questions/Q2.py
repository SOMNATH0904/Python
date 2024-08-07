# WAP that replaces all occurences of "java" with "python" in "practice.txt" file.

with open("practice.txt", "r") as f:
    data = f.read()

newData = data.replace("Java", "Python")
print(newData)

with open("practice.txt", "w") as f:
    f.write(newData)