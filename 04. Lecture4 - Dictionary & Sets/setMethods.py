collection = set()

collection.add(1)
collection.add(2)
collection.add(1)
collection.add("Somnath")
print(collection)

#collection.add([1, "Hello"])    #Error -> TypeError: unhashable type: 'list'(as list is mutable)
collection.add((4, 6, "Hello")) #We can add tuple as it is immutable
print(collection)
print(len(collection))

collection.remove(2)
print(collection)

collection.clear()
print(collection)
print(len(collection))

#pop() method is in another file

set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.union(set2)) #This union() method returns new set, doesn't modifies the old set
print(set1)
print(set2)

print(set1.intersection(set2)) #This intersection() method returns new set, doesn't modifies the old set
