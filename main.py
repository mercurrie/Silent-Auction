import os
from art import logo

# ASCII art
print(logo)

end = False

# empty dict to store bids
auction = {}

while not end:
    # Retrieve bid and name
    name = input("What is your name: ")
    bid = int(input("What is your bid: $"))

    # store in dictionary
    auction[name] = bid
    
    # ask to repeat
    repeat = input("Is there another bidder? ")

    if repeat == "no":
        end = True
    
    # Clearing the Screen
    os.system('cls')

# calculate highest bidder
def highestBidder(auction):
    winner =  ""
    highest = 0
    
    for auctionee in auction:
        if auction[auctionee] > highest:
            winner = auctionee
            highest =auction[auctionee]
    print(f'The winner of the auction is {winner} with a bid of ${highest}')

highestBidder(auction)
        