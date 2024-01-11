class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquer_un_but(self):
        self.buts_marques += 1
        print(f"{self.nom} a marqué un but!")

    def effectuer_une_passe_decisive(self):
        self.passes_decisives += 1
        print(f"{self.nom} a effectué une passe décisive!")

    def recevoir_un_carton_jaune(self):
        self.cartons_jaunes += 1
        print(f"{self.nom} a reçu un carton jaune.")

    def recevoir_un_carton_rouge(self):
        self.cartons_rouges += 1
        print(f"{self.nom} a reçu un carton rouge et est exclu du match.")

    def afficher_statistiques(self):
        print(f"\nStatistiques de {self.nom} (Joueur n°{self.numero}):")
        print(f"Position: {self.position}")
        print(f"Buts marqués: {self.buts_marques}")
        print(f"Passes décisives: {self.passes_decisives}")
        print(f"Cartons jaunes: {self.cartons_jaunes}")
        print(f"Cartons rouges: {self.cartons_rouges}")


class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouter_joueur(self, joueur):
        self.joueurs.append(joueur)

    def afficher_statistiques_joueurs(self):
        print(f"\nStatistiques des joueurs de l'équipe {self.nom}:")
        for joueur in self.joueurs:
            joueur.afficher_statistiques()

    def mettre_a_jour_statistiques_joueur(self, nom_joueur, action):
        for joueur in self.joueurs:
            if joueur.nom == nom_joueur:
                if action == "but":
                    joueur.marquer_un_but()
                elif action == "passe_decisive":
                    joueur.effectuer_une_passe_decisive()
                elif action == "carton_jaune":
                    joueur.recevoir_un_carton_jaune()
                elif action == "carton_rouge":
                    joueur.recevoir_un_carton_rouge()
                else:
                    print("Action non reconnue.")
                return
        print(f"Joueur '{nom_joueur}' non trouvé dans l'équipe.")


# Création des joueurs
joueur1 = Joueur("Messi", 10, "Attaquant")
joueur2 = Joueur("Ronaldo", 7, "Attaquant")
joueur3 = Joueur("Neymar", 11, "Attaquant")
joueur4 = Joueur("Iniesta", 8, "Milieu")
joueur5 = Joueur("Ramos", 4, "Défenseur")

# Création des équipes
equipe1 = Equipe("Barcelone")
equipe2 = Equipe("Real Madrid")

# Ajout des joueurs aux équipes
equipe1.ajouter_joueur(joueur1)
equipe1.ajouter_joueur(joueur4)
equipe2.ajouter_joueur(joueur2)
equipe2.ajouter_joueur(joueur3)
equipe2.ajouter_joueur(joueur5)

# Affichage des statistiques des joueurs avant le match
equipe1.afficher_statistiques_joueurs()
equipe2.afficher_statistiques_joueurs()

# Simuler un match
equipe1.mettre_a_jour_statistiques_joueur("Messi", "but")
equipe1.mettre_a_jour_statistiques_joueur("Messi", "passe_decisive")
equipe2.mettre_a_jour_statistiques_joueur("Ronaldo", "but")
equipe2.mettre_a_jour_statistiques_joueur("Neymar", "carton_jaune")
equipe2.mettre_a_jour_statistiques_joueur("Ramos", "carton_rouge")

# Affichage des statistiques des joueurs après le match
equipe1.afficher_statistiques_joueurs()
equipe2.afficher_statistiques_joueurs()
