from math import *
# lecture 1
print("Hello World")
# lecture 2 
print("   /|")
print("  / |")
print(" /  |")
print("/___|")
# lecture 3
character_name = "John"
character_age = "35"
print("There once was a man named " + character_name + ",")
print("he was " + character_age + " years old.")

character_name = "Mike"
print("he really liked the name " + character_name + ",")
print("but did not like being " + character_age + ".")
# 3 basic types of data in Python:
# string, number , boolen number: is_male = False
# lecture 4 working with string
print("Giraffe\nAcademy")
# \n  starts a new line
print("Giraffe\"Academy")
# print quotation mark
phrase = "Giraffe Academy"
print(phrase + " is cool")
print(phrase.upper())
print(phrase.lower())
print(phrase.isupper())
print(phrase.upper().isupper())  
print(len(phrase))
print(phrase[0])
print(phrase.index("G"))
#  print(phrase.index("z"))
print(phrase.replace("Giraffe", "Elephant"))
# lecture 5 working with numbers
print(-2.0987)
print(3 + 4.5)
print(10 % 3)  # print the reminder
my_num = 5
print(str(my_num) + " my favpurate number")
print(abs(my_num))
print(pow(3, 2))
print(round(3.2))
print(floor(3.7))
print(ceil(3.2))
print(sqrt(36))
# lecture 6 getting input from users
# name = input("Enter your name: ")  # open and closed parentheses
# age = input("Enter your age: ")
# print("Hello " + name + "! You are " + age)
# lecture 6 building a basic calculator
# num1 = input("Enter a float number: ")
# num2 = input("Enter another int number: ")
# result = float(num1) + int(num2)
# print(result)
# lecture 7 mad libs game
# color = input("Enter a color: ")
# plural_noun = input("Enter a plural noun: ")
# celebrity = input("Enter a celebrity: ")
# print("Roses are " + color)
# print(plural_noun + " are blue")
# print("I love " + celebrity)
# lecture 8 lists
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
# we can also input boolen and number into list
friends[1] = "Mike"
print(friends[0])
print(friends[-1])
print(friends[1:])
print(friends[1:3])
# lecture 8 lit functions
lucky_number = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.sort()
friends.reverse()
print(friends)
friends.extend(lucky_number)
friends.append("Creed")
friends.insert(1, "Kelly")
friends.remove("Jim")  # friends.clear(), friends.pop()
print(friends)
print(friends.index("Toby"))
print(friends.count("Toby"))
friends2 = friends.copy()
# lecture 9 tuples
coordinates = [(4, 5), (6, 7), (80, 34)]  # tuple is immutable
# coordinates[1] = 10  # This will rise an error.
print(coordinates[0])
# lecture 10 functions


def say_hi(name, age):
    print("Hello " + name + ", you are " + str(age))


say_hi("Mike", 35)
say_hi("Tim", 70)
# lecture 11 return statement


def cube(num):
    result = pow(num, 3)
    return result


print(cube(4))
# lecture 12 if statements
# num1 == float(input("Enter first number: "))
# num2 == float(input("Enter second number: "))
# if op == "+":
#     print(num1 +num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "/":
#     print(num1 / num2)
# elif op == "*":
#     print(num1 * num2)
# else:
#     print("Invalid operator")
# lecture 13 dictionaries
# Jan -> January
monthConversions ={
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversions["Nov"])
print(monthConversions.get("Dec"))
print(monthConversions.get("Luv"))  # default value
print(monthConversions.get("Luv", "Not a valid Key"))
# lecture 14 while loops
i = 1
while i <= 10:
    print(i)
    i += 1

print("Done with loop")
# lecture 15 building a guessing game
# secret_word = "giraffe"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False
# while guess != secret_word and not(out_of_guesses):
#     if guess_count < guess_limit:
#         guess = input("Enter guess: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True
# if out_of_guesses:
#     print("Out of guesses, You lose!")
# else:
#     print("You win!")
# lecture 16 for loops
friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)
for letter in "Giraffe Academy":
    print(letter)
for index in range(3, 10):
    print(index)
for index in range(len(friends)):
    print(friends[index])
for index in range(5):
    if index == 0:
        print("first Iteration")
    else:
        print("Not a fisrt iteration")
# lecture 17 exponent function
print(2**3)
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
print(raise_to_power(3, 2))
# lecture 18 2D lists & Nested loops
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][1])
for row in number_grid:
    for col in row:
        print(col)
# lecture 19 build a translator
# Giraffe Language
# vowels -> g
# dog -> dgg
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter

    return translation

# print(translate(input("Enter a phrase:")))
# lecture 20 comment
# lecture 21 try except
# try:
#     answer = 10/0
#     number = int(input("Enter a number:"))
#     print(number)
# except ValueError:
#     print("Invalid Input")
# except ZeroDivisionError as err:
#     print(err)
# we should write the specific error instead of broad error
# lecture 22 reading files
# employee_file = open ("employees.txt", "r")
# print(employee_file.readable())
# print(employee_file.readline())
# print(employee_file.readline())
# print(employee_file.readlines())
# for employee in employee_file.realines():
#     print(employee)
# employee_file.close()
# open ("employees.txt", "w")
# open ("employees.txt", "a")
# lecture 23 writing to files
# employee_file = open ("employees.txt", "w")
# employee_file.write("Toby - Human Resources")
# employee_file.write("\nKelly - Customer Service")
# employee_file.close()
# employee_file = open ("index.html", "w")
# employee_file.write("<p>This is HTML</p>")
# employee_file.close()
# lecture 24 modules and pip
import useful_tools
print(useful_tools.roll_dice(10))
# lecture 25 classes & objects
from Student import Student
Student2 = Student("Pam", "Art", 2.5, True)
print(Student2.gpa)
# lecture 26 building a multiple choice quiz
question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]
# questions = [
#     Question(question_prompts[0], "a"),
#     Question(question_prompts[1], "c"),
#     Question(question_prompts[2], "b")
# ]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question_prompts)
        if answer == question.answer:
            score += 1
        print("You got " + str(score) + "/" + str(len(questions)) + "correct")
# lecture 27 object functions
def on_honor_roll(self):
    if self.gpa >= 3.5:
        return True
    else:
        return False
print(Student2.on_honor_roll())
# lecture 28 inheritance
from Chef import Chef
from ChineseChef import ChineseChef
mychef = Chef()
mychef.make_chicken()
myChineseChef = ChineseChef()
myChineseChef.make_chicken()
myChineseChef.make_special_dish()
# lecture 29 python interpreter
# 在mac搜索框中输入terminal即可与你的mac激情对话
