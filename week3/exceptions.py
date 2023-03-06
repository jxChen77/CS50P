# # May errors exist in our program
# print("Hello, world!)
# # return SyntaxError

# Runtime errors
# x = int(input("What is x? "))
# print(f"x is {x}")

# # try
# # used to test user's input
# try:
#     x = int(input("What is x? "))
#     print(f"x is {x}")
# except ValueError:
#     print("x is not an integer")

# # after try, only one line of code is better
# try:
#     x = int(input("What's x?"))
# except ValueError:
#     print("x is not an integer")

# print(f"x is {x}")

# # if no except occurs, run the code after else:
# try:
#     x = int(input("What's x?"))
# except ValueError:
#     print("x is not an integer")
# else:
#     print(f"x is {x}")

# # we can simply use loop to prompt the user to input valid value
# while True:
#     try:
#         x = int(input("What is x? "))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         break
# print(f"x is {x}")

# # create a function to get an integer
# def main():
#     x = get_int()
#     print(f"x is {x}")

# def get_int():
#     while True:
#         try:
#             x = int(input("What is x? "))
#         except ValueError:
#             print("x is not an integer")
#         else:
#             break
#     return x
# main()

# # create a function to get an integer
# def main():
#     x = get_int()
#     print(f"x is {x}")

# def get_int():
#     while True:
#         try:
#             x = int(input("What is x? "))
#         except ValueError:
#             print("x is not an integer")
#         else:
#             return x
# main()

# # more effiecient
# def main():
#     x = get_int()
#     print(f"x is {x}")

# def get_int():
#     while True:
#         try:
#             return int(input("What is x? "))
#         except ValueError:
#             print("x is not an integer")
        
# main()

# # pass
# # does not warn user
# def main():
#     x = get_int()
#     print(f"x is {x}")


# def get_int():
#     while True:
#         try:
#             return int(input("What's x?"))
#         except ValueError:
#             pass

# main()

# # does not warn user
# def main():
#     x = get_int("What is x? ")
#     print(f"x is {x}")


# def get_int(prompt):
#     while True:
#         try:
#             return int(input(prompt))
#         except ValueError:
#             pass

# main()

