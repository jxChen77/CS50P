# # constants
# # typically denoted by capital varible names and place at thr top of our code
# MEOWS = 3 # it is constant in this case
# for _ in range(MEOWS):
#     print("meows") 

# # an example in class
# class Cat:
#     MEOWS = 3

#     def meow(self):
#         for _ in range(Cat.MEOWS):
#             print("meow")

# cat = Cat()
# cat.meow()


# # Type Hints
# def meow(n):
#     for _ in range(n):
#         print("meow")
# # return string, but we need int
# number = input("Number: ")
# meow(number)

# install mypy to get some guidance to fix problems
# define your type of vatible first and you can get guidence from mypy
# def meow(n: int):
#     for _ in range(n):
#         print("meow")

# number: int = input("Number: ")
# meow(number)

# # we can fix the problem, and there is no issues by checking with mypy
# def meow(n: int):
#     for _ in range(n):
#         print("meow")

# number: int = int(input("Number: "))
# meow(number)

# # a new error 
# def meow(n: int):
#     for _ in range(n):
#         print("meow")

# number: int = int(input("Number: "))
# meows: str = meow(number)
# print(meows)

# # no return values
# def meow(n: int) -> None:
#     for _ in range(n):
#         print("meow")

# number: int = int(input("Number: "))
# meows: str = meow(number)
# print(meows)

# we can modify our code to return a string
def meow(n: int) -> str:
    return "meow\n" * n


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")