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

# Chanllenge 1:51:30
#numbers = [5,2,5,2,2]
#for x in numbers:
#    print("x" * x) #this line is the easy way -- next lines are for hard way but nested for way
#    out = ""
#    for y in range(x):
#        out += "x"
#    print(out)

# Lists 1:56:00