# Exercise1
print("Ex 1\n")
def c_to_f(temp):
    return ((9/5) * temp) + 32

def f_to_c(temp):
    return (5/9) * (temp - 32)

def calculate(func, temp):
    print(func(temp))

calculate(c_to_f, 100)
calculate(f_to_c, 32)
calculate(c_to_f, 43)

