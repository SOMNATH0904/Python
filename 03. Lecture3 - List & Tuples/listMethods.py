list = [2, 1, 3]
print(list)     #[2, 1, 3]

list.append(4)
print(list)     #[2, 1, 3, 4]

list.sort()
print(list)     #[1, 2, 3, 4]

list.sort(reverse=True)
print(list)     #[4, 3, 2, 1]

list.reverse()
print(list)     #[1, 2, 3, 4]

# list.insert(2, 12)
# print(list)     #[1, 2, 12, 3, 4]

list.remove(3)      #remove(element) method removes the first occurence of the element, i.e., if list contains [2, 1, 3, 1] and we implement list.remove(1) then, the output will be [2, 3, 1]
print(list)     #[1, 2, 12, 4]

list.pop(1)         #removes element at idx
print(list)     #[1, 12, 4]

list.insert(2, 12)
print(list)     #[1, 2, 12, 3, 4]
