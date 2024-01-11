class Rectangle:
    def __init__(self, longueur, largeur):
        self._longueur = longueur
        self._largeur = largeur

    def get_longueur(self):
        return self._longueur

    def get_largeur(self):
        return self._largeur

    def set_longueur(self, longueur):
        self._longueur = longueur

    def set_largeur(self, largeur):
        self._largeur = largeur

mon_rectangle = Rectangle(10, 5)

print("Longueur:", mon_rectangle.get_longueur())
print("Largeur:", mon_rectangle.get_largeur())

mon_rectangle.set_longueur(15)
mon_rectangle.set_largeur(8)

print("Nouvelle longueur:", mon_rectangle.get_longueur())
print("Nouvelle largeur:", mon_rectangle.get_largeur())
