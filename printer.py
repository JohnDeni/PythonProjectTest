
from abc import ABC, abstractmethod

from receipt import Receipt


class BasePrinter(ABC):
    @abstractmethod
    def print_receipt(self, receipt: Receipt) -> None:
        pass

class BlackAndWhitePrinter(BasePrinter):
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

class ColorPrinter(BasePrinter):
    RED = "\033[91m"
    GREEN = "\033[92m"
    RESET = "\033[0m"

    def print_receipt(self, receipt: Receipt) -> None:
        print(self.GREEN + "------ RECEIPT ------" + self.RESET)
        print(f"Store: {receipt.store_name}")
        print()

        if not receipt.products:
            print(self.RED + "Чек порожній" + self.RESET)
            print("---------------------")
            return

        for product in receipt.products:
            print(f'{product["name"]:<15} {product["price"]:>7.2f} грн')

        print()

        print(f"Subtotal: {receipt.subtotal:.2f} грн")
        print(self.RED + f"Tax ({receipt.tax_percent}%): {receipt.tax:.2f} грн" + self.RESET)
        print(self.GREEN + f"Total: {receipt.total:.2f} грн" + self.RESET)
        print("---------------------")
