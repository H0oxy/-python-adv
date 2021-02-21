# 1
# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#
#     return wrapper
#
#
# def say_whee():
#     print("Whee!")
#
#
# say_whee = my_decorator(say_whee)
# say_whee()



# 2
# from datetime import datetime
#
# def not_during_the_night(func):
#     def wrapper():
#         if 7 <= datetime.now().hour < 22:
#             func()
#         else:
#             pass  # Hush, the neighbors are asleep
#     return wrapper
#
# def say_whee():
#     print("Whee!")
#
# say_whee = not_during_the_night(say_whee)
#
# say_whee()



# 3
# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
#
# @my_decorator
# def say_whee():
#     print("Whee!")
# say_whee()



# 4
# from decorators import do_twice
#
# @do_twice
# def say_whee():
#     print("Whee!")
# say_whee()




# 5
# from decorators import do_twice
#
# @do_twice
# def greet(name):
#     print(f"Hello {name}")
# greet("World")



# 6
from decorators import do_twice

@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"

6