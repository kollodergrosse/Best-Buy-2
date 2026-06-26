import pytest
from products import Product


def test_create_normal_product():
    """Test that a product instance is created correctly with valid details."""
    product = Product("MacBook Air M2", 1450, 100)

    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.active is True


def test_create_invalid_product_details():
    """Test that initializing a product with invalid details raises a ValueError."""
    # Test 1: Empty name string
    with pytest.raises(ValueError):
        Product("", 1450, 100)

    # Test 2: Negative price value
    with pytest.raises(ValueError):
        Product("MacBook Air", -10, 100)


def test_quantity_zero_becomes_inactive():
    """Test that a product becomes automatically deactivated when its stock drops to zero."""
    product = Product("Google Pixel 7", 500, 10)

    product.buy(10)

    assert product.quantity == 0
    assert product.active is False


def test_buy_updates_quantity_and_returns_price():
    """Test that purchasing an item correctly reduces stock levels and returns the accurate total price."""
    product = Product("Bose Earbuds", 250, 10)

    total_price = product.buy(3)

    assert product.quantity == 7
    assert total_price == 750


def test_buy_more_than_available_raises_exception():
    """Test that attempting to buy more units than available in stock raises a ValueError."""
    product = Product("iPhone 15", 1000, 5)

    with pytest.raises(ValueError):
        product.buy(6)