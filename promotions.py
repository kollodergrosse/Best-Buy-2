from abc import ABC, abstractmethod


class Promotion(ABC):
    """
    Abstract base class representing a promotional offer for products.
    All specific promotion types must inherit from this class and implement
    the apply_promotion method.
    """

    def __init__(self, name):
        """
        Initialize the promotion with a descriptive name.
        Args:
            name (str): The name of the promotion (e.g., "Summer Sale").
        """
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """
        Calculate the total price of a product order after applying the promotion.
        Args:
            product (Product): The product instance being purchased.
            quantity (int): The number of units being ordered.
        Returns:
            float: The total discounted price for the specified quantity.
        """
        pass


class PercentDiscount(Promotion):
    """
    A promotion that applies a fixed percentage discount to the total price.
    """

    def __init__(self, name, percentage):
        """
        Initialize the percentage discount promotion.
        Args:
            name (str): The name of the promotion.
            percentage (float): The discount percentage (must be between 0 and 100).
        Raises:
            ValueError: If the percentage is less than 0 or greater than 100.
        """
        super().__init__(name)
        if not (0 <= percentage <= 100):
            raise ValueError("Percentage must be between 0 and 100")
        self.percentage = percentage

    def apply_promotion(self, product, quantity):
        """
        Apply the percentage discount to the total order price.
        Args:
            product (Product): The product instance being purchased.
            quantity (int): The number of units being ordered.
        Returns:
            float: The total price after the percentage discount is deducted.
        """
        total_price = product.price * quantity
        discount = total_price * (self.percentage / 100)
        return total_price - discount


class SecondHalfPrice(Promotion):
    """
    A promotion where every second item of the same type is sold at half price.
    """

    def apply_promotion(self, product, quantity):
        """
        Calculate the price where every even-numbered item receives a 50% discount.
        Args:
            product (Product): The product instance being purchased.
            quantity (int): The number of units being ordered.
        Returns:
            float: The total price calculated with every second item at half price.
        """
        half_price_items = quantity // 2
        full_price_items = quantity - half_price_items
        return (full_price_items * product.price) + (half_price_items * product.price * 0.5)


class ThirdOneFree(Promotion):
    """
    A "Buy 2, Get 1 Free" promotion where every third item is completely free.
    """

    def apply_promotion(self, product, quantity):
        """
        Calculate the price by making every third item free of charge.
        Args:
            product (Product): The product instance being purchased.
            quantity (int): The number of units being ordered.
        Returns:
            float: The total price for the items, excluding the free ones.
        """
        free_items = quantity // 3
        payable_items = quantity - free_items
        return payable_items * product.price