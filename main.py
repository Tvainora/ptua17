

my_dictionary = {
    "obuolys": "vaisius, augantis ant medžių",
    "knyga": "rinkinys atspausdintų lapų, susegtų kartu, turintis tekstą ar paveikslėlius",
    "kompiuteris": "elektroninis įrenginys, skirtas duomenims saugoti ir apdoroti",}

while True:
      enter_imput = input("Įveskite žodį, kad sužinotumėte jo reikšmę (arba 'pabaiga') ")      
      if enter_imput.lower() == "pabaiga":
         print("Programa baigta")
         break
      if enter_imput in my_dictionary:
           print(f"Žodžio {enter_imput} reikšmė: {my_dictionary.get(enter_imput)}")
           break  
      else:
           print("Šio žodžio mūsų žodyne nėra")