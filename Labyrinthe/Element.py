import pygame
import random


class Element:

    """For each element in dictionnary (letter) give image and position
    Use to display"""

    dictionnary = {"w": "wall.png", "m": "MacGyver.png", "a": "seringue.png", "b": "tube_plastique.png",
                   "c": "ether.png", "g": "Gardien.png", "-": "empty.png"}

    def __init__(self, letter):
        self.position = []
        self.letter = letter
        self.image = pygame.transform.scale(pygame.image.load(Element.dictionnary[letter]), [20, 20])

    def insertposition(self, positionx, positiony):
        self.position.append([positionx, positiony])


class Player:
    """Use to check position character and objects"""

    def __init__(self, dictionnary):
        self.positionx, self.positiony = self.checkposition(dictionnary)
        self.listobjects = set()

    def checkposition(self, dictionnary):
        """
        return macgyver position
        """
        for cle, valeur in dictionnary.dict_labyrinthe.items():
            if valeur == "m":
                return cle

    def checkguardianposition(self, dictionnary):
        """
        return guardian position
        """
        for cle, valeur in dictionnary.dict_labyrinthe.items():
            if valeur == "g":
                return cle

    def checkobject(self, dictionnary):
        """
        if macgyver is in the same position of objectX
        add this object to set "listobjects"
        """
        if self.checkposition() == dictionnary.object1[0]:
            self.listobjects.add(dictionnary.object1[1])
        if self.checkposition() == dictionnary.object2[0]:
            self.listobjects.add(dictionnary.object2[1])
        if self.checkposition() == dictionnary.object3[0]:
            self.listobjects.add(dictionnary.object3[1])

    def checkallobjects(self):
        """
        return True if macgyver found 3 objects
        """
        if len(self.listobjects) == 3:
            return True
        else:
            return False

class Dictionnary:
    """generate differents objects who used a dictionnary to found position"""

    def __init__(self):
        self.dict_labyrinthe = {}
        self.object1 = []
        self.object2 = []
        self.object3 = []
        self.generatedictionnary()
        self.generateobject()

    def generatedictionnary(self):
        '''
        Generate a dictionnary from file.txt
        '''
        my_file = open("labyrinthe.txt", "r")
        text = my_file.read()

        nb_lettre = 15
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
        '''
        generate 3 objects in random position in dictionnary
        '''
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
        """
        for each letter display image in good position
        display the window game
        """
        list_wall = Element("w")
        list_gyver = Element("m")
        list_guardian = Element("g")
        list_object1 = Element("a")
        list_object2 = Element("b")
        list_object3 = Element("c")

        for cle, valeur in self.dict_labyrinthe.items():
            if valeur == "w":
                list_wall.insertposition(cle[0], cle[1])
                destx = cle[0] * 20
                desty = cle[1] * 20
                pygamewindow.blit(list_wall.image, (destx, desty))
            if valeur == "m":
                list_gyver.insertposition(cle[0], cle[1])
                destx = cle[0] * 20
                desty = cle[1] * 20
                pygamewindow.blit(list_gyver.image, (destx, desty))
            if valeur == "g":
                list_guardian.insertposition(cle[0], cle[1])
                destx = cle[0] * 20
                desty = cle[1] * 20
                pygamewindow.blit(list_guardian.image, (destx, desty))
            if valeur == "a":
                list_object1.insertposition(cle[0], cle[1])
                destx = cle[0] * 20
                desty = cle[1] * 20
                pygamewindow.blit(list_object1.image, (destx, desty))
            if valeur == "b":
                list_object2.insertposition(cle[0], cle[1])
                destx = cle[0] * 20
                desty = cle[1] * 20
                pygamewindow.blit(list_object2.image, (destx, desty))
            if valeur == "c":
                list_object3.insertposition(cle[0], cle[1])
                destx = cle[0] * 20
                desty = cle[1] * 20
                pygamewindow.blit(list_object3.image, (destx, desty))