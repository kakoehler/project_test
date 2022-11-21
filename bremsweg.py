#----------------------------------------------------------
# Dateiname: bremsweg.py
# Das Programm fragt nach Geschwindigkeit und 
# Bremsverzögerung und berechnet den Bremsweg.
# Autor: Katha
# Letzte Änderung: 21.11.2022
#---------------------------------------------------------- 
# Eingabe
print('Berechnung des Bremswegs')
v = float(input('Geschwindigkeit in m/s: '))
a = float(input('Bremsverzögerung in m/s^2: '))

# Verarbeitung
s = v**2 / (2*a)

# Ausgabe
print('Der Bremsweg beträgt ', str(s), 'Meter')
print('Ende des Programms mit ENTER bestätigen.')
