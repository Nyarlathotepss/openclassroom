import pygame
import random

class Element:

    dictionnary = {"w":"wall.png", "m":"MacGyver.png", "a":"seringue.png", "b":"tube_plastique.png", "c":"ether.png", "g":"Gardien.png", "-":"empty.png"}

    def __init__(self,letter):
        self.position = []
        self.letter = letter
        self.image = pygame.transform.scale(pygame.image.load(Element.dictionnary[letter]), [20,20])

    def insertposition(self,positionx,positiony):
        self.position.append([positionx,positiony])




class Player:

    def __init__(self,dictionnary):
        self.positionx,self.positiony = self.checkposition(dictionnary)
        self.listobjects = set()

    def checkposition(self,dictionnary):
        for cle, valeur in dictionnary.dict_labyrinthe.items(): # ICIIIIIIIIIIIIII pb j'ai modifié dictionnary.items par dictionnary.dict_labyrinthe.items et ca marche
            if valeur == "m":
                return cle

    def checkobject(self,dictionnary):

        if self.checkposition() == dictionnary.object1[0]: # j'apelle un object dictionnary qui contient object1 (lui meme une liste)
            self.listobjects.add(dictionnary.object1[1])
        if self.checkposition() == dictionnary.object2[0]:
            self.listobjects.add(dictionnary.object2[1])
        if self.checkposition() == dictionnary.object3[0]:
            self.listobjects.add(dictionnary.object3[1])

    def checkallobjects(self):

        if len(self.listobjects) == 3:
            return True
        else:
            return False

    def checkguardianposition(self,dictionnary): # Ajout
        for cle, valeur in dictionnary.dict_labyrinthe.items():
            if valeur == "g":
                return cle


class Dictionnary:

    def __init__(self):
        '''By default my dictionnary is empty'''
        self.dict_labyrinthe = {}
        self.object1 = []
        self.object2 = []
        self.object3 = []
        self.generatedictionnary()
        self.generateobject()

    def generatedictionnary(self):
        ''' Generate a dictionnary with file.txt'''
        my_file = open("labyrinthe.txt", "r")
        text = my_file.read()

        nb_lettre = 15  # Bloc pour compter le nombre de lettres dans une ligne
        key1 = 0
        key2 = 0

        for lettre in text:
            if lettre != "\n":
                self.dict_labyrinthe[key1, key2] = lettre
                key1 += 1
                if key1 == nb_lettre:
                    key1 = 0
                    key2 += 1

    def generateobject(self):
        '''generate 3 objects in random position in dictionnary'''
        list_empty_case = []
        for cle, valeur in self.dict_labyrinthe.items():
            if valeur == "-":
                list_empty_case.append(cle)
        self.object1.append(random.choice(list_empty_case))
        self.object2.append(random.choice(list_empty_case))
        self.object3.append(random.choice(list_empty_case))
        self.dict_labyrinthe[self.object1[0]] = "a"
        self.object1.append("a")
        self.dict_labyrinthe[self.object2[0]] = "b"
        self.object2.append("b")
        self.dict_labyrinthe[self.object3[0]] = "c"
        self.object3.append("c")

    def display_element(self, pygamewindow):

        list_wall = Element("w")
        list_gyver = Element("m")
        list_guardian = Element("g")
        list_object1 = Element("a")
        list_object2 = Element("b")
        list_object3 = Element("c")


        for cle, valeur in self.dict_labyrinthe.items():
            if valeur == "w":
                list_wall.insertposition(cle[0],cle[1])
                destx = cle[0] * 20
                desty = cle[1] * 20
                pygamewindow.blit(list_wall.image,(destx,desty))

        for cle, valeur in self.dict_labyrinthe.items():
            if valeur == "m":
                list_wall.insertposition(cle[0],cle[1])
                destx = cle[0] * 20
                desty = cle[1] * 20
                pygamewindow.blit(list_gyver.image,(destx,desty))

        for cle, valeur in self.dict_labyrinthe.items():
            if valeur == "g":
                list_wall.insertposition(cle[0],cle[1])
                destx = cle[0] * 20
                desty = cle[1] * 20
                pygamewindow.blit(list_guardian.image,(destx,desty))

        for cle, valeur in self.dict_labyrinthe.items():
            if valeur == "a":
                list_wall.insertposition(cle[0],cle[1])
                destx = cle[0] * 20
                desty = cle[1] * 20
                pygamewindow.blit(list_object1.image,(destx,desty))

        for cle, valeur in self.dict_labyrinthe.items():
            if valeur == "b":
                list_wall.insertposition(cle[0],cle[1])
                destx = cle[0] * 20
                desty = cle[1] * 20
                pygamewindow.blit(list_object2.image,(destx,desty))