#----------------------------------------------------------
# Dateiname: fehler1.py
# Ein fehlerhafter Programmtext zur Demonstartion.
# Eigentlich soll das Programm das Quadrat einer Zahl 
# ausgeben. Hier wird allerdings nur das Doppelte 
# ausgegeben. Das ist ein semantischer bzw. logischer 
# Fehler. Das Programm leistet nicht das, was es leisten 
# soll.
# Autor: Katha
# Letzte Änderung: 21.11.2022
#----------------------------------------------------------

# fehler1.py
a = int(input('Zahl: '))
ergebnis = a * 2
# debugging: 
# ergebnis = a ** 2
print(ergebnis)
