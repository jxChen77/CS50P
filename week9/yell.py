# # map
# def main():
#     yell("This is CS50")

# # convert to upper case
# def yell(word):
#     print(word.upper())

# if __name__ =="__main__":
#     main()


# def main():
#     yell(["This", "is", "CS50"])

# # use for loop to convert every elements to upper case
# def yell(words):
#     uppercased = []
#     for word in words:
#         uppercased.append(word.upper())
#     # use * to upace the list
#     print(*uppercased)

# if __name__ == "__main__":
#     main()

# # what will happen if we remove the brackets, but add * as args in yell
# def main():
#     yell("This", "is", "CS50")

# # use for loop to convert every elements to upper case
# def yell(*words):
#     uppercased = []
#     for word in words:
#         uppercased.append(word.upper())
#     # use * to upace the list
#     print(*uppercased)

# if __name__ == "__main__":
#     main()

# # map allows you to map a function to a sequence of values.
# def main():
#     yell("This", "is", "CS50")

# def yell(*words):
#     uppercased = map(str.upper,words)
#     # test what we will get after map
#     print(type(uppercased))
#     print(*uppercased)

# if __name__ == "__main__":
#     main()

# List Comprehensions 
# instead of using map
def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = [arg.upper() for arg in words]
    print(*uppercased)

if __name__ == "__main__":
    main()