# 13) Given a list
# S = [1,2,[3,4,[5,6,[7,8,[9,[0]]]]]]
# Answer correctly:
# The size of the S list.
# The size is 3
#  An expression that replaces the 0 in the list with 17.
s = [1,2,[3,4,[5,6,[7,8,[9,[0]]]]]]
print(len(s))

print(s)
s[2][2][2][2][1] = [17]
print(s)