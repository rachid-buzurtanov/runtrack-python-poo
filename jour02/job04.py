class Student:
    def __init__(self, nom, prenom, numero_etudiant):
        self._nom = nom
        self._prenom = prenom
        self._numero_etudiant = numero_etudiant
        self._credits = 0
        self._level = self._student_eval()

    # Assesseurs (getters)
    def get_nom(self):
        return self._nom

    def get_prenom(self):
        return self._prenom

    def get_numero_etudiant(self):
        return self._numero_etudiant

    def get_credits(self):
        return self._credits

    def get_level(self):
        return self._level

    # Mutateur (setter)
    def add_credits(self, nombre_credits):
        if nombre_credits > 0:
            self._credits += nombre_credits
            self._level = self._student_eval()
            print(f"{nombre_credits} crédits ajoutés avec succès.")
        else:
            print("Erreur : Le nombre de crédits doit être supérieur à zéro.")

    # Méthode d'évaluation privée
    def _student_eval(self):
        if self._credits >= 90:
            return "Excellent"
        elif self._credits >= 80:
            return "Très bien"
        elif self._credits >= 70:
            return "Bien"
        elif self._credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    # Méthode d'affichage des informations de l'étudiant
    def student_info(self):
        print(f"Nom: {self._nom}")
        print(f"Prénom: {self._prenom}")
        print(f"Numéro d'étudiant: {self._numero_etudiant}")
        print(f"Total de crédits: {self._credits}")
        print(f"Niveau d'évaluation: {self._level}")

# Instanciation de l'objet représentant l'étudiant John Doe
john_doe = Student("Doe", "John", 145)

# Ajout de crédits à trois reprises
john_doe.add_credits(30)
john_doe.add_credits(25)
john_doe.add_credits(15)

# Affichage des informations de l'étudiant
john_doe.student_info()
