# 11) Develop a program that displays the sum of the odd and even 
# values of the sequence ([21, 5, 34, 8, 16, 7, 3])
list = [21, 5, 34, 8, 16, 7, 3]
sum_odd = 0
sum_even = 0
for i in list:
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i

print("Odd", sum_odd, "Even", sum_even)