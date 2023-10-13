# 17) Create a function that receives the price of a product and the percentage of
# discount. View the amount of the discount and the price to be paid after the 
# discount:

def ex17(price, percent):
    discount = price * (percent / 100)
    price_to_be_paid = price - discount
    print("Full price       $:", price)
    print("Discount         %:", percent)
    print("Discount         $:", discount)
    print("Total to be paid $:", price_to_be_paid)

ex17(100, 10)