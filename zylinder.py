#! /usr/bin/env/ python
#----------------------------------------------------------
# Dateiname: zylinder.py
# Das Programm fragt nach dem Durchmesser und der Höhe 
# eines Zylinders und berechnet das Volumen.
# Autor: katha
# Letzte Änderung: 21.11.2022
#----------------------------------------------------------
# Eingabe
print('Berechnung des Volumens eines Zylinders')
# eingabe_h = input('Höhe in Meter: ')
# eingabe_d = input('Durchmesser in Meter: ')

# Verarbeitung
# h = float(eingabe_h)
# d = float(eingabe_d)
h = float(input('Höhe in Meter: '))
d = float(input('Durchmesser in Meter: '))
volumen = (d/2)**2 * 3.14 * h

# Ausgabe 
# text = 'Das Volumen beträgt ' + str(volumen) + ' Kubikmeter.'
# print(text)
print('Das Volumen beträgt ', volumen, ' Kubikmeter')
input('Programm beenden mit ENTER')
