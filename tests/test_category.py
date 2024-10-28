import pytest

from src.category import Category
from src.product import Product
from tests.confitest import (
    category1,
    category2,
    category_grass,
    category_smartphones,
    grass1,
    grass2,
    product1,
    product2,
    product3,
    product4,
    smartphone1,
    smartphone2,
    smartphone3,
)


new_product = Product.new_product(
    {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
)


def test_category1(category1, product4):
    assert category1.name == "Телевизоры"
    assert (
        category1.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert (
        category1.products
        == f"{product4.name}, {product4.price} руб. Остаток: {product4.quantity} шт.\n"
    )


def test_category2(category2, product1, product2, product3):
    assert category2.name == "Смартфоны"
    assert (
        category2.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category2.products == (
        f"{product1.name}, {product1.price} руб. Остаток: {product1.quantity} шт.\n"
        f"{product2.name}, {product2.price} руб. Остаток: {product2.quantity} шт.\n"
        f"{product3.name}, {product3.price} руб. Остаток: {product3.quantity} шт.\n"
    )


def test_add_product(category2, product4):
    category2.add_product(product4)
    category2.add_product(new_product)
    assert Category.product_count == 9


def test_category_str(category2):
    assert str(category2) == "Смартфоны, количество продуктов: 27 шт."


def test_category_grass(category_grass, grass1, grass2):
    assert category_grass.name == "Газонная трава"
    assert category_grass.description == "Различные виды газонной травы"
    assert category_grass.products == (
        f"{grass1.name}, {grass1.price} руб. Остаток: {grass1.quantity} шт.\n"
        f"{grass2.name}, {grass2.price} руб. Остаток: {grass2.quantity} шт.\n"
    )


def test_category_smartphones(category_smartphones, smartphone1, smartphone2, smartphone3):
    assert category_smartphones.name == "Смартфоны"
    assert category_smartphones.description == "Высокотехнологичные смартфоны"
    assert category_smartphones.products == (
        f"{smartphone1.name}, {smartphone1.price} руб. Остаток: {smartphone1.quantity} шт.\n"
        f"{smartphone2.name}, {smartphone2.price} руб. Остаток: {smartphone2.quantity} шт.\n"
        f"{smartphone3.name}, {smartphone3.price} руб. Остаток: {smartphone3.quantity} шт.\n"
    )
