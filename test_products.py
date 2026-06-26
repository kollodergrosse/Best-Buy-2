import pytest

from products import Product


def test_create_normal_product():
    """Test, dass das Erstellen eines normalen Produkts funktioniert."""
    product = Product("MacBook Air M2", 1450, 100)

    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.active is True


def test_create_invalid_product_details():
    """Test, dass ungültige Details eine Ausnahme auslösen."""
    # Test 1: Leerer Name
    with pytest.raises(ValueError):
        Product("", 1450, 100)

    # Test 2: Negativer Preis
    with pytest.raises(ValueError):
        Product("MacBook Air", -10, 100)


def test_quantity_zero_becomes_inactive():
    """Test, dass ein Produkt inaktiv wird, wenn die Menge 0 erreicht."""
    product = Product("Google Pixel 7", 500, 10)

    product.buy(10)

    assert product.quantity == 0
    assert product.active is False


def test_buy_updates_quantity_and_returns_price():
    """Test, dass der Produktkauf die Menge ändert und die richtige Ausgabe zurückgibt."""
    product = Product("Bose Earbuds", 250, 10)

    total_price = product.buy(3)

    assert product.quantity == 7
    assert total_price == 750


def test_buy_more_than_available_raises_exception():
    """Test, dass der Kauf einer größeren Menge als vorhanden eine Ausnahme auslösen."""
    product = Product("iPhone 15", 1000, 5)

    with pytest.raises(ValueError):
        product.buy(6)