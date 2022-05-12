
#simple decorator using @ and function

"""def make_uppercase(func):
    def inner():
        greet = func()
        print(greet.upper())
    return inner
        
        
@make_uppercase
def say_hello():
    return "Hello World"
say_hello()"""

#####################################
"""def make_uppercase(func):
    def inner():
        greet = func()
        print(greet.upper())
    return inner
        
        
@make_uppercase
def say_hello():
    return "Hello World"
say_hello()


@make_uppercase
def hello_my_guest():
    return "My Guest, welcome to home"
hello_my_guest()


@make_uppercase
def small_to_upper():
    return "python master class"
small_to_upper()"""

###################################
####### Multiple decorator ##############

"""def make_uppercase(func):
    def inner():
        greet = func()
        print(greet.upper())
        return func()
    return inner


def remove_whitespace(func):
    def inner():
        greet = func()
        print(greet.strip())
        return func()
    return inner
        
        
@make_uppercase
def say_hello():
    return "Hello World"
say_hello()


@make_uppercase
def hello_my_guest():
    return "My Guest, welcome to home"
hello_my_guest()



@remove_whitespace
@make_uppercase
def small_to_upper():
    return "  python master class  "
small_to_upper()"""

######################################
################ universal arg #######

def make_uppercase(func):
    def inner(*args, **kwrgs):
        greet = func(*args, **kwrgs)
        print(greet.upper())
        return func(*args, **kwrgs)
    return inner


def remove_whitespace(func):
    def inner(*args, **kwrgs):
        greet = func(*args, **kwrgs)
        print(greet.strip())
        return func(*args, **kwrgs)
    return inner
        
        
"""@make_uppercase
def say_hello():
    return "Hello World"
say_hello()


@make_uppercase
def hello_my_guest():
    return "My Guest, welcome to home"
hello_my_guest()
"""


@remove_whitespace
@make_uppercase
def small_to_upper(msg):
    return msg

small_to_upper("Hello Bangladesh")

