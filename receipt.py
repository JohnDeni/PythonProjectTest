from product import Product


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