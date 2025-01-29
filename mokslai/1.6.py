name = str(input("Your name and surname: "))
space_index = name.find(" ")
first_name = name[:space_index]
first_name=name.upper()
print(f"Labas, {first_name.upper()}, sveiki atvykę!")