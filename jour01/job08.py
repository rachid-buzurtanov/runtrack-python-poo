import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon

    def afficherInfos(self):
        print(f"Cercle de rayon {self.rayon}")

    def circonference(self):
        return 2 * math.pi * self.rayon

    def aire(self):
        return math.pi * (self.rayon ** 2)

    def diametre(self):
        return 2 * self.rayon

# Créer deux cercles
cercle1 = Cercle(4)
cercle2 = Cercle(7)

# Afficher les informations pour chaque cercle
cercle1.afficherInfos()
cercle2.afficherInfos()

# Afficher la circonférence pour chaque cercle
print(f"Circonférence du cercle 1: {cercle1.circonference()}")
print(f"Circonférence du cercle 2: {cercle2.circonference()}")

# Afficher le diamètre pour chaque cercle
print(f"Diamètre du cercle 1: {cercle1.diametre()}")
print(f"Diamètre du cercle 2: {cercle2.diametre()}")

# Afficher l'aire pour chaque cercle
print(f"Aire du cercle 1: {cercle1.aire()}")
print(f"Aire du cercle 2: {cercle2.aire()}")
