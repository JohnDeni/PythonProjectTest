from printer import BasePrinter, BlackAndWhitePrinter, ColorPrinter
from receipt import Receipt


receipt = Receipt("АТБ")
receipt.tax_percent = 10

receipt.add_product("Хліб", 25)
receipt.add_product("Молоко", 40)
receipt.add_product("Пиво", 64)

printer: BasePrinter = BlackAndWhitePrinter()
printer.print_receipt(receipt)

printer: BasePrinter = ColorPrinter()
printer.print_receipt(receipt)
