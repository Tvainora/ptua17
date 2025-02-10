import random

# def print_random_stuff(name, age=12, *args, **kwargs) -> None:
#     print(name, age)
#     print(args)
#     print(kwargs)


# print_random_stuff(
#     "Jonas",
#     "Petras",
#     "Antanas",
#     "Mindaugas",
#     random_name="Tomas",
#     random_name_2="Tomas",
# )


# def new_func(a, b, c, d=20, *args, **kwargs) -> None:
#     print(a, b, c, d)
#     if args:
#         # I do whatever I want with args
#         # args is a tuple
#         print(args)
#     if kwargs:
#         # I do whatever I want with kwargs
#         # kwargs is a dictionary
#         print(kwargs)




# items_list = ["apple", "cabbage", "pineapple", "bread", "beer", "banana", "meat", "beef", "chicken", "juice"]
# prices_list = [3, 4, 5, 7, 2, 1, 10, 34, 12, 9, 12]
# quantity = [50, 40, 15, 20, 100, 30, 10, 1, 2, 3, 4]

def items_list  [a:str ="apple", 
                b:str ="cabbage",
                c:str = "pineapple", 
                d:str ="bread", 
                e:str ="beer", 
                f:str ="banana", 
                g:str ="meat", 
                h:str ="beef", 
                i:str ="chicken", 
                j:str ="juice"]:
list = item_list.randomized

def prices_list  [a: int=3, 
                b: int=4, 
                c: int=5, 
                d: int=7, 
                e: int=2, 
                f: int=1, 
                g: int=10, 
                h: int=34, 
                i: int=12, 
                j: int=9, 
                k: int=12]

def quantity  [a: int=50, 
               b: int=40, 
               c: int=15, 
               d: int=20, 
               e: int=100, 
               f: int=30, 
               g: int=10, 
               h: int=1, 
               i: int=2, 
               j: int=3, 
               k: int=4]   

while True:
        baskets_quantity = int(input("How many baskets would you like me to generate? 5-10 "))
        final_list = []
        if baskets_quantity <5 or baskets_quantity >10:
            print("Netinkamas skaicius, turi but nuo 5 iki 10")



        else:   
            for i in range(baskets_quantity):
                randomized_item = random.choice(items_list)
                price_index = int(items_list.index(randomized_item))
                basket = {"item":randomized_item, "Price":prices_list[price_index], "Quantity":random.choice(quantity)}
                items_list.remove(randomized_item)
                final_list.append(basket)
        print(final_list)
        break


highest_value = max(d["Price"] for d in final_list)
final_price_list = [d['Price'] for d in final_list]
index_of_highest = final_price_list.index(highest_value)
print(f"Index of the final list that contains the must expensive item is {index_of_highest}")

lowest_value = min(d["Price"] for d in final_list)
cheapest_progress = final_price_list.index(lowest_value)
cheapest_indeed = final_list[cheapest_progress]
print(f"The cheapest is {cheapest_indeed["item"]}")

min_price = None
min_price_index = None
print(final_list)
for i, basket in enumerate(final_list):
    price = basket["Price"]
    if min_price == None:
        min_price = price
        min_price_index = i

    elif price <min_price:
        min_price = price
        min_price_index = i

print(f"Lowest price product is {min_price}")

print(f"Lowest price product index is {i}: {final_list[min_price_index]}")
