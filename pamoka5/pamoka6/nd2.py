
# Create 3 separate list . One list contains shopt items, another list - prices, and last list 
# amount.
# Ask user to enter the number of item baskets she/he wants to create (min 5 buckets).
# Basket is created randomly picking one value from each list (items,price,amount)
# Example bucket = {"item":toy, "price": 35, "amount": 56}
# Created buckets are put in a final list.
# Print the buckets index on the final list witch contains most expensive items.
# Which item is with lowest price? Which item has most monetary value in store?
# There can be only different items on the final list (can't be same item in different buckets)


while True:

import random

items_list = ["apple", "caffe", "book", "tea", "beer", "cola", "lemon", "orange", "avocado", "pineapple"]
prices_list = [1, 3, 10, 2, 4, 2, 1, 2, 3, 5]
quantity = [50, 40, 15, 20, 100, 30, 10, 60, 70, 80]

# new_dictionary = dict(zip(items_list, prices_list))
# my_dictionary = dict(zip(new_dictionary, quantity))

# my_dictionary = dict(zip(items_list, zip(prices_list, quantity)))
# randomized_item = random.choice(my_dictionary)
 
print(random.choice(my_dictionary))
# print(randomized_item)

 
while True:
    user_input = int(input("Hom many baskets you wanted to create (min 5, max 10): "))
    if user_input < 5 or user_input > 10:
        print("Wrong input. Please enter the number between 5 and 10!")
        break





