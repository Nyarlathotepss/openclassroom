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

def create_labyrinthe_to_print() :
    my_file = open("labyrinthe.txt", "r")
    text = my_file.read()
    labyrinthe_to_print = []
    for line in text.split('\n'):
        labyrinthe_to_print.append(line)
    return labyrinthe_to_print


def check_mcgyver() :

    x = 0
    y = 0
    from execute import dict_labyrinthe
    for lettre in dict_labyrinthe:
        if lettre == "m":
            x = lettre[1]
            y = lettre[0]

    return x

def move_mcgyver() :
    move_input = input("saisir une direction:")
    if move_input == "q":
        create_labyrinthe_to_print[x , y] = "-"
        create_labyrinthe_to_print[(x - 1), y] = "m"
    if move_input == "d":
        create_labyrinthe_to_print[x , y] = "-"
        create_labyrinthe_to_print[(x + 1), y] = "m"
    if move_input == "s":
        create_labyrinthe_to_print[x, y] = "-"
        create_labyrinthe_to_print[x , (y + 1)] = "m"
    elif move_input =="z":
        create_labyrinthe_to_print[x , y] = "-"
        create_labyrinthe_to_print[x , (y - 1)] = "m"


# on tente de creer le labyrinthe a affichier via le dict et non via le fichier txt ceux qui est plus pertinent
def create_lab_to_print() :
    from execute import dict_labyrinthe
    i = 0
    j = 0
    labyrinthe_to_print = []
    for lettre in dict_labyrinthe:
        labyrinthe_to_print[j]+ lettre
        i += 1
        if  i == 15:
            j = 1
    return labyrinthe_to_print





