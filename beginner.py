            #strings

#  /n creates new line where the /n is
# concatonation     "hello " + "Josh" =  "hello Josh"


            #input 

# input("What is your name? ") -> allows for user input 

# print("Hello " + input("What is your name? ")) -> Hello "user input"

# print(len(input("whats your name")))

# city = input("What city did you grow up in")
# pet = input("whats the name of your first pet")

# print(city + ' ' + pet)


# string
# number
# float
# boolean

# type() return data type of input
# type("hello") -> string
# type(123) -> number

# round(8 / 3) -> 3


            # F string
# f"your score is {number}"
# print(f"your score is {4}")


# age = int(input("how old are you"))

# days = age * 365
# weeks = age * 52
# months = age * 12

# print(f"you are {days} days old, {weeks} weeks old, and {months} months old!")


            # Randomisation      must import random module

# import random  # can import other files and use variables and or functions in those files
# random_integer = random.randint(1, 10) # gives you random integer between 1 and 10 including those numbers
# random_float = random.random()
# print(random_float)



            # Loops 

fruits = ['apple', 'pear', 'banana']
# for fruit in fruits:
#     print(fruit)            # -> 'apple' 'pear' 'banana'


        # avg height

student_heights = [180, 124, 165, 173, 189, 169, 146]
def avg_height(heights):
    sum = 0
    for i in heights:
        sum += i
    return round(sum / len(heights))

# print(avg_height(student_heights))


        # max score

scores = [78, 65, 89, 86, 55, 91, 64, 89]

max(scores) # --> 91
min(scores) # --> 55

def max_score(scores):
    max = scores[0]
    for i in scores:
        if i > max:
            max = i 
    return max

# print(max_score(scores))

        # range
 
# for i in range(a, b, c)    a = starting number, b = stopping number not including that number, c = step size


        # adding evens

def adding_evens(num):
    sum = 0
    for i in range(2, num + 1, 2):
        sum += i 
    return sum


# print(adding_evens(100))


def fizzbuzz(num):
    for i in range(1, num + 1):
        if i % 15 == 0:
            print('fizzbuzz')
        elif i % 5 == 0:
            print('buzz')
        elif i % 3 == 0:
            print('fizz')
        else:
            print(i)

# fizzbuzz(50)


        # Password Generator

import random
letters = ['a', 'b', 'c', 'd', 'e']
numbers = ['1', '2', '3', '4', '5']
symbols = ['!', '@', '#', '$', '%']

nr_letters = int(input('How many letters?  '))
nr_numbers = int(input('How many Numbers?  '))
nr_symbols = int(input('How many symbols?  '))


# password = ""

# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)

# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)

# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)

# print(password)




password = []

for char in range(1, nr_letters + 1):
    password.append(random.choice(letters))

for char in range(1, nr_numbers + 1):
    password.append(random.choice(numbers))

for char in range(1, nr_symbols + 1):
    password.append(random.choice(symbols))

# print(password)
# random.shuffle(password)
# print(''.join(password))



            # While loops

# while something is true: do something

# goal is placed after 6 hurdles
number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
    print(number_of_hurdles)

# goal is placed after a random hurdle
while not at_goal:
    jump()