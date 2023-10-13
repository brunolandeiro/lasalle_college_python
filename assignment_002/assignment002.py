# Create a python program that asks the user for the product name, price and qty. Save the values inside a list called products.
# - The program must keep asking if the user wants to add more products.
# - When the user decides to stop the program must show the name and the price for the cheapest and the most expensive product.
# - Program should show the average of the product prices at the end
# - The program should show the list with all the products information and total amount to be paid.
def is_a_valid_float(text):
    try:
        float(text)
        return True
    except ValueError:
        return False

def is_a_valid_int(text):
    try:
        int(text)
        return True
    except ValueError:
        return False

def read_float_number(text):
    number = ""
    while not(is_a_valid_float(number)):
        number = input(text)
    return float(number)

def read_int_number(text):
    number = ""
    while not(is_a_valid_int(number)):
        number = input(text)
    return int(number)

def prices_avg(products):
    total = 0
    for product in products:
        total += product["price"]
    return total / len(products)

def total_amount(products):
    total = 0
    for product in products:
        total += product["price"] * product["qtd"]
    return total

def display_products_list(products):
    print("Name\tPrice\tQuantity")
    for product in products:
        print(product["name"],"\t",product["price"],"\t",product["qtd"])

products = []
continue_adding = 'y'
quantity = ""
while continue_adding != 'n' and continue_adding != 'N':
    name = input("Enter the product name: ")
    price = read_float_number("Enter the product price: ")
    quantity = read_int_number("Enter the product quantity: ")
    products.append({"name": name, "price": price, "qtd": quantity})
    continue_adding = input("\nWants to add more products? (y/n): ")

products.sort(key=lambda product : product['price'])
cheapest_product = products[0]
most_expensive_product = products[-1]
print("\nThe cheapest product was {name}, $ {price}".format(name=cheapest_product["name"], price=cheapest_product["price"]))
print("The most expensive product was {name}, $ {price}".format(name=most_expensive_product["name"], price=most_expensive_product["price"]))
print("The average of the product prices was $ {avg}".format(avg=prices_avg(products)))
display_products_list(products)
print("The total amount to be paid: $ ", total_amount(products))

