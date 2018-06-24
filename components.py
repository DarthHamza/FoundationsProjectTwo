class Store():
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def print_products(self):
        for product in self.products:
            print (product)


class Product():
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return "{} ({}) - {} KWD".format(self.name, self.description, self.price)


class Cart():
    def __init__(self):
        self.products = []

    def add_to_cart(self, product):
        self.products.append(product)

    def get_total_price(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

    def print_receipt(self):
        for product in self.products:
            print(product)
        print ("TOTAL: {}".fomrat(self.get_total_price()))

    def checkout(self):
        self.print_receipt()
        ans = input("Confirm order?(yes/no) ").lower()
        if ans == "yes" or ans == "y":
            print("Your order has been placed.")
        else:
            print("Your order has been cancelled.")
