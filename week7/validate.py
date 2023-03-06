# # if there is @, output validate
# email = input("What is your email address? ").strip()

# if "@" in email:
#     print('Vaild')
# else:
#     print('Invalid')

# # @. will also output validate
# email = input("What is your email address? ").strip()

# if "@" in email and '.' in email:
#     print('Vaild')
# else:
#     print('Invalid')

# # improve
# email = input("What is your email address? ").strip()

# username, domain = email.split('@')
# if username and '.' in domain:
#     print('Vaild')
# else:
#     print('Invalid')

# # improve
# email = input("What is your email address? ").strip()

# username, domain = email.split('@')
# if username and '.' in domain:
#     print('Vaild')
# else:
#     print('Invalid')


# # improve
# email = input("What is your email address? ").strip()

# username, domain = email.split('@')
# if username and domain.endswith('.edu'):
#     print('Vaild')
# else:
#     print('Invalid')

# # use library
# import re

# email = input("What is your email address? ").strip()

# if re.search('@',email):
#     print('Vaild')
# else:
#     print('Invalid')

# # The pattern expression
# # .   any character except a new line
# # *   0 or more repetitions
# # +   1 or more repetitions
# # ?   0 or 1 repetition
# # {m} m repetitions
# # {m,n} m-n repetitions
# import re

# email = input("What is your email address? ").strip()

# # .+ means that something 
# if re.search(".+@.+",email):
#     print("Valid")
# else:
#     print("Invalid")

# import re

# email = input("What is your email address: ").strip()

# if re.search(".+@.+\.edu",email):
#     print("Valid")
# else:
#     print("Invalid")

# import re

# email = input("What is your email address: ").strip()

# # raw string
# if re.search(r".+@.+\.edu",email):
#     print("Valid")
# else:
#     print("Invalid")


# ^   matches the start of the string
# $   matches the end of the string or just before the newline at the end of the string
import re

email = input("What is your email address: ").strip()

# modify our 
if re.search(r"^.+@.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")


# []    set of characters
# [^]   complementing the set
import re

email = input("What is your email address: ").strip()

# modify ours 
if re.search(r"^[^@]+@[^@]+\.edu$",email):
    print("Valid")
else:
    print("Invalid")




