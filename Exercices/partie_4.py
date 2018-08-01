from Exercices.labyrinthe import squelette_labyrinthe

lettre_a_saisir = input("Veuillez saisir une lettre :")

for cle,valeur in squelette_labyrinthe.items() :
    if valeur == lettre_a_saisir :
        print(cle)






