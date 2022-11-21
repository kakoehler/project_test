#----------------------------------------------------------
# Dateiname: auskunft.py
# Bei diesem Programm handelt es sich um einen sehr 
# einfachen Prototyp eines Auskunftautomaten für einen 
# Onlineshop. Das Programm liest die Frage eines Kunden, 
# analysiert den Text und liefert eine Antwort, die zu der 
# Frage passt. Es sollen drei Fälle unterschieden werden:
# 1. Fall: Die Frage enthält das Wort 'Wann'. Es wird 
#          angenommen, dass die Frage den Liefertermin 
#          betrifft. 
#          Carla ist für die Liefertermine zuständig.
# 2. Fall: Die Frage enthält das Wort 'Rechnung'. Es wird 
#          angenommen, dass die Frage die Rechnung 
#          betrifft.
#          Tom ist für die Rechnung zuständig.
# 3. Fall: Die Frage enthält keines der beiden 
#          Schlüsselworter. Es kann nicht ermittelt werden 
#          worum es in der Frage geht. 
#          Kim ist für sonstige Angelegenheiten zuständig.
# Autor: Katha
# Letzte Änderung: 21.11.2022

# Eingabe
print('Wilkommen! Wie können wir Ihnen helfen?')
print('Bitte stellen Sie Ihre Frage!')
frage = input('Frage: ')

# Verarbeitung
if 'Wann' in frage:
    thema = 'zum Liefertermin'
    zuständig = 'Carla'
elif 'Rechnung' in frage:
    thema = 'zur Rechnung'
    zuständig = 'Tom'
else:
    thema = ''
    zuständig = 'Kim'

# Ausgabe
print('Vielen Dank für Ihre Frage ' + thema + '.')
print(zuständig + ' hilft Ihnen gerne weiter.')
