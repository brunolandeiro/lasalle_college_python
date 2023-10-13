#try / except
try:
    print(x)
except:
    print("Error catched")

print("any text")

try:
    print(x)
except NameError:
    print("the variable is not declared!")

try:
    print(x)
except NameError as name_error:
    print("the variable is not declared!", name_error)

try:
    a = 5/0
except ZeroDivisionError:
    print("You cannot divide a number by 0")

try:
    print(x)
    a = 5/0
except ZeroDivisionError:
    print("You cannot divide a number by 0")
except NameError:
    print("variable not declared")

try:
    x = "Bruno"
    print(x)
except Exception as ex:
    print("any error")
else:
    print("else")
finally:
    print("Finally")

try:
    print(y)
except Exception as ex:
    print("any error")
else:
    print("else")
finally:
    print("Finally")


def division (n1, n2):
    if(n2 == 0):
        raise ValueError("n2 cannot be 0")
    return n1 / n2

try:
    print(division(5, 0))
except Exception as ex:
    print(ex)