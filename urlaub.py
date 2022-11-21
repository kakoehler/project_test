#----------------------------------------------------------
# Dateiname: urlaub.py
# Ein Programm zur Berechnung der mittleren Kosten pro 
# Urlaubstag.
# Autor: Katha
# Letzte Änderung: 21.11.2022
#----------------------------------------------------------

# Eingabe
hotel = float(input('Hotelkosten in Euro: '))
essen = float(input('Gesamtkosten für Restaurants in Euro: '))
tage = float(input('Anzahl der Urlaubstage: '))

# Verarbeitung
kosten = (hotel + essen) / tage

# Ausgabe 
print('Miitlere Kosten pro Urlaubstag: ', kosten)
input('Programm beenden mit ENTER')
