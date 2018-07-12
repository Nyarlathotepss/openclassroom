import pickle

from carte import text


def creation_labyrinthe():
    key1 = 0
    key2 = 0
    labyrinthe = {}
    nb_lettre = 0  # Bloc pour compter le nombre de lettre dans une ligne
    for lettre in text:
        nb_lettre += 1
        if lettre == "\n":
            nb_lettre -= 1  # Ici on enleve le saut de ligne \n du comptage de lettre
            break
    for lettre in text:
        if lettre != "\n":
            labyrinthe[key1, key2] = lettre
            key1 += 1
            if key1 == nb_lettre:
                key1 = 0
                key2 += 1
        else:
            continue

    fichier_labyrinthe = open("fichier_labyrinthe.py", "wb")
    mon_pickler = pickle.Pickler(fichier_labyrinthe)
    mon_pickler.dump(labyrinthe)


def nb_apparation_lettre():
    fichier_labyrinthe = open("fichier_labyrinthe.py", "rb")
    mon_depickler = pickle.Unpickler(fichier_labyrinthe)
    labyrinthe = mon_depickler.load()

    liste_text = []  # On crée une liste de la variable text sans les saut de ligne (\n)
    for lettre in text:
        if lettre == "\n":
            ()
        else:
            liste_text.append(lettre)

    nb_apparition = 0  # On init la valeur d'apparition
    for lettre in liste_text:  # On compte les lettres
        if lettre in labyrinthe.keys():
            nb_apparition += 1
        else:
            nb_apparition = 1
        labyrinthe[lettre] = nb_apparition  # On crée une nouvelle ligne dans le dict labyrinthe
    print(labyrinthe)

    fichier_labyrinthe = open("fichier_labyrinthe", "wb")
    mon_pickler = pickle.Pickler(fichier_labyrinthe)
    mon_pickler.dump(labyrinthe)
