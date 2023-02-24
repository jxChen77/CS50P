x = 1
y = 2

z = x + y

print(z)

# x, y are treated as strings
x = input("What is x? ")
y = input("What is y? ")

# Return 12
z = x + y

print(z)

x = input("What is x? ")
y = input("What is y? ")

# convert the type of the data 
z = int(x) + int(y)

print(z)

# More efficient 
# The most inner function runs first
x = int(input("What is x? "))
y = int(input("What is y? "))

print(x + y)

x = float(input("What is X? "))
y = float(input("What is Y? "))

print(x + y)

# Get the user's input
x = float(input("What is X? "))
y = float(input("What is Y? "))

# Create a rounded result
z = round((x + y),2)

# Print the result
print(z)

# See 1,000 instead 1000
x = float(input("What is X? "))
y = float(input("What is Y? "))

# Create a rounded result
z = round((x + y))

# Print the result
print(f"{z:,}")

# More on Floats
# Get the user's input
x = float(input("What is X? "))
y = float(input("What is Y? "))

# calculate the result
z = x / y

# Print the result
print(z)

# use round
# Get the user's input
x = float(input("What is X? "))
y = float(input("What is Y? "))

# calculate the result
z = round(x / y, 2)

# use fstring
# Print the result
print(z)

# Get the user's input
x = float(input("What is X? "))
y = float(input("What is Y? "))

# calculate the result
z = x / y

# Print the result
print(f"{z:.2f}")