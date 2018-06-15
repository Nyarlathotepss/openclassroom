# Preparation du projet 3

def partie_1():
    # Créer un fichier texte (carte.txt) contenant la variable text
    text = "WWWW-----W\nW-------WW\nWWW-M--WWW\nWWWWWW--WW"

def partie_2():
    # Afficher en console le fichier texte créé à l'exercice 1
    pass

def partie_3(lettre):
    # Vérifier si la lettre entrée en paramètre est présente
    # dans le fichier créé à l'exercice 1 (retourner True si
    # la lettre est présente et False sinon)
    pass

def partie_4(lettre):
    # Trouver la position de la lettre passée en paramètre dans
    # le fichier créé à l'exercice 1. Si lettre == "M", la fonction
    # doit renvoyer le tuple (4, 2) car le lettre "M" est dans la colonne
    # 4 (numérotation à partir de 0) et la ligne 2 dans la variable text de
    # l'exercice 1.
    pass

def partie_5():
    # Créer un dictionnaire contenant toutes les lettres présentes
    # dans le fichier texte de l'exercice avec leur nombre d'apparition
    # dans le fichier : {"W": 22, "M": 1}
    pass

def partie_6():
    # Demander si le joueur veut continuer le jeu (avec input). Si la
    # réponse est "oui" ou "o", on repose la même question. Si la réponse
    # est "non" ou "n", la boucle s'arrête. Si une autre réponse est donnée,
    # afficher "Réponse non correcte" puis reposer la question.
    pass
    
if __name__ == "__main__":    
    partie_1()
    partie_2()
    print(partie_3("M"))
    print(partie_4("M"))
    partie_5()
    partie_6()
