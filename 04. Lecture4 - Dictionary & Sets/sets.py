num = {1, 2, 3, 4}
set2 = {1, 2, 2, 2}     #repeated elements stored only once, so it will be resolved to {1, 2}
collection = {1, 2, 2, 2, "hello", "world", "somnath"}  #when we will print this, it will be in unordered collection, as sets property says that each element in the set must be unique and immutable.

print(num)
print(set2)
print(collection)

nullSet = set()
print(nullSet)
