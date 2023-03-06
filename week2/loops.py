# print("meow")
# print("meow")
# print("meow")
# # How about print meow over and over again

# # while loop
# i = 3
# while i != 0:
#     print("meow")
# # it never stop printing, use control-c on the keyboard to break out of the loop

# i = 3
# while i != 0:
#     print("meow", end = " ")
#     # check the i while exeucting the loop
#     print (f"i = {i}")
#     i = i-1

# i = 1
# while i <= 3:
#     print("meow", end = " ")
#     # check the i while exeucting the loop
#     print (f"i = {i}")
#     i = i + 1

# # begin i with 0
# i = 0
# while i < 3:
#     print("meow", end = " ")
#     # check the i while exeucting the loop
#     print (f"i = {i}")
#     i += 1

# # for loop
# for i in [0, 1, 2]:
#     print("meow", end = " ")
#     # check the i while exeucting the loop
#     print (f"i = {i}")

# # improve the code
# # use range 
# for i in range(3):
#     print("meow", end = " ")
#     # check the i while exeucting the loop
#     print (f"i = {i}")

# # i or _ does not matter
# for _ in range(3):
#     print("meow", end = " ")
#     # check the i while exeucting the loop
#     print (f"_ = {_}")

# print("meow" * 3)

# # edit it
# print("meow\n"*3,end="")

# # Improving with User Input
# # get n greater than or equal 0
# while True:
#     n = int(input("What is n? "))
#     if n < 0:
#         # continue to the next iteration of the loop
#         continue
#     else:
#         # break out of the loop
#         break

# while True:
#     n = int(input("What is n? "))
#     if n > 0:
#         # break out of this loop
#         break

# for _ in range(n):
#     print("meow")

# # use function to improve the code
# def main():
#     number = get_number()
#     meow(number)

# def get_number():
#     while True:
#         n = int(input("What is n? "))
#         if n > 0:
#             break
#     return n

# def meow(n):
#     for _ in range(n):
#         print("meow")

# main()

# # more about list
# students = ["Hermoine", "Harry", "Ron"]
# # begin with 0
# print(students[0])
# print(students[1])
# print(students[2])

# # use loop to iterate over the list
# students = ["Hermoine", "Harry", "Ron"]

# for student in students:
#     print(student)

# # length
# students = ["Hermoine", "Harry", "Ron"]

# # use len() to get the length of the list
# for i in range(len(students)):
#     print(i+1,students[i])

# Dictionaries
# it is another data structure, associated with key and value

# # could use list to accomplish this role
# students = ["Hermoine", "Harry", "Ron", "Draco"]
# houses = ["Gryffindor", "Gryffindor", "Griffindor", "Slytherin"]

# students = {
#     "Hermoine": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin",
# }
# print(students["Hermoine"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])

# # improve the code
# students = {
#     "Hermoine": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin",
# }
# for student in students:
#     print(student)
#     # only print the keys out

# students = {
#     "Hermoine": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin",
# }
# for student in students:
#     # print both keys and values
#     print(student,students[student])

# students = {
#     "Hermoine": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin",
# }
# for student in students:
#     # print both keys and values, and use separate
#     print(student,students[student],sep=", ")

# # put more data 
# # this code creates both list and dicts
# students = [
#     {"name": "Hermoine", "house": "Gryffindor", "patronus": "Otter"},
#     {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
#     {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
#     {"name": "Draco", "house": "Slytherin", "patronus": None},
# ]
# # iterate each dict inside the list
# for student in students:
#     print(student["name"],student["house"],student["patronus"],sep=", ")


# # Mario
# # create a txtual representation
# print("#")
# print("#")
# print("#")

# # better code
# for i in range(3):
#     print("#")

# def main():
#     print_column(3)

# def print_column(height):
#     for _ in range (height):
#         print("#")

# main()

# def main():
#     print_row(3)
# # try to print row horizontally
# def print_row(width):
#     print("?" * width)

# main()

# # implement both rows and columns
# def main():
#     print_square(3)

# def print_square(size):

#     # for each row in square
#     for i in range(size):
#         # for each brick in square
#         for j in range(size):

#             # print brick
#             print("#", end = "")
        
#         # print blank line
#         print()

# main()

# def main():
#     print_square(3)

# def print_square(size):
#     for i in range(size):
#         print_row(size)

# def print_row(size):
#     print("#" * size)
# main()