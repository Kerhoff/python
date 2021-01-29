# 6. * Реализовать структуру данных «Товары».
#    Она должна представлять собой список кортежей.
#    Каждый кортеж хранит информацию об отдельном товаре.
#    В кортеже должно быть два элемента — номер товара и словарь с параметрами
#    (характеристиками товара: название, цена, количество, единица измерения).
#    Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# 
# 
#    Пример готовой структуры:
#    [
#    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}), 
#    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
#    ]
#
#    Необходимо собрать аналитику о товарах.
#    Реализовать словарь, в котором каждый ключ — характеристика товара,
#    например название, а значение — список значений-характеристик,
#    например список названий товаров.
#
#    Пример:
#    {
#    “название”: [“компьютер”, “принтер”, “сканер”],
#    “цена”: [20000, 6000, 2000],
#    “количество”: [5, 2, 7],
#    “ед”: [“шт.”]
#    }


goods: list = []

# Get number of products
number_of_products: int = int(input("Enter number of products:"))

# Get product details
for i in range(number_of_products):
    print("Enter product details below: ")
    product_id: int = int(input("Id: "))
    name: str = input("Name: ")
    price: float = float(input("Price: "))
    quantity: int = int(input("Quantity: "))
    unit: str = input("Unit: ")

    product: tuple = (product_id, {"name": name, "price": price, "quantity": quantity, "unit": unit})
    goods.append(product)
    i += 1

print(goods)

# Get analytics of goods
goods_analytics: dict = {"name": [], "price": [], "quantity": [], "unit": []}
for product in goods:
    goods_analytics["name"].append(product[1]["name"])
    goods_analytics["price"].append(product[1]["price"])
    goods_analytics["quantity"].append(product[1]["quantity"])
    goods_analytics["unit"].append(product[1]["unit"])

print(goods_analytics)
