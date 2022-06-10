from art import logo
print(logo)

more_bidders = True
bids = {}

while more_bidders:
    name = input("What is your name? ")
    bid = int(input("what is your bid? $"))
    bids[name] = bid
    user_input = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if user_input == 'no':
        more_bidders = False

max_value = 0
max_value_name = ""
for name in bids:
    if bids[name] > max_value:
        max_value = bids[name]
        max_value_name = name
print(f"Person with highest bid is {name} with a bid of ${max_value}.")