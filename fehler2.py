#----------------------------------------------------------
# Dateiname: fehler2.py
# Ein fehlerhafter Programmtext zur Demonstartion.
# Eigentlich soll das Programm das Quadrat einer Zahl 
# ausgeben. Allerdings wird in Zeile 1 der Variablen a 
# keine Zahl (float()), sondern eine Zeichkette (str()) 
# zugewiesen. In Zeile 2 führt das dann zu einem 
# Laufzeitfehler, da ** nicht auf eine Zeichenkette 
# angewendet werden kann.
# Autor: Katha
# Letzte Änderung: 21.11.2022
#----------------------------------------------------------

# fehler2.py
a = input('Zahl: ')          # 1
# debugging: 
# a = float(input('Zahl: '))
ergebnis = a ** 2            # 2
print(ergebnis)
