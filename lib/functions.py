#!/usr/bin/env python3

def greet_programmer():
    pass

def greet(name):
    pass

def greet_with_default(name="programmer"):
    pass

def add(num1, num2):
    pass

def halve(number):
    pass
# In lib/functions.py

def greet_programmer():
    print("Hello, programmer!")

def greet_programmer():
    greeting = "Hello, programmer!"
    print(greeting)
    return greeting

def greet(name):
    greeting = f"Hello, {name}!"
    print(greeting)
    return greeting

def greet_with_default(name="programmer"):
    greeting = f"Hello, {name}!"
    print(greeting)
    return greeting

def add(num1, num2):
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
    return result

def halve(number):
    result = number / 2
    print(f"Half of {number} is {result}")
    return result
