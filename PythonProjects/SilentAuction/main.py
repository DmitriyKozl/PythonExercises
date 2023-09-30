import os
from SilentAuction import art

print(art.logo)
bidder_dictionary = {}
bidding = True
winner = ""
while bidding:
    print("Welcome to the secret auction program.")
    name = input("what is your name?")
    bidder_dictionary[name] = input("What's your bid?: $")
    etra = input("Are there any other bidders? Type 'yes' or 'no'.")
    if etra == 'no':
        winner = max(bidder_dictionary, key=bidder_dictionary.get)
        bidding = False
    os.system('cls')


print(f"The winner is {winner} with a bid of ${bidder_dictionary[winner]}")
