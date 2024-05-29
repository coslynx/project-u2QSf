class Marketplace:
    def __init__(self):
        self.market_items = {}

    def add_item(self, item_name, price, seller):
        if item_name not in self.market_items:
            self.market_items[item_name] = {"price": price, "seller": seller}
            return f"{item_name} added to the marketplace."
        else:
            return f"{item_name} is already listed in the marketplace."

    def remove_item(self, item_name):
        if item_name in self.market_items:
            del self.market_items[item_name]
            return f"{item_name} removed from the marketplace."
        else:
            return f"{item_name} is not listed in the marketplace."

    def buy_item(self, item_name, buyer):
        if item_name in self.market_items:
            price = self.market_items[item_name]["price"]
            seller = self.market_items[item_name]["seller"]
            del self.market_items[item_name]
            return f"{buyer} bought {item_name} from {seller} for {price}."
        else:
            return f"{item_name} is not available in the marketplace."

    def view_marketplace(self):
        return self.market_items

# Instantiate the Marketplace class
marketplace = Marketplace()