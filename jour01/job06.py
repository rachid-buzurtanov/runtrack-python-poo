class Animal:
    def __init__(self):
        # Méthode d'initialisation, définit les valeurs par défaut lorsqu'un objet est créé
        self.age = 3
        self.nomanimal = ""

    def vieillir(self):
        # Méthode pour faire vieillir l'animal en incrémentant son attribut d'âge
        self.age += 1

    def nommer(self, nom):
        # Méthode pour attribuer un nom à l'animal en mettant à jour son attribut nomanimal
        self.nomanimal = nom

# Créer une instance de la classe Animal
animal = Animal()

# Afficher l'âge initial de l'animal
print("Âge de l'animal :", animal.age)

# Faire vieillir l'animal et afficher son âge mis à jour
animal.vieillir()
print("L'âge de l'animal après vieillissement :", animal.age)

# Donner un nom à l'animal et afficher son nom
animal.nommer("Rechel")
print("Nom de l'animal :", animal.nomanimal)
