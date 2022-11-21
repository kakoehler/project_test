#----------------------------------------------------------
# Dateiname: volumen_haus.py
# Dieses Programm berechnet das Volumen eines Hauses mit 
# Satteldach. Dazu werden folgende Werte eingelesen:
# - Die Länge der Stirnseite des Hauses a in Metern
# - Die Länge der Längsseite des Hauses b in Metern
# - Die Höhe der Basis(-Mauer) h1 in Metern
# - Die Höhe des Satteldachs von der Basis bis zum 
# Dachfirst h2 in Metern
# Autor: Katha
# Letzte Änderung: 21.11.2022
#----------------------------------------------------------

# Eingabe
print('Berechnung des Volumens eines Hauses mit Satteldach.')
a = float(input('Länge der Stirnseite des Hauses (a/m): '))
b = float(input('Länge der Langseite des Huases (b/m): '))
h1 = float(input('Höhe der Basis (h1/m): '))
h2 = float(input('Höhe des Dachs von der Basis bis zum First (h2/m): '))

# Verarbeitung
V1 = a * b * h1              # Volumen der Basis
V2 = (a * b * h2)/2          # Volumen des Satteldachs
V_ges = V1 + V2              # Gesamtvolumen des Hauses aus Basis und Dach

# Ausgabe
print('Das Haus hat ein Voolumen von ', str(V_ges), ' Kubikmetern.')
print('Ende des Programms mit ENTER bestätigen.')
