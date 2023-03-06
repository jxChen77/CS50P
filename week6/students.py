# # store the data of csv in list
#     open("students.csv") as file:
#     for line in file:
#         row = line.rstrip().split(",")
#         print(f"{row[0]} is in {row[1]}")

# with open("students.csv","r") as file:
#     for line in file:
#         student , college = line.rstrip().split(",")
#         print(f"{student} is in {college}")

# students = []
# with open("students.csv","r") as file:
#     for line in file:
#         student , college = line.rstrip().split(",")
#         students.append(f"{student} is in {college}")

# for student in sorted(students):
#     print(student)

# students = []

# with open("students.csv","r") as file:
#     for line in file:
#         name , house = line.rstrip().split(",")
#         # create each dict
#         student = {}
#         student["name"] = name
#         student["house"] = house
#         students.append(student)

# print (students)
# for student in students:
#     print(f"{student['name']} is in {student['house']}")

# students = []

# with open("students.csv","r") as file:
#     for line in file:
#         name , house = line.rstrip().split(",")
#         # create each dict
        
#         students.append({"name" : name, "house" : house})

# def get_name(student):
#     return student["name"]

# # use key = ... as the standard to sort 
# for student in sorted(students, key = get_name):
#     print(f"{student['name']} is in {student['house']}")

# students = []

# with open("students.csv","r") as file:
#     for line in file:
#         name , house = line.rstrip().split(",")
#         students.append({"name" : name, "house" : house})

# # use the function just once, you can simplify the code
# for student in sorted(students, key = lambda student : student['name']):
#     print(f"{student['name']} is in {student['house']}")

# # test if we change the csv file
# # and there is ValueError
# students = []

# with open("students_1.csv","r") as file:
#     for line in file:
#         name , house = line.rstrip().split(",")
#         students.append({"name" : name, "house" : house})


# for student in sorted(students, key = lambda student : student['name']):
#     print(f"{student['name']} is in {student['house']}")

# # let's use csv library to read csv file
# import csv

# students = []

# with open("students_1.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({'name' : row['name'], 'home' : row['home']})

# for student in sorted(students, key = lambda student : student['name']):
#     print(f"{student['name']} is in {student['home']}")

# # I have no idea that  i cannot ues re students.csv, but use del students.csv
# import csv

# name = input("What's your name? ")
# home = input("Where's your home? ")
# # write the data into the file
# with open("students_1.csv","a") as file:
#     writer = csv.DictWriter(file, fieldnames=["name", "home"])
#     writer.writerow({"name": name, "home": home})