class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

    def __str__(self):
        return f"{self.titre} - {self.description} - Statut: {self.statut}"

class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouter_tache(self, tache):
        self.taches.append(tache)

    def supprimer_tache(self, titre):
        self.taches = [t for t in self.taches if t.titre != titre]

    def marquer_comme_finie(self, titre):
        for t in self.taches:
            if t.titre == titre:
                t.statut = "terminée"
                print(f"Tâche '{titre}' marquée comme terminée.")
                return
        print(f"Erreur : Tâche '{titre}' non trouvée.")

    def afficher_liste(self):
        print("Liste des tâches:")
        for t in self.taches:
            print(t)

    def filter_liste(self, statut):
        filtered_list = [t for t in self.taches if t.statut == statut]
        return filtered_list

# Tester le code
tache1 = Tache("Faire les courses", "Acheter des fruits et légumes")
tache2 = Tache("Réviser pour l'examen", "Relire les chapitres 1 à 5")
tache3 = Tache("Faire du sport", "Courir pendant 30 minutes")

liste_taches = ListeDeTaches()

liste_taches.ajouter_tache(tache1)
liste_taches.ajouter_tache(tache2)
liste_taches.ajouter_tache(tache3)

# Afficher la liste des tâches
liste_taches.afficher_liste()

# Marquer une tâche comme terminée
liste_taches.marquer_comme_finie("Faire les courses")

# Afficher la liste mise à jour
liste_taches.afficher_liste()

# Filtrer les tâches par statut
taches_a_faire = liste_taches.filter_liste("à faire")
print("\nTâches à faire:")
for t in taches_a_faire:
    print(t)

# Supprimer une tâche
liste_taches.supprimer_tache("Réviser pour l'examen")

# Afficher la liste mise à jour après la suppression
liste_taches.afficher_liste()
