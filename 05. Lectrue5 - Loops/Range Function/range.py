# Syntax of Range : range(start?, stop, step?)

seq = range(5)
# print(seq[0])
# print(seq[1])
# print(seq[2])
# print(seq[3])
# print(seq[4])
# print(seq[5])     -> Will give error as this range() function takes one value less to the assigned value, i.e, ending position is not included.

for i in seq:
    print(i)
