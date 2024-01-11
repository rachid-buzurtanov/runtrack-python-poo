class Livre:
    def __init__(self, titre, auteur, nombre_de_pages):
        self._titre = titre
        self._auteur = auteur
        self._nombre_de_pages = nombre_de_pages

    # Assesseurs (getters)
    def get_titre(self):
        return self._titre

    def get_auteur(self):
        return self._auteur

    def get_nombre_de_pages(self):
        return self._nombre_de_pages

    # Mutateurs (setters)
    def set_titre(self, titre):
        self._titre = titre

    def set_auteur(self, auteur):
        self._auteur = auteur

    def set_nombre_de_pages(self, nombre_de_pages):
        # Vérifier si le nombre de pages est un entier positif
        if isinstance(nombre_de_pages, int) and nombre_de_pages > 0:
            self._nombre_de_pages = nombre_de_pages
        else:
            print("Erreur : Le nombre de pages doit être un entier positif.")

# Exemple d'utilisation
mon_livre = Livre("Les Misérables", "Victor Hugo", 1630)

# Afficher les valeurs initiales
print("Titre:", mon_livre.get_titre())
print("Auteur:", mon_livre.get_auteur())
print("Nombre de pages:", mon_livre.get_nombre_de_pages())

# Modifier les valeurs
mon_livre.set_titre("Harry Potter")
mon_livre.set_auteur("J. K. Rowling")
mon_livre.set_nombre_de_pages(8888)  # Modifie le nombre de pages

# Afficher les valeurs modifiées
print("\nValeurs modifiées:")
print("Titre:", mon_livre.get_titre())
print("Auteur:", mon_livre.get_auteur())
print("Nombre de pages:", mon_livre.get_nombre_de_pages())

# Tentative de modifier le nombre de pages avec une valeur non valide
mon_livre.set_nombre_de_pages(-50)  # Affiche un message d'erreur
