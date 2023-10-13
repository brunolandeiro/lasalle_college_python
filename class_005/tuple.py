# tuples

tuple1 = ("Bruno", 30, 1.68)
print(tuple1)
print(tuple1[0])
print(tuple1[0:2])
print(tuple1[-3:-1])

tuple2 = tuple1 + ("Lemos", 1993)
n1, n2, n3, n4 ,n5 = tuple2
print(n1, n2, n3, n4 ,n5)

n1, *n2 = tuple2
print(n1, n2)

n1, *n2, n3 = tuple2
print(n1, n2, n3)

tuple2 = list(tuple2)
print(tuple2)
tuple2[1]=31
tuple2 = tuple(tuple2)
print(tuple2)

print(tuple2.count("Bruno"))
print(tuple2.index("Bruno"))
print(len(tuple2))

for i in tuple2:
    print(i)
