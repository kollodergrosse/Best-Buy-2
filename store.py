from products import Product


class Store:
    """
    Represents a store that manages an inventory of various products.
    Provides core management operations such as adding or removing products,
    tracking total stock quantities, querying active items, and processing
    customer purchase orders.
    """

    def __init__(self, product_list):
        """
        Initialize the Store with a predefined collection of products.
        Args:
            product_list (list): A list of Product instances to initialize
            the store inventory.
        """
        self.products = product_list


    def add_product(self, product):
        """
        Add a new product to the store or update stock if it already exists.
        If the product instance is entirely new, it is appended to the inventory.
        If a product with the same instance already exists, its quantity is combined
        with the current stock level.
        Args:
            product (Product): The product instance to add or update.
        Raises:
            ValueError: If the provided object is not a valid instance of Product.
        """
        if isinstance(product, Product):
            if product not in self.products:
                self.products.append(product)

            else:
                for existing_product in self.products:
                    if existing_product.name == product.name:
                        existing_product.set_quantity(
                            existing_product.get_quantity() + product.get_quantity())

        else:
            raise ValueError(f"'{product.name}' is not of Type Product")


    def remove_product(self, product):
        """
        Permanently remove a specific product instance from the store inventory.
        Args:
            product (Product): The product instance to remove.
        Raises:
            Exception: If the product instance cannot be found in the store.
            ValueError: If the provided object is not a valid instance of Product.
        """
        if isinstance(product, Product):
            if product in self.products:
                self.products.remove(product)

            else:
                raise Exception(f"'{product.name}' does not exist!")

        else:
            raise ValueError(f"'{product.name}' is not of Type Product")


    def get_total_quantity(self):
        """
        Calculate the total combined stock levels of all products in the store.
        Returns:
            int: The cumulative quantity sum of all inventory items.
        """
        total = 0
        for product in self.products:
            quantity = product.get_quantity()
            total += quantity

        return total


    def get_all_products(self):
        """
        Retrieve a list of all items currently active and available for sale.
        Returns:
            list[Product]: A list containing only the active Product instances.
        """
        all_products = []
        for product in self.products:
            if product.is_active():
                all_products.append(product)

        return all_products


    def order(self, shopping_list):
        """
        Process a multi-item purchase order and calculate the final total cost.
        Iterates through a list of product-quantity pairings, executes individual
        product transactions, and sums up the total price. Gracefully logs
        validation or type failures without disrupting the remaining shopping list items.
        Args:
            shopping_list (list[tuple]): A list of tuples where each element contains
                                         a (Product, quantity) pairing.
        Returns:
            float: The combined total price of all successfully ordered products.
        """
        total_price = 0.0
        try:
            for product, quantity in shopping_list:
                if isinstance(product, Product) and int(quantity) > 0:
                    total_price = total_price + product.buy(quantity)

        except TypeError as e:
            print("Type Error", e)

        except ValueError as v:
            print("Value Error", v)

        return total_price