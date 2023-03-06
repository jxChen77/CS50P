# # Object-coiented programming(OOP)
# name = input("Name: ")
# house = input("House: ")
# print(f"{name} from {house}")

# # create functions
# def main():
#     name = get_name()
#     house = get_house()
#     print(f"{name} from {house}")

# def get_name():
#     return input("Name: ")

# def get_house():
#     return input("House: ")

# if __name__ == "__main__":
#     main()

# # simplify our program by storing the student as a tuple
# def main():
#     name, house = get_student()
#     print(f"{name} from {house}")

# # return name and house
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return name, house

# if __name__ == "__main__":
#     main()


# # simplify our program by storing the student as a tuple
# def main():
#     student = get_student()
#     print(f"{student[0]} from {student[1]}")

# # return name and house
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return (name, house)

# if __name__ == "__main__":
#     main()

# # simplify our program by storing the student as a tuple
# def main():
#     student = get_student()
#     if student[0] == "Padma":
#         # we cannot change the values in tuple, it is immutable 
#         student[1] = "Ravenclaw"
#     print(f"{student[0]} from {student[1]}")

# # return name and house
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return name, house

# if __name__ == "__main__":
#     main()

# # simplify our program by storing the student as a tuple
# def main():
#     student = get_student()
#     if student[0] == "Padma":
#         # if you want to change the values, make it as list
#         student[1] = "Ravenclaw"
#     print(f"{student[0]} from {student[1]}")

# # return name and house
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return [name, house]

# if __name__ == "__main__":
#     main()


# # simplify our program by storing the student as a tuple
# def main():
#     student = get_student()
#     print(type(student),student)
#     print(f"{student['name']} from {student['house']}")

# # return dict
# def get_student():
#     student = {}
#     student['name'] = input("Name: ")
#     student['house'] = input("House: ")
#     return student

# if __name__ == "__main__":
#     main()

# # simplify our program by storing the student as a tuple
# def main():
#     student = get_student()
#     print(type(student),student)
#     print(f"{student['name']} from {student['house']}")

# # return dict
# # remove unneeded varible
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return {'name' : name, 'house' : house}

# if __name__ == "__main__":
#     main()

# # simplify our program by storing the student as a tuple
# def main():
#     student = get_student()
#     print(type(student),student)
#     # change the value in dict
#     if student['name'] == "Padma":
#         student['house'] = "Ravenclaw"
#     print(f"{student['name']} from {student['house']}")
#     print(type(student),student)

# # return dict
# # remove unneeded varible
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return {'name' : name, 'house' : house}

# if __name__ == "__main__":
#     main()

# # Classes
# class Student:
#     ...

# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")

# def get_student():
#     student = Student()
#     student.name = input("Name: ")
#     student.house = input("House: ")
#     return student

# if __name__ == "__main__":
#     main()

# # Classes
# class Student:
#     # method in class
#     def __init__(self, name, house):
#         self.name = name
#         self.house = house
        
# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     student = Student(name,house)
#     return student

# if __name__ == "__main__":
#     main()

# # Classes
# class Student:
#     # method in class
#     def __init__(self, name, house):
#         self.name = name
#         self.house = house
        
# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name,house)

# if __name__ == "__main__":
#     main()


class Student:
    # method in class
    def __init__(self, name, house, patronus):
        # write some error in class
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus
    
        # provides a means by which a student is returned when called
    def __str__(self):
        return f"{self.name} from {self.house}"
        
def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name,house,patronus)

if __name__ == "__main__":
    main()


