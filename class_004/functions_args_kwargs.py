#Function / defined parameters (ARGS / KWARGS)
def my_bmi(height, weight, name = ""):
    bmi = weight / (height**2)
    print("Hello {name} your bmi is {bmi}".format(name=name,bmi=bmi))

my_bmi(1.70, 90)

my_bmi(1.70, 90, "Bruno")
my_bmi(1.70, 90, name="Bruno")

def my_bmi_args(*args):
    bmi = args[1] / (args[0]**2)
    print(args[2], bmi)

my_bmi_args(1.70, 90, "Bruno")

def my_bmi_kwargs(**kwargs):
    if kwargs.get("weight") is None or kwargs.get("height") is None:
        print("Invalid kwargs")
        return
    bmi = kwargs["weight"] / (kwargs["height"]**2)
    print(kwargs["name"], bmi)

my_bmi_kwargs(height=1.70, weight=90, name="Bruno")
my_bmi_kwargs(height=1.70, name="Bruno")

