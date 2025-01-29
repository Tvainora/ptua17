narys=str(input("Ar esate narys? taip ar ne "))
met=int(input("Kiek Jums metu? "))

if narys == "ne":
    print("Negali skaityt")
elif narys == "taip" and met <= 10:
    print(f"Tau {met} todel gali skaityt vaiku knygas") 
elif narys == "taip" and met > 10:
    print(f"Tau {met} Skaityt gali tik suaugusiuju knygas")
