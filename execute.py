import pickle
from labyrinthe import creation_labyrinthe

creation_labyrinthe()

labyrinthe = open("test.py", "rb")
mon_depickler = pickle.Unpickler(labyrinthe)
mon_labyrinthe = mon_depickler.load()
print(mon_labyrinthe)
