# AICP week 4 Tasks

class AuctionItem:
    def __init__(self, item_number, description, reserve_price):
        self.item_number = item_number
        self.description = description
        self.reserve_price = reserve_price
        self.number_of_bids = 0
        self.highest_bid = 0

class Auction:
    def __init__(self):
        self.items = []

    def setup_auction(self):
        # Task 1 - Auction set up
        # Add at least 10 items to the auction
        for i in range(1, 11):
            item_number = input(f"Enter item {i} number: ")
            description = input(f"Enter item {i} description: ")
            reserve_price = float(input(f"Enter item {i} reserve price: $"))
            item = AuctionItem(item_number, description, reserve_price)
            self.items.append(item)

    def display_items(self):
        # Display all items with their details
        for item in self.items:
            print(f"Item {item.item_number}: {item.description}, Reserve Price: ${item.reserve_price}")

    def bid(self):
        # Task 2 - Buyer bids
        item_number = input("Enter the item number you want to bid for: ")
        buyer_number = input("Enter your buyer number: ")
        bid_amount = float(input("Enter your bid amount: $"))

        for item in self.items:
            if item.item_number == item_number:
                if bid_amount > item.highest_bid:
                    item.highest_bid = bid_amount
                    item.number_of_bids += 1
                    print(f"Bid accepted for Item {item_number} by Buyer {buyer_number}")
                else:
                    print(f"Your bid of ${bid_amount} is not higher than the current highest bid.")
                return

        print(f"Item {item_number} not found in the auction.")

    def end_auction(self):
        # Task 3 - At the end of the auction
        total_fee = 0
        items_sold = 0
        items_not_meeting_reserve = 0
        items_with_no_bids = 0

        for item in self.items:
            if item.highest_bid >= item.reserve_price:
                total_fee += 0.1 * item.highest_bid
                items_sold += 1
                print(f"Item {item.item_number} sold for ${item.highest_bid} (Auction Company Fee: ${0.1 * item.highest_bid})")
            else:
                items_not_meeting_reserve += 1
                print(f"Item {item.item_number} did not meet reserve price. Highest bid: ${item.highest_bid}")

            if item.number_of_bids == 0:
                items_with_no_bids += 1
                print(f"Item {item.item_number} received no bids.")

        print(f"\nTotal Auction Company Fee: ${total_fee}")
        print(f"Items Sold: {items_sold}\nItems not meeting reserve: {items_not_meeting_reserve}\nItems with no bids: {items_with_no_bids}")

def main():
    print("An interactive Auction Board!")
    auction = Auction()
    auction.setup_auction()
    auction.display_items()

    # Simulate buyer bids
    auction.bid()
    auction.bid()

    # End the auction and display results
    auction.end_auction()

if __name__ == "__main__":
    main()


