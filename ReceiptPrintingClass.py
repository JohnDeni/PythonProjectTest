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

    @property
    def products(self) -> list[Product]:
        return self._products.copy()

    def calculate_subtotal(self) -> float:
        return sum(product["price"] for product in self._products)

    def calculate_tax(self) -> float:
        subtotal = self.calculate_subtotal()
        return round(subtotal * (self.tax_percent / 100), 2)

    def calculate_total(self) -> float:
        return round(self.calculate_subtotal() + self.calculate_tax(), 2)


class Printer:
    def print_receipt(self, receipt: Receipt) -> None:
        print("------ RECEIPT ------")
        print(f"Store: {receipt.store_name}")
        print()

        if not receipt.products:
            print("Чек порожній")
            print("---------------------")
            return

        for product in receipt.products:
            print(f'{product["name"]:<15} {product["price"]:>7.2f} грн')

        print()

        subtotal = receipt.calculate_subtotal()
        tax = receipt.calculate_tax()
        total = receipt.calculate_total()

        print(f"Subtotal: {subtotal:.2f} грн")
        print(f"Tax ({receipt.tax_percent}%): {tax:.2f} грн")
        print(f"Total: {total:.2f} грн")
        print("---------------------")


receipt = Receipt("АТБ", 20)

receipt.add_product("Хліб", 25)
receipt.add_product("Молоко", 40)
receipt.add_product("Пиво", 64)

printer = Printer()
printer.print_receipt(receipt)
