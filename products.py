class Product:
    """
    Represents a standard physical product in the store inventory.
    Manages the core attributes of an item including its name, price, 
    available stock quantity, active status, and any active promotional offer.
    """

    def __init__(self, name, price, quantity):
        """
        Initialize a new Product instance with validation.
        Args:
            name (str): The name of the product. Cannot be empty.
            price (float): The unit price of the product. Cannot be negative.
            quantity (int): The initial stock quantity. Cannot be negative.
        Raises:
            ValueError: If the name is empty, or if price/quantity are negative.
        """
        if name == "":
            raise ValueError("Product name can't be empty")
        self.name = name
        if price < 0:
            raise ValueError("Product price can't be negative")
        self.price = price
        if quantity < 0:
            raise ValueError("Product Quantity can't be negative")
        self.quantity = quantity
        self.active = True
        self.promotion = None

    def get_promotion(self):
        """
        Get the promotion currently assigned to the product.
        Returns:
            Promotion or None: The active promotion instance, or None if no promotion is set.
        """
        return self.promotion

    def set_promotion(self, promotion):
        """
        Assign a new promotional campaign to the product.
        Args:
            promotion (Promotion): The promotion instance to apply.
        """
        self.promotion = promotion

    def get_quantity(self):
        """
        Get the current stock level of the product.
        Returns:
            int: The current available quantity.
        """
        return self.quantity

    def set_quantity(self, quantity):
        """
        Update the stock quantity of the product.
        Automatically deactivates the product if the stock level hits zero.
        Args:
            quantity (int): The new stock level. Cannot be negative.
        Raises:
            ValueError: If the quantity provided is negative.
        """
        if quantity < 0:
            raise ValueError("Product quantity can't be negative")
        self.quantity = quantity
        if self.get_quantity() == 0:
            self.active = False

    def is_active(self):
        """
        Check if the product is currently available for purchase.
        Returns:
            bool: True if the product is active, False otherwise.
        """
        return self.active

    def activate(self):
        """Change the product's status to active."""
        self.active = True

    def deactivate(self):
        """Change the product's status to inactive."""
        self.active = False

    def show(self):
        """Print the primary details of the product including any active promotions."""
        promo_info = f", Promotion: {self.promotion.name}" if self.promotion else ""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}{promo_info}")

    def buy(self, quantity):
        """
        Process a purchase for a specific quantity of the product.
        Reduces stock and calculates the final total price, applying 
        any active promotions if they exist.
        Args:
            quantity (int): The number of items to purchase. Must be positive.
        Returns:
            float: The calculated total price for this purchase.
        Raises:
            ValueError: If quantity is negative or exceeds available stock.
        """
        if quantity < 0:
            raise ValueError("Product Quantity can't be negative")

        if quantity <= self.get_quantity():
            if self.promotion:
                total = self.promotion.apply_promotion(self, quantity)
            else:
                total = quantity * self.price

            self.set_quantity((self.get_quantity() - quantity))
        else:
            raise ValueError("Error! Quantity is too large")

        return total


class NonStockedProduct(Product):
    """
    Represents a digital or non-physical product (e.g., software license, service).
    Inherits from Product but bypasses physical stock inventory limitations.
    The quantity for these items is permanently set to zero.
    """

    def __init__(self, name, price):
        """
        Initialize a NonStockedProduct with a fixed initial quantity of 0.
        Args:
            name (str): The name of the digital product.
            price (float): The price of the digital product.
        """
        super().__init__(name, price, quantity=0)

    def buy(self, quantity):
        """
        Process the purchase of a digital product.

        Calculates the price directly without verifying or reducing
        physical inventory levels. Supports promotions.
        Args:
            quantity (int): The number of digital items/licenses to buy.
        Returns:
            float: The calculated total price after any promotion logic.
        Raises:
            ValueError: If the requested quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Product Quantity can't be negative")

        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        return quantity * self.price

    def show(self):
        """Print standard product details followed by its digital availability notice."""
        super().show()
        print("   [Special Feature: Non-Stocked / Digital Product - Unlimited Availability]")


class LimitedProduct(Product):
    """
    Represents a physical product with strict ordering constraints.
    Inherits from Product but introduces a maximum limit on how many
    units can be purchased within a single transaction.
    """

    def __init__(self, name, price, quantity, max_limit):
        """
        Initialize a LimitedProduct with an order restriction threshold.
        Args:
            name (str): The name of the limited product.
            price (float): The price of the product.
            quantity (int): The initial stock quantity available.
            max_limit (int): Maximum units allowed per order. Cannot be negative.
        Raises:
            ValueError: If max_limit is less than 0.
        """
        super().__init__(name, price, quantity)
        if max_limit < 0:
            raise ValueError("Max limit can't be negative")
        self.max_limit = max_limit

    def buy(self, quantity):
        """
        Process a purchase while enforcing the order quantity limit.
        Args:
            quantity (int): The number of items requested.
        Returns:
            float: The total price processed by the base purchase logic.
        Raises:
            ValueError: If the quantity requested exceeds the allowed limit.
        """
        if quantity > self.max_limit:
            raise ValueError(f"Error! This is a limited product. Max allowed per order: {self.max_limit}")

        return super().buy(quantity)

    def show(self):
        """Print standard product details followed by its purchase limit notice."""
        super().show()
        print(f"   [Special Feature: Limited Product - Maximum {self.max_limit} units per order]")