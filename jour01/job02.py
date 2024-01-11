# Définition de la classe Operation avec une méthode d'initialisation (__init__) 
# qui prend deux paramètres par défaut (nombre1 et nombre2).
class Operation:
    
    def __init__(self, nombre1=233, nombre2=728):
        # Initialise la classe avec les valeurs par défaut ou celles fournies en arguments.
        self.nombre1 = nombre1  # Attribut de la classe pour stocker la valeur de nombre1
        self.nombre2 = nombre2  # Attribut de la classe pour stocker la valeur de nombre2

# Création d'une instance de la classe Operation sans arguments, utilisant les valeurs par défaut.
operation_instance = Operation()

# Affichage de la valeur de nombre1 de l'instance créée.
print("Le nombre1 est :", operation_instance.nombre1)

# Affichage de la valeur de nombre2 de l'instance créée.
print("Le nombre2 est :", operation_instance.nombre2)
