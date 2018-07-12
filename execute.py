import pickle

from labyrinthe import *

creation_labyrinthe()

mon_labyrinthe = open("fichier_labyrinthe.py", "rb")
mon_depickler = pickle.Unpickler(mon_labyrinthe)
mon_labyrinthe = mon_depickler.load()
print(mon_labyrinthe)



nb_apparation_lettre()
mon_labyrinthe = open("fichier_labyrinthe.py","rb")
mon_unpickler = pickle.Unpickler(mon_labyrinthe)
mon_unpickler.load()

print(mon_labyrinthe)

