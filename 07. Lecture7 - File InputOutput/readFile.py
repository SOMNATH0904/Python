f = open("demo.txt", "r")
data = f.read()
print(data)
f.close()

f = open("demo.txt", "r")
data = f.read(8)
print(data)
f.close()