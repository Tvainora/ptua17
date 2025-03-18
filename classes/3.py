class Books:

    def __init__(self, title, author):
        self.title = title
        self.author = author

def get_title(self) -> str:
    return self.title

def get_author(self) -> str:
    return self.author

def create_report(self):
    return f"Title {self.title}, Author: {self.author}"

book1=Books(title = "Puikybė ir prietarai" , author = "Džeinė Ostin")
book2=Books(title = "Hamletas" , author = "Viljamas Šekspyras")
book3=Books(title = "Karas ir taika" , author = "Levas Tolstojus")
book4=Books(title = "Haris Poteris" , author = "D. K. Rouling" )

print(book1.create_report())
print(book2.create_report())
print(book3.create_report())
print(book4.create_report())


