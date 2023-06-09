import os

bids = {}
bidding_finished = False

def highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")

while not bidding_finished:
    name = input("What's your name?: ")
    price = int(input("What is your bid?: $"))

    bids[name] = price

    cont = input("Are there any other bidders? Type 'yes' or 'no': ")
    if cont == "no":
        bidding_finished = True
        highest_bidder(bids)
    elif cont == "yes":
        os.system('cls')
