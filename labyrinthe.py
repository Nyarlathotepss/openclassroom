# Creation du labyrinthe en dictionnaire
import pickle

from carte import text

def creation_labyrinthe () :
    key1 = 0
    key2 = 0
    labyrinthe = {}
    for lettre in text :
        if lettre != "\n" :
            labyrinthe[key1,key2] = lettre
            key1 += 1
            if key1 == 10 :
                key1 = 0
                key2 += 1
        else :
            continue

    fichier_labyrinthe =  open("test.py","wb")
    mon_depickler = pickle.Pickler(fichier_labyrinthe)
    mon_depickler.dump(labyrinthe)
