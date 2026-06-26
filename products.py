
class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self):
        """return the quantity of the product"""
        return self.quantity


    def set_quantity(self, quantity):
        """set the quantity of the product"""
        if quantity < 0:
            raise ValueError("Product quantity can't be negative")

        self.quantity = quantity

        if self.get_quantity() == 0:
            self.active = False


    def is_active(self):
        """check if the product is active"""
        if self.active:
            return True

        return False


    def activate(self):
        """activate the product"""
        self.active = True


    def deactivate(self):
        """deactivate the product"""
        self.active = False


    def show(self):
        """show the product with the details name, price and quantity"""
        print(f"{self.name}, {self.price}, {self.quantity}")


    def buy(self, quantity):
        """buys the product if it is active. returns the total price of the ordered product"""

        total = 0.0
        if quantity < 0:
            raise ValueError("Product Quantity can't be negative")

        if quantity <= self.get_quantity():
            total += quantity * self.price
            self.set_quantity((self.get_quantity() - quantity))

        else:
            raise ValueError("Error! Quantity is too large")

        return total
