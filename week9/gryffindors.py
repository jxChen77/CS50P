# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
# ]
# gryffindors = []
# for student in students:
#     if student["house"] == "Gryffindor":
#         gryffindors.append(student["name"])
    
# for gryffindor in sorted(gryffindors):
#     print(gryffindor)

# # make it more elegently :
# # you can get a list you want in a single line
# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
# ]
# gryffindors = [student["name"] for student in students 
#                if student["house"] == "Gryffindor"]

    
# for gryffindor in sorted(gryffindors):
#     print(gryffindor)

# # filter
# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
# ]
# def is_gryffindor(s):
#     return s["house"] == "Gryffindor"

# gryffindors = filter(is_gryffindor,students)

# # key means sorted by key
# # lambad means just used here and only once, after using, it will be deleted
# for gryffindor in sorted(gryffindors, key = lambda s: s["house"]):
#     print(gryffindor["name"])


# # filter
# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
# ]

# gryffindors = filter(lambda s: s["house"] == "Gryffindor",students)

# # key means sorted by key
# # lambad means just used here and only once, after using, it will be deleted
# for gryffindor in sorted(gryffindors, key = lambda s: s["house"]):
#     print(gryffindor["name"])

# # Diction Comprehensions
# # same idea as list comprehensions
# students = ["Hermione", "Harry", "Ron"]

# gryffindors = []

# for student in students:
#     gryffindors.append({"name" : student, "house" : "Gryffindor"})
# # check the type
# print(type(gryffindors))
# print(gryffindors)

# # apply dictionary comprehensions:
# students = ["Hermione", "Harry", "Ron"]

# gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

# print(gryffindors)

# # even simplify
# students = ["Hermione", "Harry", "Ron"]

# gryffindors = {student: "Gryffindor" for student in students}
# print(type(gryffindors))
# print(gryffindors)

# # enumerate
# students = ["Hermione", "Harry", "Ron"]

# for i in range(len(students)):
#     print(i+1,students[i])

# # do the same thing by enumeration
# students = ["Hermione", "Harry", "Ron"]
# print(type(enumerate(students)))
# for i, student in enumerate(students):
#     print(i+1,student)