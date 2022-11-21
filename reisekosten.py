#----------------------------------------------------------
# Dateiname: reisekosten.py
# Das Programm berechnet die Kosten für eine Gruppenreise 
# mit dem Bus. Dazu werden folgende Daten nacheinander 
# abgefragt:
# - Kosten für den Reisebus
# - Hotelkosten pro Person
# - Kosten für einen Reiseführer
# - Anzahl der Teilnehmener
# Ausgegeben werden:
# - Die Gesamtkosten der Fahrt
# - Die Teilnahmegebühr pro Person
# Autor: Katha
# Letzte Änderung: 21.11.2022
#---------------------------------------------------------- 

# Eingabe
print('Berechnung der Kosten einer Busreise (gesamt/pro Person)')
bus = float(input('Kosten für den Reisebus (€): '))
hotel = float(input('Hotelkosten pro Person (€): '))
personal = float(input('Kosten für den Reiseführer (€): '))
n = float(input('Anzahl der Teilnehmerinnen: '))

# Verarbeitung
gesamt = bus + hotel*n + personal
einzel = gesamt/n

# Ausgabe
print('Gesamtkosten für ', str(n), ' Personen: ', str(gesamt), '€')
print('Teilnehmerbeitrag pro Person (€): ', str(einzel), '€')
print('Ende des Programms mit ENTER bestätigen.')
