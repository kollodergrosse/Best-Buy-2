from products import Product


class Store:
    def __init__(self, product_list):
        self.products = product_list


    def add_product(self, product):
        """adds a new product to the store"""
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
        """removes a product from the store"""
        if isinstance(product, Product):
            if product in self.products:
                self.products.remove(product)

            else:
                raise Exception(f"'{product.name}' does not exist!")

        else:
            raise ValueError(f"'{product.name}' is not of Type Product")



    def get_total_quantity(self):
        """returns the total quantity of the store"""
        total = 0
        for product in self.products:
            quantity = product.get_quantity()
            total += quantity

        return total


    def get_all_products(self):
        """returns all products from the store"""
        all_products = []
        for product in self.products:
            if product.is_active():
                all_products.append(product)

        return all_products


    def order(self, shopping_list):
        """gets the shopping list and uses buy method to order get the price of the pruducts. returns total price"""
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

