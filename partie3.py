
lettre_saisie = input("saisir un caractere:")

from carte import text

if lettre_saisie in text :
    lettre_presente = True
else :
    lettre_presente = False

print(lettre_presente)
