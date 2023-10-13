name = input("Enter the name: ")
height = float(input("Enter the height: "))
weight = float(input("Enter the weight: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    classification = "Underweight"
elif bmi < 25:
    classification = "Normal weight"
elif bmi < 30:
    classification = "Overweight"
elif bmi < 35:
    classification = "Obesity class 1"
elif bmi < 40:
    classification = "Obesity class 2"
else :
    classification = "Obesity class 3"


print("Hello", name, "your BMI is:", round(bmi, 2), "Classification:", classification)