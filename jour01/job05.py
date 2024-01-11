# Définition de la classe Point avec une méthode d'initialisation (__init__) 
# qui prend deux paramètres (x et y).
class Point:
    
    def __init__(self, x, y):
        # Initialise la classe avec les coordonnées spécifiées.
        self.x = x  # Attribut de la classe pour stocker la coordonnée x
        self.y = y  # Attribut de la classe pour stocker la coordonnée y

    # Méthode pour afficher les coordonnées du point.
    def afficherLesPoints(self):
        print(f"Coordonnées: ({self.x}, {self.y})")

    # Méthode pour afficher la coordonnée x du point.
    def afficherX(self):
        print(f"X-Coordonnée: {self.x}")

    # Méthode pour afficher la coordonnée y du point.
    def afficherY(self):
        print(f"Y-Coordonnée: {self.y}")

    # Méthode pour changer la coordonnée x du point.
    def changerX(self, new_x):
        self.x = new_x

    # Méthode pour changer la coordonnée y du point.
    def changerY(self, new_y):
        self.y = new_y


# Création d'une instance de la classe Point avec les coordonnées (6, 8).
cord = Point(6, 8)

# Appel des méthodes pour afficher les coordonnées, la coordonnée x et la coordonnée y du point.
cord.afficherLesPoints()
cord.afficherX()
cord.afficherY()

# Changement des coordonnées x et y du point.
cord.changerX(2)
cord.changerY(12)

# Affichage des nouvelles coordonnées du point.
cord.afficherLesPoints()
