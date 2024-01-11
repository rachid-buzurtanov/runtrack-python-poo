import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        degats = random.randint(5, 15)  # Simule des dégâts aléatoires entre 5 et 15
        adversaire.vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts.")

class Jeu:
    def __init__(self):
        self.niveau = 1

    def choisir_niveau(self):
        self.niveau = int(input("Choisissez le niveau de difficulté (1 facile, 2 moyen, 3 difficile) : "))

    def lancer_jeu(self):
        joueur = Personnage("Joueur", self.niveau * 20)  # Les points de vie du joueur dépendent du niveau
        ennemi = Personnage("Ennemi", self.niveau * 15)  # Les points de vie de l'ennemi dépendent du niveau

        print(f"\nDébut du combat ! Niveau {self.niveau}")
        print(f"{joueur.nom} a {joueur.vie} points de vie.")
        print(f"{ennemi.nom} a {ennemi.vie} points de vie.\n")

        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi)
            print(f"{joueur.nom} a {joueur.vie} points de vie.")
            print(f"{ennemi.nom} a {ennemi.vie} points de vie.\n")

            if ennemi.vie <= 0:
                print(f"{ennemi.nom} est vaincu ! {joueur.nom} a gagné.")
                break

            ennemi.attaquer(joueur)
            print(f"{joueur.nom} a {joueur.vie} points de vie.")
            print(f"{ennemi.nom} a {ennemi.vie} points de vie.\n")

            if joueur.vie <= 0:
                print(f"{joueur.nom} a été vaincu ! {ennemi.nom} a gagné.")
                break

# Création du jeu
jeu = Jeu()

# Choix du niveau de difficulté
jeu.choisir_niveau()

# Lancement du jeu
jeu.lancer_jeu()
