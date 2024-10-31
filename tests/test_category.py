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


def test_category(category1, category2):
    assert category2.name == "Смартфоны"
    assert (
        category2.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len([category2.products]) == 1

    assert category2.category_count == 2
    assert category1.category_count == 2

    assert category2.product_count == 4
    assert category1.product_count == 4


def test_category1(category1, product4):
    assert category1.name == "Телевизоры"
    assert (
        category1.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert [
        (
            category1.products
            == f"{product4.name}, {product4.price} руб. Остаток: {product4.quantity} шт.\n"
        )
    ]


def test_category2(category2, product1, product2, product3):
    assert category2.name == "Смартфоны"
    assert (
        category2.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert [
        category2.products
        == (
            f"{product1.name}, {product1.price} руб. Остаток: {product1.quantity} шт.\n"
            f"{product2.name}, {product2.price} руб. Остаток: {product2.quantity} шт.\n"
            f"{product3.name}, {product3.price} руб. Остаток: {product3.quantity} шт.\n"
        )
    ]


def test_add_product(category2, product4):
    category2.add_product(product4)
    category2.add_product(new_product)
    assert Category.product_count == 13


def test_add_error(category1):
    with pytest.raises(TypeError):
        category1.add_product(1)


def test_category_str(category1, category2):
    assert str(category2) == "Смартфоны, количество продуктов: 27 шт."
    assert str(category1) == "Телевизоры, количество продуктов: 7 шт."


def test_category_grass(category_grass, grass1, grass2):
    assert category_grass.name == "Газонная трава"
    assert category_grass.description == "Различные виды газонной травы"
    assert [
        category_grass.products
        == (
            f"{grass1.name}, {grass1.price} руб. Остаток: {grass1.quantity} шт.\n"
            f"{grass2.name}, {grass2.price} руб. Остаток: {grass2.quantity} шт.\n"
        )
    ]


def test_category_smartphones(
    category_smartphones, smartphone1, smartphone2, smartphone3
):
    assert category_smartphones.name == "Смартфоны"
    assert category_smartphones.description == "Высокотехнологичные смартфоны"
    assert [
        category_smartphones.products
        == (
            f"{smartphone1.name}, {smartphone1.price} руб. Остаток: {smartphone1.quantity} шт.\n"
            f"{smartphone2.name}, {smartphone2.price} руб. Остаток: {smartphone2.quantity} шт.\n"
            f"{smartphone3.name}, {smartphone3.price} руб. Остаток: {smartphone3.quantity} шт.\n"
        )
    ]


def test_avg_price1(category1, product4):

    category1 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )
    result = category1.avg_price()
    assert result == 17571.43


def test_avg_price2(category2, product1):

    category2 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1],
    )
    result = category2.avg_price()
    assert result == 36000.0


def test_avg_price_none_list(category1, product4):
    category1 = Category(name="none", description="none", products=[])
    result = category1.avg_price()
    assert result == 0


def test_category_property(category1, category2):
    with pytest.raises(AttributeError):
        print(category1.__products)
    assert category1.products_str_view == "55 QLED 4K, 123000.0 руб. Остаток: 7 шт.\n"
    assert (
        category2.products_str_view
        == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )
