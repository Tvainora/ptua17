# # Write a function that takes a list of numbers as input and returns:
# # The sum of all numbers in the list.
# # A new list with each element squared
# # [1, 2, 3, 4]  -> (10, [1, 4, 9, 16])


def process_numbers(numbers: list) -> tuple:
    square_list = []
    sum = 0
    for i in numbers:
        sum += i
        square_list.append(i * i)

    return sum, square_list

print(process_numbers([1, 2, 3, 4, 9, 11]))

# Task 3: Nested List and Dictionary Manipulation with Functions
# Write a function that takes a list of dictionaries, where each dictionary represents a person with their name and a list of their test scores. The function should:
# Return the average score for each person.
# Create and return a new list of dictionaries with each dictionary containing the person's name and their highest test score.
 
 
def process_scores(people_scores: list) -> tuple:
    scores_list = []
  
   
        
 
# [

#   {"name": "Alice", "scores": [85, 90, 78]},

#   {"name": "Bob", "scores": [88, 92, 95]},

#   {"name": "Charlie", "scores": [78, 80, 72]}

# ]

# -> (

#   [84.33, 91.67, 76.67], 

#   [{"name": "Alice", "highest_score": 90}, {"name": "Bob", "highest_score": 95}, {"name": "Charlie", "highest_score": 80}]

# )

 