definitions = {
    "obuolys": "vaisius, augantis ant medžių",
    "knyga": "rinkinys atspausdintų lapų, susegtų kartu, turintis tekstą ar paveikslėlius",
    "kompiuteris": "elektroninis įrenginys, skirtas duomenims saugoti ir apdoroti",}

while True:
      user_imput = input("Please enter word which you are looking for (or 'end') ")      
      if user_imput.lower() == "end":
         print("End of the program")
         break
      if user_imput in definitions:
           print(f"Input {user_imput} meaning: {definitions[user_imput]}")
           break  
      else:
           print("No word found in dictionary")