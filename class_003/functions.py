def my_function():
    print("My name is: ")

my_function()

def my_function_param(name):
    print("My name is: {name}".format(name=name))

my_function_param("Bruno Landeiro")
my_name = "Bruno Lemos"
my_function_param(my_name)

def sum(num1, num2):
    return num1 + num2

result = sum(1,1)
print("Return of the function sum: {result}".format(result=result))

def my_func_param_func(func):
    func("Bruno")

#my_func_param_func(my_function)

my_func_param_func(my_function_param)

def swap_number(num1, num2):
    return num2, num1

print(swap_number(6, 7))

num1 = 1
num2 = 2
num1, num2 = swap_number(num1, num2)
print(num1, num2)

#Function returning a function

def my_calc_sum(num1, num2):
    print(num1 + num2)

def my_calc_mult(num1, num2):
    print(num1 * num2)

def my_calculator(op):
    if(op == "+"):
        return my_calc_sum;
    if(op == "*"):
        return my_calc_mult;

my_calculator("*")(1,5)
fx = my_calculator("+")
fx(1,5)
#print de reference in the memory
print(id(fx), id(my_calc_sum))