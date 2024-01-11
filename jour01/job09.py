class Produit:

    def __init__(self, nom, prixHT, TVA=20):
    # Initialise la classe avec (nom, prixHT, TVA=20) où nom est le nom du produit, prixHT est le prix hors taxes et TVA est le taux de TVA par défaut à 20%.
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def calculerPrixTTC(self):
    # Cette méthode calcule le prix TTC en utilisant le taux de TVA.
        prixTTC = self.prixHT * (1 + self.TVA / 100)
        return prixTTC

    def afficher(self):
    # La méthode afficher retourne une représentation sous forme de chaîne de caractères de l'objet.
        return str(self)

    def modifierNom(self, nouveauNom):
    # Les méthodes modifierNom et modifierPrixHT permettent de mettre à jour les attributs nom et prixHT.
        self.nom = nouveauNom

    def modifierPrixHT(self, nouveauPrixHT):
        self.prixHT = nouveauPrixHT

    def getNom(self):
    # Les méthodes getNom, getPrixHT et getTVA permettent d'obtenir les valeurs des attributs.
        return self.nom

    def getPrixHT(self):
        return self.prixHT

    def getTVA(self):
        return self.TVA

    def __str__(self):
    # La méthode spéciale __str__ retourne une représentation sous forme de chaîne de caractères de l'objet.
        return f"Nom: {self.nom}, Prix HT: {self.prixHT}, TVA: {self.TVA}%, Prix TTC: {self.calculerPrixTTC()}"

# Création d'instances de la classe Produit.
produit1 = Produit("Samsung S24", 999.99)
produit2 = Produit("DLC Destiny 2", 99.99)
produit3 = Produit("Asus Zephyrus G15 ", 1499.99)

print("Informations initiales des produits:")
# Affichage des informations initiales des produits.
print(produit1.afficher())
print(produit2.afficher())
print(produit3.afficher())

# Modification des attributs des produits.
produit1.modifierNom("Iphone 15")
produit1.modifierPrixHT(1111.0)

produit2.modifierNom("Huawei P50")
produit2.modifierPrixHT(899.99)

produit3.modifierNom("God of War 2022")
produit3.modifierPrixHT(79.99)

print("Informations après modification:")
# Affichage des informations après modification.
print(produit1.afficher())
print(produit2.afficher())
print(produit3.afficher())
