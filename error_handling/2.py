# # TypeError, +
# ValueError,
# KeyError,
# IndexError,
# AttributeError


import logging

logging.basicConfig(
    level=logging.ERROR,
    filename="ups2.txt",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",)

def safe_divide(int(a), int(b)):
        try:
        c = a / b
        except Exception as e:
        logging.error("Error! {e}")
        return "Error ocured!"

print(safe_divide(int(10), str(2)))




# try:
#     input = 25 / 0
#     print(input)
# except Exception as e:
#     print(f"Error: {e}")
# else:
#     print("No error occured")
# finally:
#     print("I will always run")







# print(safe_divide(10, "hello world"))
# print(safe_divide(10, 2))




import math

def calculate_tip(amount: float ∣ int , rating: str):
    rating=rating.lower()
    tip_rating = {"Terrible": 0, "Poor": tip 0.05, "Good": 0.10, "Great": 0.15 , "Excellent": 0.20}
    if rating in tip_rating:
        users_tip = tip_rating [rating] * amount
        return math.ceil (users_tip)
    else:
        return "Rating not regognized!"