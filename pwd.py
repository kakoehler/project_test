#----------------------------------------------------------
# Dateiname: pwd.py
# Dieses Programm führt einen Login-Dialog aus. Stimmt das 
# eingegebene Passwort mit dem gespeicherten überein, wird 
# der Benutzer begrüßt; Ansonsten wird nichts ausgegeben.
# Autor: Katha
# Letzte Änderung: 21.11.2022
#----------------------------------------------------------

# Eingabe
print('Bitte geben Sie ihr Passwort ein!')
pwd = input('Passwort: ')
if pwd == 'katha':                 # 1
    print('Passwort wurde erkannt.')   # 2
    print('Wilkommen!')                # 3
