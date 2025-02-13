def process_ages(people: dict) -> tuple:
    sum_age = sum(list(people.values()))
    avg_age = sum_age/len(people)
    square_poeple = {}
    for name, age in people.items():
        square_poeple[name] = age * age
    return avg_age, square_poeple



print(process_ages({"Alice": 25, "Bob": 30, "Charlie": 35}))