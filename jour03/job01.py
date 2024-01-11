class Ville:
    def __init__(self, nom, nombre_habitants):
        self._nom = nom
        self._nombre_habitants = nombre_habitants

    def get_nom(self):
        return self._nom

    def get_nombre_habitants(self):
        return self._nombre_habitants

    def augmenter_population(self):
        self._nombre_habitants += 1


class Personne:
    def __init__(self, nom, age, ville):
        self._nom = nom
        self._age = age
        self._ville = ville
        # Augmenter la population de la ville lors de la création d'une personne
        self._ville.augmenter_population()

    def ajouter_population(self):
        self._ville.augmenter_population()


# Création des objets Ville
paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

# Affichage du nombre d'habitants de chaque ville
print(f"Nombre d'habitants à {paris.get_nom()}: {paris.get_nombre_habitants()}")
print(f"Nombre d'habitants à {marseille.get_nom()}: {marseille.get_nombre_habitants()}")

# Création des objets Personne
john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

# Affichage du nombre d'habitants après l'arrivée de nouvelles personnes
print("\nAprès l'arrivée de nouvelles personnes :")
print(f"Nombre d'habitants à {paris.get_nom()}: {paris.get_nombre_habitants()}")
print(f"Nombre d'habitants à {marseille.get_nom()}: {marseille.get_nombre_habitants()}")
