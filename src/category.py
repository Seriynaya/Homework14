from src.product import Product
class Category:
    name = str
    description = str
    products = list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=list):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.product_count += len(self.__products)
        Category.category_count += 1

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        return self.__products

    @property
    def products_list(self):
        str_product = ""
        for product in self.__products:
            str_product += (
                f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
            )
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
