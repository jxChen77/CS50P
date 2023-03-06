# name = input("What is your name? ")
# print(f"hello, {name}")

# names:list = []
# for _ in range(3):
#     name = input("What is your name? ")
#     names.append(name)

# names:list = []
# # simplify the code
# for _ in range(3):
#     names.append(input("What is your name? "))

# for name in sorted(names):
#     print(f"hello, {name}")

# name = input("What is your name? ")
# # the program will rewrite the txt each time
# file = open("names.txt","w")
# file.write(name)
# file.close()

# name = input("What is your name? ")
# # avoid rewriting the txt each time
# # a means append
# file = open("names.txt","a")
# file.write(f"{name}\n")
# file.close()

# name = input("What is your name? ")
# # automate close the file
# with open("names.txt","a") as file:
#     file.write(f"{name}\n")

# with open("names.txt","r") as file:
#     lines = file.readlines()

# for line in lines:
#     print("hello,",line)

# with open("names.txt","r") as file:
#     lines = file.readlines()

# for line in lines:
#     # make it less ugly
#     # removing the extraneous line break
#     print("hello,",line.rstrip())

# # simplifies the code
# with open("names.txt", "r") as file:
#     for line in file:
#         print("hello,", line.rstrip())

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
        
# sort the names first and then print
for name in sorted(names):
    print(f"hello, {name}")

