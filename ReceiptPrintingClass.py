from typing import TypedDict


class Product(TypedDict):
    name: str
    price: float


class Receipt:
    def __init__(self, store_name: str, tax_percent: float = 20) -> None:
        self.store_name = store_name
        self._tax_percent = tax_percent
        self._products: list[Product] = []

    @property
    def tax_percent(self) -> float:
        return self._tax_percent

    @tax_percent.setter
    def tax_percent(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Tax percent must be a number")
        if value < 0:
            raise ValueError("Tax percent cannot be negative")

        self._tax_percent = value

    def add_product(self, name: str, price: float) -> None:
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number")
        if price <= 0:
            raise ValueError("Price must be positive")

        self._products.append({"name": name, "price": float(price)})

    @property
    def products(self) -> list[Product]:
        return self._products

    @property
    def subtotal(self) -> float:
        return sum(product["price"] for product in self._products)

    @property
    def tax(self) -> float:
        return round(self.subtotal * (self._tax_percent / 100), 2)

    @property
    def total(self) -> float:
        return round(self.subtotal + self.tax, 2)


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

        print(f"Subtotal: {receipt.subtotal:.2f} грн")
        print(f"Tax ({receipt.tax_percent}%): {receipt.tax:.2f} грн")
        print(f"Total: {receipt.total:.2f} грн")
        print("---------------------")



receipt = Receipt("АТБ")
receipt.tax_percent = 10

receipt.add_product("Хліб", 25)
receipt.add_product("Молоко", 40)
receipt.add_product("Пиво", 64)

printer = Printer()
printer.print_receipt(receipt)
