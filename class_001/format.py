#Format
name = "Bruno"
height = 1.70
weight = 75
bmi = weight / (height * height)
print("Hello " + name + " your BMI is: " + str(round(bmi, 2)))
print("\nFormats")
print("Hello", name, "your BMI is:", round(bmi, 2))
print(f'Hello {name} your BMI is: {bmi:.2f}')
print("Hello {} your BMI is: {}".format(name, round(bmi, 2)))
print("Hello {} your BMI is: {:.2f}".format(name, bmi))
print("Hello {my_name} your BMI is: {my_bmi}".format(my_name = name, my_bmi = round(bmi, 2)))
