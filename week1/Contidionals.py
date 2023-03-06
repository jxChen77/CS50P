# # Used to allow the program to make decisions. 
# # Give selections to the program
# # Such operators:  > < >= <= == !=
# x = int(input("What is X? "))
# y = int(input("What is Y? "))

# # control flow
# # execute the code only when after "if" is True
# # every condtions will be checked
# if x < y:
#     print("X is less than Y")
# if x > y:
#     print("X is greater than Y")
# if x == y:
#     print("X is equal to Y")

# #
# x = int(input("What is X? "))
# y = int(input("What is Y? "))

# # execute the code only when after "if" is True
# # not all condtions will be checked, from top to bottom, the check ends when one condition is correct
# if x < y:
#     print("X is less than Y")
# elif x > y:
#     print("X is greater than Y")
# elif x == y:
#     print("X is equal to Y")

# x = int(input("What is X? "))
# y = int(input("What is Y? "))

# # execute the code only when after "if" is True
# # not all condtions will be checked, from top to bottom, the flow ends when one condition is correct
# # catch all other conditions
# if x < y:
#     print("X is less than Y")
# elif x > y:
#     print("X is greater than Y")
# else:
#     print("X is equal to Y")

# # or
# x = int(input("What is x? "))
# y = int(input("What is y? "))

# # decrease the complexity
# if x < y or x > y:
#     print("X is not equal to Y")
# else:
#     print("X is equal to y.")

# x = int(input("What is x? "))
# y = int(input("What is y? "))
# if x != y:
#     print("X is not equal to Y")
# else:
#     print("X is equal to y.")

# x = int(input("What is x? "))
# y = int(input("What is y? "))
# if x == y:
#     print("X is equal to Y")
# else:
#     print("X is not equal to y.")

# # and 
# score = int(input("Score:"))

# # use and in condition
# if score >= 90 and score <=100:
#     print("Grade A")
# elif score >= 80 and score < 90:
#     print("Grade B")
# elif score >= 70 and score < 80:
#     print("Grade C")
# elif score >= 60 and score < 70:
#     print("Grade D")
# else:
#     print("Grade F")


# score = int(input("Score:"))

# # replace and
# if 90 <= score <=100:
#     print("Grade A")
# elif 80 <= score < 90:
#     print("Grade B")
# elif 70 <= score < 80:
#     print("Grade C")
# elif 60 <= score < 70:
#     print("Grade D")
# else:
#     print("Grade F")

# score = int(input("Score:"))

# # improve the program
# if 90 <= score:
#     print("Grade A")
# elif 80 <= score :
#     print("Grade B")
# elif 70 <= score :
#     print("Grade C")
# elif 60 <= score :
#     print("Grade D")
# else:
#     print("Grade F")

# modulo
# % get the remainder

# x = int(input("What is X? "))
# if x % 2 == 0:
#     print("X is even")
# else:
#     print("X is odd")

# # create a function to check if x is even
# def main():
#     x = int(input("What is X? "))
#     if is_even(x):
#         print("X is even")
#     else:
#         print("X is odd")

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
# main()

# # make the code more Pythonic
# def main():
#     x = int(input("What is X? "))
#     if is_even(x):
#         print("X is even")
#     else:
#         print("X is odd")

# def is_even(n):
#     # a short if else statement
#     # This is a unique way of coding only seen in Python.
#     return True if n % 2 == 0 else False
# main()

# # make the code more readable
# def main():
#     x = int(input("What is X? "))
#     if is_even(x):
#         print("X is even")
#     else:
#         print("X is odd")

# def is_even(n):
#     return n % 2 == 0 
# main()

# # match
# # match statements can be used to conditionally run code that matches certain values.

# name = input("What is your name? ")

# # use if elif statement to match the names
# if name == "Harry":
#     print("Gryffindor")
# elif name == "Hermione":
#     print("Gryffindor")
# elif name == "Ron":
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")

# # use or to improve the code

# name = input("What is your name? ")

# if name == "Harry" or name == "Hermione" or name == "Ron":
#     print("Geyffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")

# # Alternatively, uyse match statements
# name = input("What is your name? ")

# # match statements require python 3.10 or newer
# # But my version is 3.9.7, sorry
# match name:
#     case "Harry":
#         print("Gryffindor")
#     case "Hermione":
#         print("Gryffindor")
#     case "Ron":
#         print("Gryffindor")
#     case "Draco":
#         print("Slytherin")
#     case _:
#         print("Who?")