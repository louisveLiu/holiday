import math

name = "Bro"
print(type(name))

age = 21
print("Your age is: " + str(age))

a = b = c = 5
print(a)
print(b)
print(c)

name = "Louis Code"
print(name.find("s"))

print(name.capitalize())

print(name.upper())

name_digit = "123"
print(name.isdigit())
print(name_digit.isdigit())

print(name.isalpha())
name_alpha = "LouisCode"
print(name_alpha.isalpha())

print(name.count("o"))

print(name.replace("o", "a"))

#type casting: int(2.0)

# age = int(input("How old are you?: "))
# age += 1
# print(age)

# height = float(input("How tall are you?: "))
# print("You are " + str(height) + "cm tall")

print(round(math.pi))
print(abs(math.pi))
print(pow(math.pi, 2))

# string slicing
first_name = name[0:5]
print(first_name)
last_name = name[6:]
print(last_name)

funky_name = name[0:8:2]
print(funky_name)

website = "http://google.com"
slice = slice(7, -4)
print(website[slice])
print(website[7: -4])

# age = int(input("How old are you?: "))
# if age >= 18:
#     print("You are an adult!")
# elif age < 0:
#     print("You haven't been born yet!")
# else:
#     print("You are a child!")

# name = ""
# while len(name) == 0:
#     name = input("Enter your name: ")
# print("Hello" + name)

# rows = int(input("How many rows?: "))
# cols = int(input("How many columns?: "))
# symbol = input("Enter a symbol to use: ")
# for i in range(rows):
#     for j in range(cols):
#         print(symbol, end="")
#     print()
# Note that both end="" & print() are used to deal with the indention problem in columns and rows respectively.

# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break

# phone_number = "123-456-7890"
# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")
# print()

# continue: skips to the next iteration of the loop
# pass: does nothing, acts as a placeholder

for i in range(1, 21):
    if i == 13:
        pass
    else:
        print(i)

# 查tuple中某一element的位置可以用index语句

utensils = {"a", "b", "c", "d"}
for i in utensils:
    print(i)

# set_a_and_b = set_a.union(set_b)

# set_a.difference(set_b)

# set: unordered

capitals = {'USA':'Washington DC',
            'India':'New Dehli',
            'China':'Beijing',
            'Russia':'Mescow'}
# print(capitals['Germany'])
print(capitals.get('Germany'))
print(capitals.keys())
print(capitals.values())

for key,value in capitals.items():
    print(key, value)

capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})
capitals.pop('China')
capitals.clear()

# *arg = parameter that will pack all arguments into a tuple
# useful so that a function can accept a varing amount of arguments

# **kwargs = parameter that will pack all arguments into a dictionary
# useful so that a function can accept a varing amount of keyword arguments

def hello(**kwargs):
    print("Hello " + kwargs['first'] + " " + kwargs['last'])

hello(first='Suck', last='you')

def hello_1(**kwargs):
    print("Hello",end=" ")
    for key, value in kwargs.items():
        print(value,end=" ")

hello_1(title="Mr.",first="Louis",last="Liu")

animal = "cow"
item = "moon"
print( "\nThe {} jumped over the {}".format(animal, item))
print( "The {1} jumped over the {0}".format(animal, item))
print( "The {item} jumped over the {item}".format(animal, item="sun"))
print( "The {:>10} jumped over the {}".format(animal, item))
print( "The {:<10} jumped over the {}".format(animal, item))
print( "The {:^10} jumped over the {}".format(animal, item))
print( "The {item:10} jumped over the {animal}".format(animal="me", item="duck"))
print( "The {0:>10} jumped over the{1}.".format(animal, item))
number = 3.14159
print("The number pi is {:.2f}".format(number))

number = 1000
print("The number pi is {:b}".format(number))
print("The number pi is {:,}".format(number))
print("The number pi is {:o}".format(number))  # eigit-digit computation
print("The number pi is {:x}".format(number))
print("The number pi is {:E}".format(number))

# pseudo-random
import random
x = random.randint(1, 6)
y = random.random()
print(x)
print(y)

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "3", "Q", "K", "A"]
random.shuffle(cards)
print(cards)

# try ...     (2:40:00)
# except ...
# except ZeroDivisionError as e
# print(e)
# except ValueError
# except Exception
# else: print ...
# finally:

import os

# path = "..."
# if os.path.exists(path):
#    print(...)
#    if os.path.isfile(path):
#        print()
#    elif os.path.isdir(path):
#        print()
# else:
#      print("location does not exist.")

# python read file
# try:
#     with open('test.txt) as file:
# except FileNotFoundError:
# print("That file was not found :(")

text = "Yoooooooo\nThis is some text\nHave a good one!\n"
with open('test.py', 'w') as file:
    file.write(text)

import shutil

# copyfile(): copies contents of a file
# copy(): copyfile() + permission mode + destination can be a directory
# copy2(): copy() + copies metadata (file's creation and modication times)

import shutil
shutil.copyfile('test.py', 'copy.txt')

# os.rmdir(path): FileNotFoundError, PermissionError
choices = ["a", "b", "c"]
computer = random.choice(choices)
print(computer)

class Car:
    color = None
def change_color(car, color):
    car.color = color
car_1 = Car()
car_2 = Car()
car_3 = Car()
change_color(car_1,"white")
change_color(car_2,"white")
change_color(car_3,"white")
print(car_1.color)
print(car_2.color)
print(car_3.color)

class Duck:
    def walk(self):
        print("This duck is walking.")
    def talk(self):
        print("This duck is talking")
class Person():
    def catch(self, chick):
        chick.walk()
        chick.talk()
duck = Duck()
person = Person()
person.catch(duck)

# walrus operator
print(happy := True)

# foods = list()
# while True:
#     food = input("What food do you like?: ")
#     if food == "quit":
#         break
#     foods.append(food)
# while food := input("What food do you like?: ") != "quit":
#     food.append(food)

def quiet(text):
    return text.lower()
def hello(func):
    text = func("Hello")
    print(text)
hello(quiet)

double = lambda x:x * 2
multiply = lambda x, y: x * y
full_name = lambda first_name, last_name: first_name+" "+last_name
age_check = lambda age:True if age >= 18 else False
print(double(5))

cities_in_F = {'NY':32, 'Bos':75, 'LA':100, 'Chiag':50}
cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
print(cities_in_C)

def hello():
    print("Hello!")
if __name__ == '__main__':
    hello()
print(__name__)

import time
print(time.ctime(0))
print(time.time())

from tkinter import *
window = Tk()
photo = PhotoImage(file='/Users/liuqinyu/Desktop/math_document/self_study/cosplay.jpeg')
label = Label(window,
              text="Hello World!",
              font=('Arial',40,'bold'),
              fg='00FF00',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom')
label.place(x=100, y=100)
window.mainloop()