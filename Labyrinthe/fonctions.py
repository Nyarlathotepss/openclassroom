# On genere un dict a partir du fichier txt

def create_dict_labyrinthe(key1=0, key2=0):
    my_file = open("labyrinthe.txt", "r")
    text = my_file.read()
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
    return labyrinthe

def create_labyrinthe_to_print():

    ligne = str()
    list_lettre = []
    i = 0
    for lettre in dict_labyrinthe.values():
        list_lettre.append(lettre)
        i += 1
        if i > 15:
            ligne = "".join(list_lettre)
            print(ligne + "\n")
            ligne = None
            i = 0

def check_mcgyver() :

    from execute import dict_labyrinthe
    if lettre == "m" in dict_labyrinthe.values():
        position = dict_labyrinthe.keys()
    return position

def move_mcgyver():

    move_input = input("saisir une direction:")
    if move_input == "q":
        create_labyrinthe_to_print[(position)] = "-"
        create_labyrinthe_to_print[(position)([0] - 1)] = "m"
    if move_input == "d":
        create_labyrinthe_to_print[x , y] = "-"
        create_labyrinthe_to_print[(x + 1), y] = "m"
    if move_input == "s":
        create_labyrinthe_to_print[x, y] = "-"
        create_labyrinthe_to_print[x , (y + 1)] = "m"
    if move_input =="z":
        create_labyrinthe_to_print[x , y] = "-"
        create_labyrinthe_to_print[x , (y - 1)] = "m"





