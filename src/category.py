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
        self.product_count += len(products) if products else 0
        self.category_count += 1

if __name__ == '__main__':
    category1 = Category('Телевизоры', 'Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником')
    category2 = Category('Смартфоны', 'Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни')

    category = Category('Список товаров', 'ассортимент магазина', [category1, category2])
    print(category.name)
    print(category.description)
    print(category.products)
    print(category.category_count)
    print(category.product_count)