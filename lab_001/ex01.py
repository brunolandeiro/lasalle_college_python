# 1) Accept two int values from the user and return their product. 
# If the product is greater than 1000, then return their sum

def ex1(num1, num2):
    result = num1 * num2
    if result > 1000 :
        result = num1 + num2
    return result

num1 = int(input("Enter a integer number: "))
num2 = int(input("Enter other integer number: "))
print(ex1(num1, num2))
