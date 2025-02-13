# 1) Create a lambda function that takes a number and returns its square.
# 2) Create a lambda function that takes two numbers and returns their squared sum.
# 3) Use the lambda function to sort list of tuples based on the second element:
# tuples_list = [(1,3), (4,1), (5,2), (2,4)]


# Use lambda functions to sort list of strings by their length and then alphabetically.

# words = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']

# 1

square=(lambda a: a*a)(5)
print(square)
        
# 2

square_two=(lambda a, b: (a+b)**2)(5, 5)
print(square_two)

# 3

tuples_list = [(1,3), (4,1), (5,2), (2,4)]
tuples_list.sort(key=lambda x:x[1])
print(tuples_list)

# 4

words = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']
by_lenght=sorted(words ,key=len)
print(by_lenght)




