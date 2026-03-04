
class Receipt:

    def __init__(self, store_name, tax_percent):
        self.store_name = store_name
        self.tax_percent = tax_percent
        self.products = []

    def add_product(self, name, price):
        if price > 0:
            self.products.append({"name": name, "price": price})
        else:
            raise ValueError("Price is negative")

    def show_products(self):
        print(self.products)

    def calculate_subtotal(self):

        total = 0

        for product in self.products:
            total += product["price"]

        return total

    def calculate_tax(self):

        subtotal = self.calculate_subtotal()
        tax_amount = subtotal * (self.tax_percent / 100)
        return round(tax_amount, 2)

    def calculate_total(self):

        total = self.calculate_subtotal() + self.calculate_tax()

        return total

    def print_receipt(self):
        print("------ RECEIPT ------")
        print("Store:", self.store_name)
        print()

        for product in self.products:
            print(f'{product["name"]:<10} {product["price"]:>5} грн')

        print()

        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax()
        total = subtotal + tax

        print("Subtotal:", subtotal, "грн")
        print(f"Tax ({self.tax_percent}%):", round(tax, 2),"грн")
        print("Total:", total, "грн")
        print("---------------------")


obj = Receipt("АТБ", 20)
obj.add_product("Хліб", 25)
obj.add_product("Молоко", 40)
obj.add_product("пиво", 64)
obj.show_products()
obj.print_receipt()
