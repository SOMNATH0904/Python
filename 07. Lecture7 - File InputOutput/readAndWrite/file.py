f = open("hello.txt", "r+")
f.write("Hello World!")
print(f.read())
f.close()