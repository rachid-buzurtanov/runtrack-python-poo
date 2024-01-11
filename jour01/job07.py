class Personnage:
    def __init__(self, x, y):
        # Initialise la classe avec les coordonnées x et y du personnage
        self.x = x
        self.y = y

    def gauche(self):
        # Méthode qui déplace le personnage d'une unité vers la gauche
        self.x -= 1

    def droite(self):
        # Méthode qui déplace le personnage d'une unité vers la droite
        self.x += 1

    def haut(self):
        # Méthode qui déplace le personnage d'une unité vers le haut
        self.y -= 1

    def bas(self):
        # Méthode qui déplace le personnage d'une unité vers le bas
        self.y += 1

    def position(self):
        # Méthode qui renvoie les coordonnées actuelles du personnage
        return (self.x, self.y)

# Crée une instance de la classe Personnage avec les coordonnées initiales (0, 0)
personnage = Personnage(0, 0)

# Déplace le personnage vers la droite et affiche la nouvelle position
personnage.droite()
print("Position après déplacement vers la droite :", personnage.position())

# Déplace le personnage vers le haut et affiche la nouvelle position
personnage.haut()
print("Position après déplacement vers le haut :", personnage.position())

# Déplace le personnage vers la gauche et affiche la nouvelle position
personnage.gauche()
print("Position après déplacement vers la gauche :", personnage.position())

# Déplace le personnage vers le bas et affiche la nouvelle position
personnage.bas()
print("Position après déplacement vers le bas :", personnage.position())
