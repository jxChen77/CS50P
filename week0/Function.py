# Def
def hello():
    print("Hello")

name = input("What's your name? ")
hello()
print(name)


def hello(to):
    print("Hello,",to)

name = input("What's your name? ")
hello(name)

def hello(to = 'world'):
    print("Hello, ",to)

name = input("What's your name? ")
hello(name)

# output without passing the expected arguments
hello()

def main():
    name = input("What's your name?")
    hello(name)

    hello()

def hello(to = 'world'):
    print("Hello, ", to)

main()

# Returning values
def main():
    x = int(input("What's x? "))
    print("x squared is ", square(x))


def square(n):
    # Pass the values back
    return n * n

main()