#reduce
from functools import reduce

list_x = [1,2,3,4,5,6,7,8]

sum_list_x = reduce(lambda acumulative_v, item : item + acumulative_v, list_x, 0)

print(sum_list_x)

products=[
    {"name":"apple", "price":1, "qty": 4},
    {"name":"apple 2", "price":1, "qty": 4},
    {"name":"apple 3", "price":3, "qty": 4},
    {"name":"apple 4", "price":1, "qty": 4}
]

total_price = reduce(lambda a, item : (item["price"] * item["qty"]) + a, products, 0)
print(total_price)