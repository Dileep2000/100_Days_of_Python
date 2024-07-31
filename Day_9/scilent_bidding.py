import os


def highest_bidder(bids):
    name = ""
    max_bid = 0
    for bid in bids:
        if bids[bid] > max_bid:
            max_bid = bids[bid]
            name = bid
    return name


if __name__ == '__main__':
    bids = {}
    while True:
        print("""
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                      /_______________\\
    """)
        print("Welcome to secret acution program.")
        name = input("What is your name? ")
        bid = int(input("What's your bid?: $"))
        bids[name] = bid
        finish = input("Are there any other bidders? Type 'yes' or 'no'.\n")
        if finish.lower() == 'no':
            break
        os.system("cls")
    winner = highest_bidder(bids)
    print(f"The winner is {winner} with a bid of {bids[winner]}.")
