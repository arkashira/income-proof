import pytest
from axentx_product.product import Product

def test_product_init():
    """
    Test the initialization of a Product instance.
    """
    product = Product("Test Product", 9.99)
    assert product.name == "Test Product"
    assert product.price == 9.99

def test_product_get_price():
    """
    Test the get_price method of a Product instance.
    """
    product = Product("Test Product", 9.99)
    assert product.get_price() == 9.99
