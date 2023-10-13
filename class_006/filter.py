#filter
list_x = [1,2,3,4,5,6,7,8]

products=[
    {"name":"apple", "price":1, "qty": 4},
    {"name":"apple 2", "price":1, "qty": 4},
    {"name":"apple 3", "price":3, "qty": 4},
    {"name":"apple 4", "price":1, "qty": 4}
]

new_list_x = list(filter(lambda item: item%2 == 0, list_x))
print(new_list_x)

n_products = list(filter(lambda item: item["price"]>2, products))
print(n_products)


