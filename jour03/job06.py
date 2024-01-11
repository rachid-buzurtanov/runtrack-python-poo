class Commande:
    def __init__(self, numero_commande):
        self._numero_commande = numero_commande
        self._plats_commandes = {}
        self._statut_commande = "en cours"

    # Méthode privée pour calculer le total d'une commande
    def _calculer_total(self):
        total = sum(plat['prix'] for plat in self._plats_commandes.values())
        return total

    # Méthode privée pour calculer la TVA
    def _calculer_tva(self):
        tva = self._calculer_total() * 0.2  # Exemple : TVA de 20%
        return tva

    # Méthode pour ajouter un plat à la commande
    def ajouter_plat(self, nom_plat, prix_plat):
        if nom_plat not in self._plats_commandes:
            self._plats_commandes[nom_plat] = {'prix': prix_plat, 'statut': 'en cours'}
            print(f"Plat '{nom_plat}' ajouté à la commande.")
        else:
            print(f"Erreur : Le plat '{nom_plat}' est déjà dans la commande.")

    # Méthode pour annuler une commande
    def annuler_commande(self):
        if self._statut_commande == "en cours":
            self._statut_commande = "annulée"
            print("La commande a été annulée.")
        else:
            print("Erreur : Impossible d'annuler une commande déjà terminée ou annulée.")

    # Méthode pour afficher la commande avec son total à payer
    def afficher_commande(self):
        total = self._calculer_total()
        tva = self._calculer_tva()
        total_a_payer = total + tva
        print("\nDétails de la commande:")
        print(f"Numéro de commande : {self._numero_commande}")
        print("Plats commandés :")
        for nom_plat, plat_info in self._plats_commandes.items():
            print(f"  - {nom_plat} : {plat_info['prix']} € ({plat_info['statut']})")
        print(f"Total : {total} €")
        print(f"TVA (20%) : {tva} €")
        print(f"Total à payer : {total_a_payer} €")
        print(f"Statut de la commande : {self._statut_commande}")

# Exemple d'utilisation
commande1 = Commande(1)

# Ajouter des plats à la commande
commande1.ajouter_plat("Pizza Margherita", 12)
commande1.ajouter_plat("Salade César", 8)
commande1.ajouter_plat("Pâtes Bolognaises", 10)

# Afficher la commande
commande1.afficher_commande()

# Annuler la commande
commande1.annuler_commande()

# Afficher la commande après annulation
commande1.afficher_commande()
