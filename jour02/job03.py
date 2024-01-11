from job02 import Livre
class Livre:
    def __init__(self, titre, auteur, nombre_de_pages):
        self._titre = titre
        self._auteur = auteur
        self._nombre_de_pages = nombre_de_pages
        self._disponible = True

    # Assesseurs (getters)
    def get_titre(self):
        return self._titre

    def get_auteur(self):
        return self._auteur

    def get_nombre_de_pages(self):
        return self._nombre_de_pages

    def get_disponible(self):
        return self._disponible

    # Mutateurs (setters)
    def set_titre(self, titre):
        self._titre = titre

    def set_auteur(self, auteur):
        self._auteur = auteur

    def set_nombre_de_pages(self, nombre_de_pages):
        if isinstance(nombre_de_pages, int) and nombre_de_pages > 0:
            self._nombre_de_pages = nombre_de_pages
        else:
            print("Erreur : Le nombre de pages doit être un entier positif.")

    # Méthode de vérification
    def verification(self):
        return self._disponible

    # Méthode d'emprunt
    def emprunter(self):
        if self.verification():
            print("Livre emprunté avec succès.")
            self._disponible = False
        else:
            print("Erreur : Le livre n'est pas disponible pour l'emprunt.")

    # Méthode de rendu
    def rendre(self):
        if not self.verification():
            print("Livre rendu avec succès.")
            self._disponible = True
        else:
            print("Erreur : Le livre n'a pas été emprunté.")

# Exemple d'utilisation
mon_livre = Livre("Titre du livre", "Auteur du livre", 200)

# Afficher les valeurs initiales
print("Disponibilité du livre:", mon_livre.verification())

# Emprunter le livre
mon_livre.emprunter()

# Vérifier la disponibilité après l'emprunt
print("Disponibilité du livre après l'emprunt:", mon_livre.verification())

# Rendre le livre
mon_livre.rendre()

# Vérifier la disponibilité après le rendu
print("Disponibilité du livre après le rendu:", mon_livre.verification())
