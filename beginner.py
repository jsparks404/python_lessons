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

print(max_score(scores))