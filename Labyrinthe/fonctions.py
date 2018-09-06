
def list_display_lab ():

    listtodisplay = []
    i = 0
    for letter in self.dict_labyrinthe.values:
        listtodisplay.append(letter)
        fenetre.blit(self.image)
        i += 1

        if i > 15:
            listtodisplay.append(/n)


            ''' def lablist (self):
             create an object type list to show image in pygame( a revoir pour return list)
             ligne = str()
             list_lettre = []
             i = 0
             for lettre in self.dict_labyrinthe.values():
                 list_lettre.append(lettre)
                 i += 1
                 if i > 15:
                     ligne = "".join(list_lettre)
                     print(ligne)
                     ligne = None
                     i = 0
                     list_lettre = []'''






