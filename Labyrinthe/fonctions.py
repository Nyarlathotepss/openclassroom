dictionnary = {"w": "wall.png", "m": "MacGyver.png", "a": "seringue.png", "b": "tube_plastique.png", "c": "ether.png",
               "g": "Gardien.png", "-": "empty.png"}


def __init__(self, letter):
    self.number = []
    self.letter = letter
    self.image = pygame.transform.scale(pygame.image.load(Element.dictionnary[letter]), [20, 20])


def insertnumber(self, number):

    self.number.append(number)



def display_element(self, fenetre):

    test = Element()
    num = 0
    for valeur in self.dict_dictionnary:
        num +=1
        insertnumber(num)
        test.letter = valeur

