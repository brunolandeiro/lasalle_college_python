#map
simple_list = [1,2,3,4,5,6,7,8]
products=[
    {"name":"apple", "price":1, "qty": 4},
    {"name":"apple 2", "price":1, "qty": 4},
    {"name":"apple 3", "price":3, "qty": 4},
    {"name":"apple 4", "price":1, "qty": 4}
]

new_simple_list = map(lambda x: x*2, simple_list)
new_simple_list = list(new_simple_list)
print(new_simple_list)

new_products = map(lambda item : item["price"], products)
new_products = list(new_products)
print(new_products)

def update_product(item):
    item["price"] = item["price"]*1.15
    item["price"] = round(item["price"], 2)
    return item

new_products = map(update_product, products)
new_products = list(new_products)
print(new_products)