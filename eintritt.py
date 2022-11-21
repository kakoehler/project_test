#----------------------------------------------------------
# Dateiname: eintritt.py
# Dieses Programm fragt nach dem Alter und gibt für 
# Personen unter 18 einen anderen Text aus als für 
# Erwachsene.
# Autor: Katha
# Letzte Änderungen: 21.11.2021
#----------------------------------------------------------

# Eingabe
print('Wilkommen im Kino!')
print('Geben Sie bitte Ihr Alter an.')
alter = int(input('Alter (Jahre): '))

# Verarbeitung
if alter < 18:
    print('Dein Ticket kostet 5,00 €')
else:
    print('Ihr Ticket kostet 8,50 €')
# Ausgabe -- Ende
print('Viel Spaß!')
