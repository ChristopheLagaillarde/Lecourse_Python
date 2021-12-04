import sys

class ParieNonValideException(Exception):
    def __init__(self):
        super().__init__()

try:
    def factoriel(nombre):
        for i in range(1, nombre):
            nombre *= i
        return nombre


    n = int(input("Saisir le nombre de cheval partant"))
    p = int(input("Saisir le nombre de cheval joué"))

    if n < p:
        raise ParieNonValideException()

    X = factoriel(n) // factoriel(n - p)
    Y = float(factoriel(n) // (factoriel(p) * factoriel(n - p)))

    print("Dans l'ordre vous avez", 1/X, "de gagner")
    print("Dans le désordre vous avez", 1/Y, "de gagner")

except ValueError:
    print("Saisie non valide")

except ParieNonValideException:
    print("Parie non valide")

