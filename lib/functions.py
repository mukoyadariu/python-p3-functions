#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print("Hello, " + name + "!")

def greet_with_default(name="programmer"):
    print("Hello, " + name + "!")

def add(num1, num2):
    return num1 + num2

def halve(number):
    return number / 2

greet_programmer()
greet("Guido")
greet_with_default()
greet_with_default("Mike")
result=add(1, 2)
print(result)
halved_value=halve(40)
print(halved_value)
