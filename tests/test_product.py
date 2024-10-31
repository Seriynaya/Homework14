import pytest

from src.product import Product
from tests.confitest import product1, product2, product3, product4

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


def test_product3(product3):
    assert product3.name == "Xiaomi Redmi Note 11"
    assert product3.description == "1024GB, Синий"
    assert product3.price == 31000.0
    assert product3.quantity == 14


def test_product4(product4):
    assert product4.name == "55 QLED 4K"
    assert product4.description == "Фоновая подсветка"
    assert product4.price == 123000.0
    assert product4.quantity == 7


def test_new_product():
    new_product.price = 0
    assert new_product.price == 180000
    new_product.price = 12000
    assert new_product.price == 12000


def test_new_product_1():
    name_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP " "камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    assert name_product.name == "Samsung Galaxy S23 Ultra"
    assert name_product.description == "256GB, Серый цвет, 200MP камера"
    assert name_product.price == 180000.0
    assert name_product.quantity == 5


def test_product_str(product1, product2, product3, product4):
    assert str(product1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert str(product2) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    assert str(product3) == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
    assert str(product4) == "55 QLED 4K, 123000.0 руб. Остаток: 7 шт."


def test_add_product(product2, product3):
    assert product2 + product3 == 2114000
    with pytest.raises(TypeError):
        product2 + 1


def test_add_product1(product1, product2):
    assert product1 + product2 == 2580000.0
    with pytest.raises(TypeError):
        product1 + 1


def test_product_price(product1, product2, product3, product4, capsys):
    product1.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    product1.price = 180000.0
    assert product1.price == 180000.0

    product2.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    product2.price = 210000.0
    assert product2.price == 210000.0

    product3.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    product3.price = 31000.0
    assert product3.price == 31000.0

    product4.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    product4.price = 123000.0
    assert product4.price == 123000.0
