# Variables
#price = 15              # integer
#first_name = "Ali"      # string
#score = 4.5             # float
#is_new = True           # boolia

#print('price =', price + score)
#print("new user =", is_new)
#print('0----' * 2)
#print('-1111'*2)
#print('* ' * 10)

# get Input from User
#name = input("What is your name? ")
#color = input("What color do you like? ")
#print(name + " likes " + color)

## Type Conversion
#birth_year = input("Birth year: ") # inputs are always string and to use as int or other types should be converted
#print(type(birth_year)) # see var type
#age = 2020 - int(birth_year) # converting by int() or float() or bool()
#print(type(age))
#print("your age:" , age)
#weigh_lbs = input("weigh (lbs): ")
#weigh_kg = float(weigh_lbs) * 0.45
#print("weigh (kg):" , weigh_kg)

# Stings
#course = "Python's course for Beginners" # having an apostrophe in string
#b_course = 'Python for "Beginners"' # having a double quotes
#course = """
#Hi xyz,
#
# here is my first mail.
#
# thank you
# course for Beginners
# """ # having more lines as a string with help of three single/double quotes
#course = "Python for Beginners"
#print(course[0]) # using Index of character from left to right start with 0 -- here prints P
#print(course[-1])# using Index of character from right to left start with -1 -- here prints s
#print(course[-2])# using Index of character from right to left start with -1 -- here prints r
#print(course[0:3]) # from index 0 to index 2 (interpreter doesn't count last one(here index 3)) -- here prints Pyt
#print(course[-4:-1])# from index -4 to index -2 (interpreter doesn't count last one(here index -1)) -- here prints ner
#print(course[0:])# printing from index 0 to end of string -- here all of string
#print(course[3:])# printing from index 3 to end of string -- here prints "hon for Beginners"
#print(course[:5])# printing from index 0 to index 4  -- here prints Pytho
#another = course[2:12] # saving part of string in another variable
#print(another)
#name = "Jennifer"
#print(name[1:-1]) #here prints ennife

# Formatted Stings -- it's ideal for generating text from vars
#first = "John"
#last = "Smith"
#message = first + " [" + last + "] is a coder" # this message is our goal but it's still in normal mode
#print(message)
#msg = f"{first} [{last}] is a coder" # our formatted string
#print(msg)

# String Methods
#course = "Python for Beginners"
#print(len(course)) # len counts mount of characters
#print(course.upper()) # all chars will be in upper mode
#print(course.lower())  # all chars will be in lower mode
#print(course.find("P")) # it returns index of given char -- here is 0
#print(course.find("Beginners")) # it returns index of first char of given word(the word can be uncompleted like "Begi") -- here is 11
#print(course.replace("o", "ii")) # it replaces our char with given char
#print(course.replace("Beginners", "profis")) # it replaces our word with given word
#print("for" in course) # to check if there is a word or some chars in our string -- answer True/False
#print(course.title()) # it changes every first char of all word in upper mode

# Arithmetic Operations
#print(3 + 5) # addition operator
#print(3 - 5) # subtraction operator
#print(3 * 5) # multiplication operator
#print(10 / 3) # division operator in float mode -- it returns 3.33333333
#print(10 // 3) # division operator in integer mode -- it returns 3
#print(10 ** 3) # power operator
#print(10 % 3) # remainder of the division operator
#x = 10
#x = x + 3
#x += 3
#print(x)

# Math Functions (for complete info see https://docs.python.org/3/library/math.html)
#import math
#x = 2.7
#print(round(x)) # round our float to an integer ( .5 rounds it down and .6 rounds it up)
#print(abs(-14.3)) # absolut value returns just positive value -- here 14.3
#y = math.ceil(x) # math.ciel round it up even if it's 2.0001 -- here 3
#print(y)
#print(math.floor(x)) # math.floor round it down even if it's 2.999 -- here 2

# If Statements
#is_warm = False
#is_cold = False
#warm_msg = '''It is a hot day.
#Drink plenty of water.'''
#cold_msg = """It is a cold day.
#Wear warm clothes"""
#ok_msg = """It is a lovely day.
#Enjoy your day."""
#if is_warm:
#    print(warm_msg)
#elif is_cold:
#    print(cold_msg)
#else:
#    print(ok_msg)

# Logical Operators (and -- or -- not)
#has_high_income = True
#has_good_credit = True
#if has_high_income or has_good_credit:
#    print("Eligible for loan.")
#else:
#    print("can't get the loan.")
# another example
#has_good_credit = True
#has_criminal_record = False
#if has_good_credit and not has_criminal_record:
#    print("Eligible for loan.")
#else:
#    print("can't get the loan.")

# Comparison Operators
#temperature = int(input("Temperature: "))
#if temperature >= 30:
#    print("It's a hot day.")
#elif temperature <= 10:
#    print("It's a cold day.")
#else:
#    print("It's a cool day.")
# Example
#name = input("Name: ")
#if len(name) < 3:
#    print("Name must be at least 3 characters!")
#elif len(name) > 30:
#    print("Name can be a maximum of 30 characters!")
#else: print("Your name is: " + name)

# Project Weigh Conversion
#weigh = int(input("Weigh: "))
#w_mode = input("(L)bs or (K)g: ")
#if w_mode.upper() == "L":
#    w_kg = weigh * 0.45
#    print(f"You are {w_kg} kilos.")
#elif w_mode.upper() == "K":
#    w_lbs = weigh / 0.45
#    print(f"You are {w_lbs} pounds.")
#else:
#    print("Please give the correct character for conversion!!!")

# While Loops
#i = 1
#while i <= 5:
#    print("* " * i)
#    i += 1
#print("Done")
# Example
secret_num = 9
guess_count = 0
guess_limit = 3
#while guess_count < guess_limit:
#    guess = int(input("Guess: "))
#    guess_count +=1
#    if guess == secret_num:
#        print("You won!")
#        break
#else:
#    print("You failed; Try again!!!")

# Car Game
#command = ""
#started = False
#while command != "quit":
#    command = input("> ").lower()
#    if command == "start":
#        if started:
#            print("Car is already started.")
#        else:
#            started = True
#            print("Car started... ready to go...")
#    elif command == "stop":
#        if not started:
#            print("Car is already stopped.")
#        else:
#            started = False
#            print("Car stopped!")
#    elif command == "help":
#        print("""start - to start the cat
#stop  - to stop the car
#quit  - to exit
#        """)
#    elif command == "quit":
#        break
#    else:
#        print('please enter the correct command, or write "help".')

# For Loops
#for x in "Python":
#    print(x)
#for item in ["Mosh", "John", "Ali"]:
#    print(item)
#for num in [1,2,3,4,5]:
#    print(num)
#for x in range(10): # prints 0 to 9
#    print(x)
#for y in range(5,10):
#    print(y)
#for z in range(5,10,2): #here 2 is our jump -- prints 5 7 9
#    print(z)
# Example
#price = [10, 20, 30]
#s = 0
#for item in price:
#    s += item
#print(f"Total: {s}")

# Nested Loops
#for x in range(2):
#    for y in range(2):
#        for z in range(2):
#            print(f"({x} , {y} , {z})")

# Chanllenge
#numbers = [5,2,5,2,2]
#for x in numbers:
#    print("x" * x) #this line is the easy way -- next lines are for hard way but nested for way
#    out = ""
#    for y in range(x):
#        out += "x"
#    print(out)

# Lists
#name = ["Bob", "Mosh", "Ali", "Sara", "Jafar"]
#name[0] = "Jon" # modify an item in list
#print(name[1]) # prints Mosh
#print(name[-1]) # prints Jafar
#print(name[2:]) # prints ['Ali', 'Sara', 'Jafar']
#print(name[1:4]) # prints ['Mosh', 'Ali', 'Sara'] -- like strings 4 is not counted
#print(name[2:-1]) # prints ['Ali', 'Sara']
#print(name[:]) # prints all items
# Example : finding the largest number in a list
#numbs = [14, 5, 6, 12, 3, 18, 9]
#maxnum = numbs[0]
#for x in numbs:
#    if maxnum < x:
#        maxnum = x
#print(maxnum)

# 2D Lists
#matrix = [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9]
#]
#matrix[0][1] = 55 # modify an item
#print(matrix[0][2]) # prints 3
#print(matrix[1][0:2]) # prints [4, 5]
#print(matrix[2][-2]) # prints 8
#for row in matrix:
#    for item in row:
#        print(item) # prints every item from 1 to 9

# List Methods
#numbers = [5, 3, 2, 0, 6, 1, 5, 7, 4]
#numbers.append(20) # append to the end of list
#numbers.insert(2, 10) # insert the value 10 in index 2
#numbers.remove(1) # removes value 1
#numbers.clear() # removes all of list
#numbers.pop() # removes the last value
#print(numbers.index(1)) # returns the index of value 1
#print(5 in numbers) # check if there is the value in list - yes=True ,,, no=False
#print(numbers.count(5)) # returns the repetition of value 5 -- here we have value 5 twice, so it returns 2
#numbers.sort() # sort the list Ascending
#numbers.reverse() # make our list reverse -- with sort it shows revers sort (descending)
#number2 = numbers.copy() # make a copy of our list
# Exercise: remove the duplicates in a list
#numbers = [5, 3, 2, 0, 6, 1, 5, 7, 4, 4, 4]
#uniques = []
#for item in numbers:
#    if item not in uniques:
#        uniques.append(item)
#print(uniques)

# Toples : like lists but we can't modify it or mute it
#numbs = (1, 3, 2, 6) # in tuple we use parenthesis
#print(numbs[1]) # returns the value in index 1
#print(numbs.count(3)) # returns the count of value 3
#print(numbs.index(6)) # returns the index of value 6

# Unpacking
#numbs = (1, 2, 3) # no matter if it's a list or tuple
#x, y, z = numbs # unpacking our list in 3 variables
#print(x)
#print(y)
#print(z)

# Dictionaries
#customer = {
#    "name" : "John Smith",
#    "age" : 30,
#    "is_verified" : True
#}
#print(customer["name"])
#customer["name"] = "Jack Baily" # modify the name
#print(customer.get("name")) # same as first print without any error
#customer["birthdate"] = "Jan 1 1988" # adding a new key-value
#print(customer["birthdate"])
# Exercise : print digits in words
#digits = input("Digits: ")
#digits_mapping = {
#    "1" : "One",
#    "2" : "Two",
#    "3" : "Three",
#    "4" : "Four",
#    "5" : "Five"
#}
#output = ""
#for digit in digits:
#    print(digits_mapping[digit]) # this print mode returns errors for unknown digits
#    output += digits_mapping.get(digit, "!!") + " "
#print(output)

# Emoji Converter
#message = input("> ")
#words = message.split(' ') # make a list from our message string with space splitter
#emojies = {
#    ":)": "😊",
#    ":(": "😞"
#} # our imoji dictionary -- imoji in windows 10 --> (win + .)
#output = "" # empty string
#for word in words:
#    output += emojies.get(word, word) + " " # first word looks in dic and if there isn't any ting there, second word adds same word from list to output
#print(output)

# Functions
#def greet_user():
#    print("Hi there!")
#    print("Welcome aboard.")    # we define our function for printing 2 lines -- after defining functions we need 2 empty lines
#
#
#print("Start")
#greet_user() # using our func to print the greeting messages
#print("Finish")

# Parameters in Functions
#def greet_user(name):
#    print(f"Hi {name}!")
#    print("Welcome aboard.")    # we define our function with name parameter for printing greeting lines
#
#
#print("Start")
#greet_user("John") # using our func + parameter to print the greeting messages
#print("Finish")
# with 2 parameters
#def greet_user(name, last):
#    print(f"Hi {name} {last}!")
#    print("Welcome aboard.")    # we define our function with 2 parameters for printing greeting lines
#
#
#print("Start")
#greet_user("John", "Smith") # using our func + parameters to print the greeting messages
#print("Finish")

# Keyword Arguments
#def greet_user(name, last):
#    print(f"Hi {name} {last}!")
#    print("Welcome aboard.")    # we define our function with 2 parameters for printing greeting lines
#
#
#print("Start")
#greet_user(last="Smith", name="John") # using our func + keywords for positional parameters to print the greeting messages
#print("Finish")

# Return Statement
#def square(number):
#    return number*number
#
#
#numb = int(input('Please enter your number: ')) # get a number
#sqr = square(numb) # make a square of our number
#print("your number's square:", sqr)

# Creating a Reusable Function (we use our emoji dictionary and make it as a function)
#def emoji_converter(message):
#    words = message.split(' ') # make a list from our message string with space splitter
#    emojies = {
#        ":)": "😊",
#        ":(": "😞"
#    } # our imoji dictionary -- imoji in windows 10 --> (win + .)
#    output = "" # empty string
#    for word in words:
#        output += emojies.get(word, word) + " " # first word looks in dic and if there isn't any ting there, second word adds same word from list to output
#    return output
#
#
#msg = emoji_converter(input("> "))
#print(msg)

# Exeptions (don't let program crash and return an error that we wrote it)
#try:
#    age = int(input("Age: "))
#    income = 2000
#    risk = income/age
#    print(age)
#except ValueError:
#    print('Invalid Value!!!') # when user enter an invalid value like "abcd" or "21a"
#except ZeroDivisionError:
#    print("Age can not be Zero!!!") # because of division in risk variable if age is 0 then program will crash

# Comments
# We write comments to explain why

# Classes
#class Point: # we use classes to create types -- we define methodes and functions in classes
#    def move(self):
#        print("move")
#
#    def draw(self):
#        print("draw")
#
#
#point1 = Point() # make an object
#point1.x = 10  # make an object for class with atribute
#point1.y = 20
#print(point1.x)
#point1.draw()
#point1.move()
#
#point2 = Point() # make an other object with class that has nothing to do with first one
#point2.x = 15
#print(point2.x)

# Constructors
#class Point:
#    def __init__(self, x, y): # defining our cunstructor
#        self.x = x
#        self.y = y
#
#    def move(self):
#        print("move")
#
#    def draw(self):
#        print("draw")
#
#
#point1 = Point(10, 20)
#print(point1.y)
#print(point1.x)

# Exercise (a type named person with name attribute and talk method)
#class Person:
#    def __init__(self, name):
#        self.name = name
#    def talk(self):
#        print(f"Hi. I am {self.name}.")
#
#
#john = Person("John Smith")
#john.talk()
#bob = Person("Bob Davis")
#bob.talk()

# Inheritance 03:14:52
#class Mammal: # our main class or parent class
#    def walk(self):
#        print("walk")
#
#
#class Dog(Mammal): # inherits all methods in parent class
#    def bark(self):
#        print("bark")
#
#
#class Cat(Mammal):
#    pass        # it's doing nothing just to avoid empty class warnings
#
#
#dog1 = Dog()
#dog1.walk()
#dog1.bark() # this bark method is available just for Dog class not Cat class
#cat1 = Cat()
#cat1.walk()

# Modules (for example we make a converters.py file and we write some codes there)
#import converters
#print(converters.lbs_to_kg(10))
#print(converters.kg_to_lbs(75))
#from converters import kg_to_lbs
#print(kg_to_lbs(40))

# Exercise finding max number in a list in utils module
#from utils import find_max
#numbers = [10, 2, 3, 1, 112, 6]
#mx = find_max(numbers)
#print(mx) # in python there is a build-in function named max does the same job as our function in module -- print(max(numbers))

# Packages 3:30:25


