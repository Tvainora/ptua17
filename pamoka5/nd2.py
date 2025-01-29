shopping_list=["pienas", "kiaušiniai", "duona", "sviestas" ]
print(shopping_list)
i=shopping_list.index("duona")
shopping_list[i]="bananai"
print(shopping_list)
shopping_list.insert(0 , "obuolys")
print(shopping_list)
shopping_list.insert(5 , "miltai")
shopping_list.insert(7 , "cukrus")
print(shopping_list)
print(shopping_list[2:4])