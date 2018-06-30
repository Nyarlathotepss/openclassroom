import random

#creation d'une liste de mot ainsi que la selection aleatoire
liste_mots = ["voiture", "chat","jardin","cours","barriere"]
mot = random.choice(liste_mots)
liste_lettre_saisie_correcte = []
nb_chance = 8
mot_trouve = ""

def recup_mot_cache(mot,liste_lettre_saisie_correcte):
    mot_cache = ""
    for lettre in mot :
        if lettre in liste_lettre_saisie_correcte :
            mot_cache += lettre
        else :
            mot_cache += "*"
    return mot_cache

while nb_chance != 0 and mot_trouve != mot :
    #demande de saisie de caractere UN seul
    lettre_saisie = input("veuillez saisir un caractere:")
    while len(lettre_saisie) >1:
        print("UN seul caracetere,recommencer") 
        lettre_saisie = input("veuillez saisir un caractere:")
    else:
        print("la lettre saisie est "+ lettre_saisie)
    
        #verifier la presence de la lettre_saisie   
    if lettre_saisie in mot :
        print("bravo")
        liste_lettre_saisie_correcte.append(lettre_saisie)
    elif lettre_saisie in liste_lettre_saisie_correcte :
        print("deja utilise")
    else:
        nb_chance -= 1 
        print("dommage")
    mot_trouve = recup_mot_cache(mot,liste_lettre_saisie_correcte)
    print(mot_trouve)
    if mot_trouve == mot :
        print("Bravo vous avez reussi")
        break
if nb_chance == 0 :
    print("Game Over")
