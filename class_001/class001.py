#OUTPUTS
print("OUTPUTS")
print("Hello World!")
print("Hello\nWorld!")
print("Hello" + " " + "world!")
print("Hello", "World!")
print("Hello", "World!", sep="-")
print("Hello", "World!", end="*")
print("teste")

#Question 1
print("203","940","239", sep=".", end="-")
print("10")

# Types
print("\nTypes")
print("Renan", type("Renan"))
print(123, type(123))
print(123.4, type(123.4))
print(2 == 2, type(2 == 2))
#Cast
print("\nCast")
print(bool(""))
print(bool("abc"))
print(int("123"))
print(str(123.4))

# Arithmetic Operators
print("\nArithmetic Operators")
print(4 + 7);
print(12 - 5);
print(6 * 6);
print(30 / 5)
print(10 % 4)
print(18 // 5)
print(3 ** 5)
print("\nEx")
print(5.2 / 2)
print(int(5.2 / 2))
print("Test" * 10)
print(str(20) + "Test")
print(int(4.5)/3)

#Variables
print("\nVariables")
my_var = "Bruno"
print(my_var, type(my_var))
my_var = 10
print(my_var, type(my_var))
my_var = 122.42
print(my_var, type(my_var))

name = "Bruno"
height = 1.70
weight = 75
bmi = weight / (height * height)
print("Hello " + name + " your BMI is: " + str(round(bmi, 2)))
#Format
print("\nFormats")
print("Hello", name, "your BMI is:", round(bmi, 2))
print(f'Hello {name} your BMI is: {bmi:.2f}')
print("Hello {} your BMI is: {}".format(name, round(bmi, 2)))
print("Hello {} your BMI is: {:.2f}".format(name, bmi))
print("Hello {my_name} your BMI is: {my_bmi}".format(my_name = name, my_bmi = round(bmi, 2)))

#input
print("\nInputs")

name = input("Entrer name: ")
print(name)

number = int(input("Entrer number: "))
print(number, type(number))
##