import pytest

from tests.confitest import product1, product2, product3, product4
from src.product import Product

new_product = Product.new_product(
    {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
)

def test_product1(product1):
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5


def test_product2(product1):
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5


def test_new_product():
    new_product.price = 0
    assert new_product.price == 180000
    new_product.price = 12000
    assert new_product.price == 12000

def test_product_str(product1, product2, product3, product4):
    assert str(product1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert str(product2) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    assert str(product3) == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
    assert str(product4) == "55 QLED 4K, 123000.0 руб. Остаток: 7 шт."

def test_add_product(product2, product3):
    assert product2 + product3 == 2114000
    with pytest.raises(TypeError):
        product2 + 1
