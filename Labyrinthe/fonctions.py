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

def create_labyrinthe_to_print() :
    my_file = open("labyrinthe.txt", "r")
    text = my_file.read()
    labyrinthe_to_print = []
    for line in text:
        labyrinthe_to_print = line.strip("\n")
    return labyrinthe_to_print


'''def check_mcgyver ():
    for lettre in labyrinthe_to_print[2]:
        if lettre == "m":
            mc_gyver =  create_labyrinthe_to_print()


def move_mcgyver() :
    move_input = input("saisir une direction:")
    if move_input == "q":

    if move_input == "d":

    if move_input == "s":

    elif move_input =="z": '''




