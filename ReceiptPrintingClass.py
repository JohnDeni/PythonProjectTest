from typing import TypedDict

class Product(TypedDict):
    name: str
    price: float

class Receipt:

    def __init__(self, store_name: str, tax_percent: float) -> None:
        self.store_name = store_name
        self.tax_percent = tax_percent
        self._products: list[Product] = []

    def add_product(self, name: str, price: float) -> None:
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number")
        if price <= 0:
            raise ValueError("Price must be positive")

        self._products.append({"name": name, "price": float(price)})

    def show_products(self):
        print(self._products)

    def calculate_subtotal(self) -> float:

        return sum(product["price"] for product in self._products)

    def calculate_tax(self) -> float:

        subtotal = self.calculate_subtotal()
        tax_amount = subtotal * (self.tax_percent / 100)
        return round(tax_amount, 2)

    def __calculate_total(self) -> float:

        return self.calculate_subtotal() + self.calculate_tax()

    def print_receipt(self) -> None:
        print("------ RECEIPT ------")
        print("Store:", self.store_name)
        print()

        for product in self._products:
            print(f'{product["name"]:<10} {product["price"]:>5} грн')

        print()

        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax()
        total = self.__calculate_total()

        print("Subtotal:", subtotal, "грн")
        print(f"Tax ({self.tax_percent}%): {tax} грн")
        print("Total:", total, "грн")
        print("---------------------")


obj = Receipt("АТБ", 20)
obj.add_product("Хліб", 25)
obj.add_product("Молоко", 40)
obj.add_product("пиво", 64)
obj.show_products()
obj.print_receipt()
