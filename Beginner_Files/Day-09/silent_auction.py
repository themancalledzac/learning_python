from replit import clear
from silent_auction_art import logo
# HINT: You can call clear() to clear the output in the console.

print(logo)

bids = {}
bidding_finished = False

while not bidding_finished:
    name = input("What is your name? ")
    price = input("What is your bid? $")
    bids[name] = price
    should_continue = input(
        "Are there any other bidders? Type 'yes' or 'no'. ")
    if should_continue == "no":
        bidding_finished = True

for bid in bids:
