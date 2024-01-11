class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde_initial, decouvert=False):
        self._numero_compte = numero_compte
        self._nom = nom
        self._prenom = prenom
        self._solde = solde_initial
        self._decouvert = decouvert

    def afficher(self):
        print(f"Compte n°{self._numero_compte} - {self._nom} {self._prenom}")
        print(f"Solde : {self._solde} €")
        if self._decouvert:
            print("Le découvert est autorisé.")
        else:
            print("Le découvert n'est pas autorisé.")

    def afficher_solde(self):
        print(f"Solde actuel : {self._solde} €")

    def versement(self, montant):
        if montant > 0:
            self._solde += montant
            print(f"Versement de {montant} € effectué.")
        else:
            print("Erreur : Le montant du versement doit être supérieur à zéro.")

    def retrait(self, montant):
        if self._solde >= montant or self._decouvert:
            self._solde -= montant
            print(f"Retrait de {montant} € effectué. Nouveau solde : {self._solde} €")
        else:
            print("Erreur : Solde insuffisant et découvert non autorisé.")

    def agios(self, taux_agios):
        if self._solde < 0:
            agios = abs(self._solde) * taux_agios
            self._solde -= agios
            print(f"Des agios de {agios} € ont été appliqués. Nouveau solde : {self._solde} €")
        else:
            print("Pas d'agios à appliquer, le solde est positif.")

    def virement(self, compte_destinataire, montant):
        if montant > 0 and self._solde >= montant:
            self._solde -= montant
            compte_destinataire.versement(montant)
            print(f"Virement de {montant} € effectué vers le compte {compte_destinataire._numero_compte}.")
        else:
            print("Erreur : Montant invalide ou solde insuffisant pour effectuer le virement.")


# Création du premier compte avec un solde initial de 1000€
compte1 = CompteBancaire(1, "Dupont", "Jean", 1000)

# Affichage des détails du compte
compte1.afficher()

# Versement de 500€
compte1.versement(500)

# Retrait de 200€
compte1.retrait(200)

# Affichage du solde
compte1.afficher_solde()

# Création du deuxième compte avec un solde initial de -500€ autorisant le découvert
compte2 = CompteBancaire(2, "Martin", "Sophie", -500, decouvert=True)

# Affichage des détails du compte à découvert
compte2.afficher()

# Versement de 1000€ depuis le premier compte vers le deuxième (pour le remettre à zéro)
compte1.virement(compte2, 1000)

# Affichage des détails des deux comptes après le virement
compte1.afficher()
compte2.afficher()
