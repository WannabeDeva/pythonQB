class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.booked_tables = []
        self.customer_orders = []

    def add_item_to_menu(self, item_name, price):
        self.menu_items[item_name] = price

    def book_table(self, table_number):
        self.booked_tables.append(table_number)

    def customer_order(self, table_number, items):
        order = {"table_number": table_number, "items": items}
        self.customer_orders.append(order)

    def print_menu(self):
        print("Menu:")
        for item, price in self.menu_items.items():
            print(f"{item}: ${price}")

    def print_table_reservations(self):
        print("Booked Tables:", self.booked_tables)

    def print_customer_orders(self):
        print("Customer Orders:")
        for order in self.customer_orders:
            print(f"Table {order['table_number']}: {order['items']}")

# Example usage:
restaurant = Restaurant()
restaurant.add_item_to_menu("Pizza", 10)
restaurant.add_item_to_menu("Burger", 8)
restaurant.add_item_to_menu("Salad", 6)

restaurant.book_table(1)
restaurant.book_table(2)

restaurant.customer_order(1, ["Pizza", "Burger"])
restaurant.customer_order(2, ["Salad"])

restaurant.print_menu()
print()
restaurant.print_table_reservations()
print()
restaurant.print_customer_orders()
