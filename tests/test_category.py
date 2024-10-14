import pytest
from tests.confitest import category1, category2
def test_category(category1, category2):
    assert category1.name == "Смартфоны"
    assert category1.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert len(category1.products) == 3

    assert category1.category_count == 1
    assert category1.product_count == 3

    assert category2.category_count == 1
    assert category2.product_count == 3