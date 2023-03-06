# import random

# class Hat:
#     def __init__(self):
#         self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

#     def sort(self, name):
#         print(name, "is in", random.choice(self.houses))

# hat = Hat()
# hat.sort("Harry")

# # name the sort function without __init__, and without creating a ins
# import random

# class Hat:
#     houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
#     @ classmethod
    #   # replace self with cls
#     def sort(cls, name):
#         print(name, "is in", random.choice(cls.houses))
# #use classmethod
# Hat.sort("Harry")

# class Student:
#     def __init__(self, name, house):
#         self.name = name
#         self.house = house
    
#     def __str__(self):
#         return f"{self.name} from {self.house}"
    
#     @classmethod
#     def get(cls):
#         name = input("Name: ")
#         house = input("House: ")
#         return cls(name,house)

# def main():
#     student = Student.get()
#     print(student)
#     print(type(student))

# if __name__ == "__main__":
#     main()

