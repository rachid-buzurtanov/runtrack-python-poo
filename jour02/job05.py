class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self._marque = marque
        self._modele = modele
        self._annee = annee
        self._kilometrage = kilometrage
        self._en_marche = False
        self._reservoir = 50

    # Assesseurs (getters)
    def get_marque(self):
        return self._marque

    def get_modele(self):
        return self._modele

    def get_annee(self):
        return self._annee

    def get_kilometrage(self):
        return self._kilometrage

    def get_en_marche(self):
        return self._en_marche

    def get_reservoir(self):
        return self._reservoir

    # Mutateurs (setters)
    def set_marque(self, marque):
        self._marque = marque

    def set_modele(self, modele):
        self._modele = modele

    def set_annee(self, annee):
        self._annee = annee

    def set_kilometrage(self, kilometrage):
        self._kilometrage = kilometrage

    # Méthode pour démarrer la voiture
    def demarrer(self):
        if self._verifier_plein():
            self._en_marche = True
            print("La voiture a démarré.")
        else:
            print("La voiture ne peut pas démarrer, le réservoir est trop bas.")

    # Méthode pour arrêter la voiture
    def arreter(self):
        self._en_marche = False
        print("La voiture a été arrêtée.")

    # Méthode privée pour vérifier le niveau de carburant
    def _verifier_plein(self):
        return self._reservoir > 5

# Exemple d'utilisation
ma_voiture = Voiture("Toyota", "Corolla", 2022, 15000)

# Afficher les valeurs initiales
print("Marque:", ma_voiture.get_marque())
print("Modèle:", ma_voiture.get_modele())
print("Année:", ma_voiture.get_annee())
print("Kilométrage:", ma_voiture.get_kilometrage())
print("En marche:", ma_voiture.get_en_marche())
print("Reservoir:", ma_voiture.get_reservoir())

# Démarrer la voiture
ma_voiture.demarrer()

# Afficher les valeurs après démarrage
print("\nAprès démarrage:")
print("En marche:", ma_voiture.get_en_marche())
print("Reservoir:", ma_voiture.get_reservoir())

# Arrêter la voiture
ma_voiture.arreter()

# Afficher les valeurs après arrêt
print("\nAprès arrêt:")
print("En marche:", ma_voiture.get_en_marche())
print("Reservoir:", ma_voiture.get_reservoir())
