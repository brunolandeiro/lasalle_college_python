#decorators
'''
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)
say_whee()

@my_decorator
def say_hey():
    print("Hey!!")

say_hey()
'''
###################
'''
def say_hello():
    print("Hello")

say_hello()

def my_master():
    def first_slave():
        print("first slave Hello!")
    return first_slave

my_master()

my_var = my_master()
my_var()

print("\n########\n\n")

def my_master(my_func):
    def first_slave():
        print("Now i am decorated")
        my_func()
    return first_slave

my_var = my_master(say_hello)

my_var()

print("\n########\n\n")

say_hello = my_master(say_hello)
say_hello()

print("\n########\n\n")

def my_master(my_func):
    def first_slave(*agrs, **kwargs):
        print("Now i am decorated")
        my_func(*agrs, **kwargs)
    return first_slave

@my_master
def say_hello_2(msg):
    print(msg)

say_hello_2("Cool!!!")
'''
#Usage
import time as times
def speed(my_func):
    def slave(*args, **kwargs):
        start = times.time();
        my_func(*args, **kwargs)
        end = times.time();
        time = (end - start) * 1000
        print("spend", time, "ms to run") 
    return slave

my_list =[1,2,3,4,5,6,7,8,9,10]

@speed
def test_for(my_list):
    for i in range(len(my_list)):
        print(my_list[i])

@speed
def test_foreach(my_list):
    for i in my_list:
        print(i)

test_for(my_list)
test_foreach(my_list)