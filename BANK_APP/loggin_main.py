print("Wellcome to BANK PRO app!")

user_login = input("Enter your login: ")
# user_email = input("Enter your E-mail here: ")


import json
email_list = list()

with open("email_list.json", "r") as file:
    email_list = json.load(file)

class login:


    def validate_email(user_email):
        if user_email.count("@") != 1:
            return False

        parts = user_email.split("@")
        username = parts[0]
        domain = parts[1]

        if not username:
            return False

        if "." not in domain:
            return False

        domain_parts = domain.split(".")

        for part in domain_parts[:-1]:
            if len(part) == 0:
                return False

        if len(domain_parts[-1]) < 2:
            return False

        return True



    user_email = str(input("Enter your E-mail here: "))
    

    if validate_email(user_email):
        print (f"Your E-mail adrees is valid. Youll get loggin and password shortly.")
    
    else:
        print("E-mail adress was incorect. Please try again.")

