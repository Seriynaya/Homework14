from src.product import Product


class Category:
    """Класс предоставляющий информацию о категории товара и его общих характеристиках"""

    name = str
    description = str
    products = list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Инициализация объекта"""
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.product_count += len(self.__products)
        Category.category_count += 1

    def avg_price(self):
        try:
            prices = sum([value.price for value in self.__products])
            quantities = sum([value.quantity for value in self.__products])
            avg = prices / quantities
            return round(avg, 2)

        except ZeroDivisionError:
            return 0

    def __str__(self):
        """Отображение строки в заданном формате"""
        quantity = 0
        for i in self.__products:
            quantity += i.quantity
        return f"{self.name}, количество продуктов: {quantity} шт."

    def add_product(self, product):
        """Функция добавления нового продукта в список"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products_list(self):
        return self.__products

    @property
    def products_str_view(self):
        """Отображение продукта в заданном формате"""
        str_product = ""
        for product in self.__products:
            str_product += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return str_product


if __name__ == "__main__":
    category1 = Category(
        "Телевизоры",
        "Современный телевизор",
    )
    category2 = Category(
        "Смартфоны",
        "Смартфоны",
    )

    category = Category(
        "Список товаров", "ассортимент магазина", [category1, category2]
    )
    print(category.name)
    print(category.description)
    print(category.products)
    print(category.category_count)
    print(category.product_count)
