
class Product:

    def __init__(self, name, price, quantity):
        if name == "":
            raise ValueError("Product name can't be empty")
        self.name = name
        if price < 0 :
            raise ValueError("Product price can't be negative")
        self.price = price
        if quantity < 0:
            raise ValueError("Product Quantity can't be negative")
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


class NonStockedProducts(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def buy(self, quantity):
        if quantity < 0:
            raise ValueError("Product Quantity can't be negative")

        # Da es nicht gelagert wird, entfällt die Bestandsprüfung und -reduzierung.
        return quantity * self.price

    def show(self):
        super().show()
        print("   [Special Feature: Non-Stocked / Digital Product - Unlimited Availability]")


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, max_limit):
        super().__init__(name, price, quantity)
        if max_limit < 0:
            raise ValueError("Max limit can't be negative")
        self.max_limit = max_limit

    def buy(self, quantity):
        if quantity > self.max_limit:
            raise ValueError(f"Error! This is a limited product. Max allowed per order: {self.max_limit}")

        return super().buy(quantity)

    def show(self):
        super().show()
        print(f"   [Special Feature: Limited Product - Maximum {self.max_limit} units per order]")

