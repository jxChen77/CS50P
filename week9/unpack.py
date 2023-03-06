# # divide the input into 2 varibles
# first, _ = input("What's your name? ").split(" ")
# print(f"hello, {first}")


# def total(galleons, sickles, kunts):
#     return (galleons * 17 + sickles) * 29 + kunts

# print(total(100, 50, 25), "Kunts")

# # store the varibles in a list
# def total(galleons, sickles, kunts):
#     return (galleons * 17 + sickles) * 29 + kunts

# coins = [100, 50, 25]
# print(total(coins[0], coins[1], coins[2]), "Kunts")

# # how about pass a entire list, we can use unpacking
# def total(galleons, sickles, kunts):
#     return (galleons * 17 + sickles) * 29 + kunts

# coins = [100, 50, 25]
# # notice that * unpacks the sequence of the list of coins and passes in total
# print(*coins)
# print(total(*coins), "Kunts")

# # pass the varibles by calling the names 
# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts

# print(total(galleons=100, sickles=50, knuts=25), "Knuts")


# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts
# # call them by dictionary
# coins = {"galleons": 100, "sickles": 50, "knuts": 25}
# print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts")

# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) * 29 + knuts
# # call them by dictionary
# coins = {"galleons": 100, "sickles": 50, "knuts": 25}
# # ** helps to unpack dictionary. When unpacking a dictionary, it provides both the keys and values.
# print(total(**coins), "Knut
