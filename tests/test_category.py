import pytest

from tests.confitest import category1, category2


def test_category(category1, category2):
    assert category1.name == "Смартфоны"
    assert category1.description == "Смартфоны"
    assert category2.name == "Телевизоры"
    assert category2.description == "Современный телевизор"
    assert len(category1.products) == 3

    assert category1.category_count == 2
    assert category1.product_count == 2

    assert category2.category_count == 2
    assert category2.product_count == 2
