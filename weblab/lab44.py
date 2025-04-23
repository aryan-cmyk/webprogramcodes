class Restaurant:
    def __init__(self):
        self.menu = {}
        self.tables = []
        self.orders = {}

    def add_menu_item(self, item, price):
        self.menu[item] = price

    def book_table(self, table_no):
        self.tables.append(table_no)

    def take_order(self, customer, items):
        self.orders[customer] = items

    def show_menu(self):
        print("Menu:")
        for item, price in self.menu.items():
            print(f"{item} - ₹{price}")

    def show_tables(self):
        print("Booked Tables:", self.tables)

    def show_orders(self):
        print("Orders:")
        for customer, items in self.orders.items():
            print(f"{customer} ordered: {items}")

# 🎯 Example
r = Restaurant()
r.add_menu_item("Pizza", 300)
r.add_menu_item("Pasta", 250)
r.book_table(5)
r.take_order("Aryan", ["Pizza", "Pasta"])
r.show_menu()
r.show_tables()
r.show_orders()
