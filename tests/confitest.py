import pytest

from src.category import Category
from src.product import Product


@pytest.fixture()
def product1():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture()
def category1():
    return Category(
        name="Смартфоны",
        description="Смартфоны",
        products=["Samsung Galaxy S23 Ultra", "Iphone 15", "Xiaomi Redmi Note 11"],
    )


@pytest.fixture()
def category2():
    return Category(
        name="Телевизоры",
        description="Современный телевизор",
        products=["Samsung", "Xiaomi", "Toshiba"],
    )
