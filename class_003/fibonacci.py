#Exercises
#1 Fibonacci
print("Fibonacci")
n1 = 0
n2 = 1
sequence_size = -1
while(sequence_size < 0):
    sequence_size = int(input("How many numbers?"))

if sequence_size < 2 :
    print(n1)
elif sequence_size < 3:
    print(n1, n2)
else:
    print(n1, n2, end=" ")
    for i in range(2, sequence_size):
        print(n1 + n2, end=" ")
        n1, n2 = n2, n1 + n2
        