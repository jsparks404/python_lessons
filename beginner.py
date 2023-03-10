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

import random  # can import other files and use variables and or functions in those files
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

# nr_letters = int(input('How many letters?  '))
# nr_numbers = int(input('How many Numbers?  '))
# nr_symbols = int(input('How many symbols?  '))


# password = ""

# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)

# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)

# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)

# print(password)




password = []

# for char in range(1, nr_letters + 1):
#     password.append(random.choice(letters))

# for char in range(1, nr_numbers + 1):
#     password.append(random.choice(numbers))

# for char in range(1, nr_symbols + 1):
#     password.append(random.choice(symbols))

# print(password)
# random.shuffle(password)
# print(''.join(password))



            # While loops

# while something is true: do something

# goal is placed after 6 hurdles
number_of_hurdles = 6
# while number_of_hurdles > 0:
#     jump()
#     number_of_hurdles -= 1
#     print(number_of_hurdles)

# # goal is placed after a random hurdle
# while not at_goal:
#     jump()


#     #Maze
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# # edge case to avoid infinite loop
# while front_is_clear():
#     move()
# turn_left()

# # moving through maze
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()






        # Hangman

# word_list = ['aardvark', 'baboon', 'camel']

# chosen_word = random.choice(word_list)   #chooses random word from word list
# print(f'The chosen word is {chosen_word}')

# display = []
# for letter in chosen_word:
#     display.append('_')
# print(display)

# guess = input('Guess a letter: ').lower() # takes user input and makes it lowercase



# for position in range(len(chosen_word)):   # sees if letter at index matches guess
#     letter = chosen_word[position]
#     if letter == guess:
#         display[position] = letter

# print(display)
# end_of_game = False
# lives = 6
# while not end_of_game:
#     guess = input('Guess a letter: ').lower()
#     for position in range(len(chosen_word)):
#         letter = chosen_word[position]
#         if letter == guess:
#             display[position] = letter
#     if guess not in chosen_word:
#         lives -= 1
#         print(lives)
#         if lives == 0:
#             end_of_game = True
#             print('Loser')
#     if '_' not in display:
#         end_of_game = True
#         print('Winner')
#     print(display)




        # Paint calculator
import math

# def paint_calc(height, width, cover):
#     area = height * width
#     num_cans = math.ceil(area / cover)
#     print(f"You'll need {num_cans} cans of paint")


# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height = test_h, width = test_w, cover = coverage)



        # Prim number checker



# def prime_number(num):
#     for i in range(2, math.ceil(num / 2)):
#         if num % i == 0:
#             return f"{num} is not a prime number"
#     else:
#         return f"{num} is a prime number"



# num = int(input("Check this number: "))
# print(prime_number(num))


# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message here:\n")
# shift = int(input("Type the shift number:\n"))
# shift = shift % 26
# def encrypt(text, shift):
#     cipher_text = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position + shift
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"the encoded text is {cipher_text}")
    

# def decrypt(cipher_text, shift):
#     original_text = ''
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift
#         new_letter = alphabet[new_position]
#         original_text += new_letter
#     print(f"the decoded text is {original_text}")



def caesar(text, shift, direction):
    end_text = ''
    if direction == 'decode':
            shift *= -1
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        new_letter = alphabet[new_position]
        end_text += new_letter
    print(f"The {direction}d text is {end_text}")


# caesar(text, shift, direction)





            # Dictionaries
        # Objects

pro_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    
}

    # accessing values like lists using bracket notation

# print(pro_dictionary["Bug"])

    # adding to dictionary
pro_dictionary["Loop"] = "The act of doing something over and over again."
# print(pro_dictionary)

empty_dict = {}   # can be added to later

    # Wipe existing dict by setting dictionary equal to {}
# pro_dictionary = {}

    # Edit item by setting key equal to different value
# pro_dictionary["Bug"] = "An insect in your computer"


    # Looping through dictionary
# for key in pro_dictionary:
#     print(key)    #just prints keys
#     print(pro_dictionary[key])   # prints key then value





scores = {
    "Harry": 81,
    "Ron": 78, 
    "Hermione": 99, 
    "Draco": 74,
    "Neville": 62,
}


grades = {}

for student in scores:
    score = scores[student]
    if score > 90:
        grades[student] = "Outstanding"
    elif score > 80:
        grades[student] = "Exceeds Expectations"
    elif score > 70:
        grades[student] = "Acceptable"
    else:
        grades[student] = "Fail"

# print(grades)




        # Nesting

travel_log = {
    "France": {
        "cities_visitied": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": ["Berlin", "Hamburg"]
}


travel_log2 = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg"],
        "total_visits": 5,
    }
]

def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["total_vistits"] = times_visited
    new_country["cities_visited"] = cities_visited
    travel_log2.append(new_country)

# add_new_country("Russia", 1, ["Moscow", "Sochi"])

# print(travel_log2)



        # Blind Auction
# bids = {}
# bidding_finished = False
# def highest_bidder(bidding_record):
#     highest_bid = 0
#     winner = ""
#     for bidder in bidding_record:
#        bid_amount = bidding_record[bidder]
#        if bid_amount > highest_bid:
#            highest_bid = bid_amount
#            winner = bidder
#     print(f"The winner is {winner} with the bid of ${highest_bid}")

# while not bidding_finished:
#     name = input("What is your name: ")
#     price = int(input("What is your bid: $"))
#     bids[name] = price
#     should_continue = input("Any other bidders? 'Yes' or 'no': ")
#     if should_continue == "no":
#         bidding_finished = True
#         highest_bidder(bids)
    






            # functions with outputs

# .title() returns string in title case -->  josh sparks = Josh Sparks



# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"

# print(format_name("josh", "sparks"))

        # multiple return values      can do with conditionals
    # docstrings --> strings to document   """ """  populates documentation when function is called.


def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"



            # Calculator

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add, 
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    num1 = int(input("What's the first number: "))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = int(input("What's the second number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or type 'n' start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

# calculator()





            # Blackjack


def deal_card():
    """returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    #check for blackjack
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # check if ace should be 11
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "DRAW"
    elif computer_score == 0:
        return "Lose, opponent has BlackJack"
    elif user_score == 0:
        return "Winner with BlackJack"
    elif user_score > 21:
        return "Loser busted"
    elif computer_score > 21:
        return "Winner, opponent busts"
    elif user_score > computer_score:
        return "Winner"
    else:
        return "Loser"

def play_game():
    user_cards = []
    computer_cards = []
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(user_cards, user_score)
        print(computer_cards[0])

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            hit_or_stay = input("Type 'y' to hit and 'n' to stay: ")
            if hit_or_stay == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(user_score, computer_score)
    print(compare(user_score, computer_score))

    while input("Do you want to play again? 'y' or 'n': ") == 'y':
        play_game()



# play_game()




            # Scope

# no such thing as block scope in python

        # modifying global variable, don't do often, prone to bugs

enemies = 1                 #globally scoped here

# def increase_enemies():
#     enemies = 2             #locally scoped here

# def increase_enemies():
#     global enemies              # global key word accesses globally scoped variable
#     enemies += 1


# def increase_enemies():
#     return enemeies += 1            # can instead return globally scoped variable change



PI = 3.14159265         # Global constant convention should be all capitalized


            # number guessing game high low


def game():
    number = random.randint(1, 100)
    attempts = 0
    in_play = True

    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == 'easy':
        attempts = 10
    else:
        attempts = 5

    while in_play:
        print(f"You have {attempts} attempts to guess the correct number")
        guess = int(input("Guess a number: "))
        if guess == number:
            print("You guessed the correct number!")
            in_play = False
        elif guess > number:
            print("Too high. Guess again")
            attempts -= 1
        elif guess < number:
            print("Too low. Guess again")
            attempts -= 1
        if attempts == 0:
            print("You ran out of attempts")
            in_play = False


# game()




            # Debugging

# Describe the problem
# Reproduce the bug
# Evaluate each line
# Read errors, watch for red underlines
# Use print() to find problems
# Use debugger
# Take a break
# Ask for help
# Run code often
# Google




