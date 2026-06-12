class Product:
    def __init__(self, name, price):
        """
        Initialize a Product instance.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
        """
        self.name = name
        self.price = price

    def get_price(self):
        """
        Get the price of the product.

        Returns:
            float: The price of the product.
        """
        return self.price
