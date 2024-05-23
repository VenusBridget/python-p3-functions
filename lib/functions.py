#!/usr/bin/env python3

def greet_programmer():
    print ('Hello, programmer!')
greet_programmer()

def greet(name):
    print (f'Hello, {name}!')
greet ('Bridget')
    

def greet_with_default(name="programmer"):
    print (f'Hello, {name}!')
greet_with_default()


def add(num1, num2):
    print (num1 + num2)
    return (num1 + num2)
add (2,2)

def halve(number):
    pass
    print (number/2)
    return number/2
halve(4)
