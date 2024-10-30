import pytest

from tests.confitest import smartphone1, smartphone2, smartphone3, grass1


def test_smartphone1(smartphone1):
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"


def test_smartphone2(smartphone2):
    assert smartphone2.name == "Iphone 15"
    assert smartphone2.description == "512GB, Gray space"
    assert smartphone2.price == 210000.0
    assert smartphone2.quantity == 8
    assert smartphone2.efficiency == 98.2
    assert smartphone2.model == "15"
    assert smartphone2.memory == 512
    assert smartphone2.color == "Gray space"


def test_smartphone3(smartphone3):
    assert smartphone3.name == "Xiaomi Redmi Note 11"
    assert smartphone3.description == "1024GB, Синий"
    assert smartphone3.price == 31000.0
    assert smartphone3.quantity == 14
    assert smartphone3.efficiency == 90.3
    assert smartphone3.model == "Note 11"
    assert smartphone3.memory == 1024
    assert smartphone3.color == "Синий"


def test_add_product_smartphone1(smartphone2, smartphone3):
    assert smartphone2 + smartphone3 == 2114000.0
    with pytest.raises(TypeError):
        smartphone2 + 1


def test_add_product_smartphone2(smartphone1, smartphone2):
    assert smartphone1 + smartphone2 == 2580000
    with pytest.raises(TypeError):
        smartphone1 + 1


def test_smartphone_add_grass(smartphone1, grass1):
    with pytest.raises(TypeError):
        smartphone1 + grass1
