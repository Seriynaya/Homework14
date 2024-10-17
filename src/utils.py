import json

from src.category import Category
from src.product import Product


def read_json_file(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def obj_from_json(data):
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))

    return categories


if __name__ == "__main__":
    read_file = read_json_file("../data/products.json")
    json_product = obj_from_json(read_file)
    print(json_product)
