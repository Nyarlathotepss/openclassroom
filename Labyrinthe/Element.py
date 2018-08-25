class Element:

    def __init__(self):
        self.positionx = int
        self.positiony = int


class Player(Element):

    def checkposition(self):
        for cle,valeur in dict_labyrinthe.items():
            if valeur == "m":
                return cle

class Block(pygame.sprite.Sprite):

        # Constructor. Pass in the color of the block,
        # and its x and y position
        def __init__(self, color, width, height):
            # Call the parent class (Sprite) constructor
            pygame.sprite.Sprite.__init__(self)

            # Create an image of the block, and fill it with a color.
            # This could also be an image loaded from the disk.
            self.image = pygame.Surface([width, height])
            self.image.fill(color)

            # Fetch the rectangle object that has the dimensions of the image
            # Update the position of this object by setting the values of rect.x and rect.y
            self.rect = self.image.get_rect()
            
class Dictionnary:
    
    def __init__(self):
        '''By default my dictionnary is empty'''
        self.name = ""
    
    def generatedictionnary(self):
        ''' Generate a dictionnary with file.txt'''
        my_file = open("labyrinthe.txt", "r")
        text = my_file.read()
        dict_labyrinthe = {}
        nb_lettre = 0  # Bloc pour compter le nombre de lettre dans une ligne
            key1 = 0
            key2 = 0
        for lettre in text:
            nb_lettre += 1
            if lettre == "\n":
            nb_lettre -= 1  # Ici on enleve le saut de ligne \n du comptage de lettre
            break
        for lettre in text:
            if lettre != "\n":
                dict_labyrinthe[key1,key2] = lettre
                key1 += 1
                if key1 == nb_lettre:
                    key1 = 0
                    key2 += 1
                    
        def generateobject(self):
            '''generate 3 objects in random position in dictionnary'''
            list_empty_case = []
            for cle,valeur in dict_labyrinthe.items():
                if valeur == "-":
                list_empty_case.append(cle)
            position_object1 = random.choice(list_empty_case)
            position_object2 = random.choice(list_empty_case)
            position_object3 = random.choice(list_empty_case)
            dict_labyrinthe[position_object1] = "a"
            dict_labyrinthe[position_object2] = "b"
            dict_labyrinthe[position_object3] = "c"
            
