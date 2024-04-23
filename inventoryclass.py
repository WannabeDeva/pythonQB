class Inventory:
    def __init__(self):
        self.item_details = {}

    def add_item(self, item_id, item_name, stock_count, price):
        self.item_details[item_id] = {'item_name': item_name, 'stock_count': stock_count, 'price': price}

    def update_item(self, item_id, item_name=None, stock_count=None, price=None):
        if item_id in self.item_details:
            if item_name is not None:
                self.item_details[item_id]['item_name'] = item_name
            if stock_count is not None:
                self.item_details[item_id]['stock_count'] = stock_count
            if price is not None:
                self.item_details[item_id]['price'] = price
            print("Item details updated successfully.")
        else:
            print("Item ID not found.")

    def check_item_details(self, item_id):
        if item_id in self.item_details:
            return self.item_details[item_id]
        else:
            return None

# Example usage:
inventory = Inventory()

# Add items to the inventory
inventory.add_item(1, 'Apple', 50, 2.5)
inventory.add_item(2, 'Banana', 40, 1.8)
inventory.add_item(3, 'Orange', 60, 3.0)

# Update item details
inventory.update_item(2, stock_count=50, price=2.0)
inventory.update_item(4)  # Item ID not found

# Check item details
item_id = 1
item_details = inventory.check_item_details(item_id)
if item_details:
    print(f"Item details for item ID {item_id}: {item_details}")
else:
    print("Item ID not found.")
