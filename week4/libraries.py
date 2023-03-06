# # you can import libraries into your own project

# import random
# coin = random.choice(["heads", "tails"])
# print (coin)

# from random import choice
# coin = choice(["heads", "tails"])
# print(coin)

# import random
# # get random integer from 1 to 10
# number = random.randint(1, 10)
# print(number)

# import random

# cards = ["jack", "queen", "king"]
# # make list into a random order, no return
# random.shuffle(cards)
# for card in cards:
#     print(card)

# # Statistics
# import statistics
# print(statistics.mean([100,90]))

# # command-line arguments
# import sys
# try:
#     # at index 0 is the name of the python file
#     print("Hello, my name is", sys.argv[1])
# except IndexError:
#     print("Too few arguments.")

# # command-line arguments
# import sys

# if len(sys.argv) < 2:
#     print("Too few arguments.")
# elif len(sys.argv) > 2:
#     print("Too many arguments.")
# else:
#     print("Hello, my name is ", sys.argv[1])

# # command-line arguments
# import sys

# if len(sys.argv) < 2:
#     sys.exit("Too few arguments.")
# elif len(sys.argv) > 2:
#     # exit the program
#     sys.exit("Too many arguments.")

# print("Hello, my name is", sys.argv[1])

# import sys
# if len(sys.argv) < 2:
#     sys.exit("Too few arguments.")

# for arg in sys.argv:
#     # The name of the python file alse be output
#     print("hello, my name is",arg)

# import sys
# if len(sys.argv) < 2:
#     sys.exit("Too few arguments.")

# # avoid output the first in arguments
# for arg in sys.argv[1:]:
#     print("hello, my name is",arg)

# import cowsay
# import sys
# # test it, it is fun
# if len(sys.argv) == 2:
#     cowsay.cow("Hello," + sys.argv[1])

# import cowsay
# import sys
# # test it, it is fun
# if len(sys.argv) == 2:
#     cowsay.trex("Hello," + sys.argv[1])

