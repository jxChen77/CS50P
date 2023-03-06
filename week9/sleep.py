# # Generators and Iterators
# n = int(input("What's n? "))
# for i in range(n):
#     print("🐑" * i)

# # make our code more sophisticated
# def main():
#     n = int(input("What's n? "))
#     for i in range(n+1):
#         print("🐑" * i)

# if __name__ == "__main__":
#     main()

# # make code partly 
# def main():
#     n = int(input("What's n? "))
#     for i in range(n):
#         print(sheep(i))

# def sheep(n):
#     return "🐑" * n+1

# if __name__ == "__main__":
#     main()

# # provide more abilities for sheep function
# # if the n is huge, our program may crash
# def main():
#     n = int(input("What's n? "))
#     for s in sheep(n):
#         print(s)

# def sheep(n):
#     flock = []
#     for i in range(n):
#         flock.append("🐑"*i)
#     return flock

# if __name__ == "__main__":
#     main()

# yield can solve this problem
def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "🐑" * i

if __name__ == "__main__":
    main()