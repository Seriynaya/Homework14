from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """Класс предоставляющий информацию о конкретном продукте"""

    name: str
    description: str
    price: int
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Инициализация объекта"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        if self.quantity >= 1:
            self.quantity = quantity
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__()

    def __str__(self):
        """Отображение строки в заданном формате"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Метод сложения двух продуктов"""
        if type(self) == type(other):
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError

    @classmethod
    def new_product(cls, product_info: dict):
        """Добавление нового продукта в список"""
        name = product_info.get("name")
        description = product_info.get("description")
        price = product_info.get("price")
        quantity = product_info.get("quantity")
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price_cost: int):
        """Функция изменения цены"""
        if price_cost <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = price_cost


if __name__ == "__main__":
    product = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )

    print(product.name)
    print(product.description)
    print(product.price)
    print(product.quantity)
