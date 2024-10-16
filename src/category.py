class Category:
    name = str
    description = str
    products = list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.product_count += 1
        Category.category_count += 1


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