from sympy.logic.boolalg import Implies, Not, Or
from sympy import symbols, simplify

# Definición de símbolos para las proposiciones lógicas P, Q y R.
P, Q, R = symbols('P Q R')


# Función para aplicar Modus Ponens
def modus_ponens(implication, premise):
    # Aplica el Modus Ponens a una implicación dada la premisa verdadera.

    if premise:
        # Realiza la sustitución en la implicación si la premisa es verdadera.
        return implication.subs({P: True})
    return None


# Función para aplicar Modus Tollens
def modus_tollens(implication, conclusion):
    # Aplica el Modus Tollens a una implicación dada la falsedad de la conclusión.

    if not conclusion:
        # Devuelve la negación del antecedente si la conclusión es falsa.
        return Not(implication.args[0])
    return None


# Función para demostrar Resolución
def resolution(clause1, clause2):
    """
    Aplica la resolución entre dos cláusulas para deducir una nueva cláusula o determinar una tautología.

    Parameters:
    clause1 (Or): La primera cláusula lógica.
    clause2 (Or): La segunda cláusula lógica.

    Returns:
    Expression/bool: La nueva cláusula deducida; True si resulta en una tautología; False si no se puede resolver.
    """
    # Extraer todos los literales de ambas cláusulas.
    literals1 = set(clause1.args)
    literals2 = set(clause2.args)

    # Buscar literales opuestos en las cláusulas.
    for lit in literals1:
        if Not(lit) in literals2:
            # Formar una nueva cláusula sin los literales opuestos.
            new_literals = literals1.union(literals2) - {lit, Not(lit)}
            if not new_literals:
                # Retorna True si la nueva cláusula es una tautología (vacía).
                return True
            # Retorna la nueva cláusula combinada.
            return Or(*new_literals)
    # Retorna False si no hay literales opuestos para resolver.
    return False


# Definición de implicaciones lógicas.
implication_pq = Implies(P, Q)
implication_qr = Implies(Q, R)

# Ejemplo de uso de Modus Ponens.
premise_p = True  # P es verdadero.
conclusion_q = modus_ponens(implication_pq, premise_p)  # Aplicar Modus Ponens.
print(f"Modus Ponens: {conclusion_q}")

# Ejemplo de uso de Modus Tollens.
conclusion_not_p = modus_tollens(implication_pq, False)  # Q es falso.
print(f"Modus Tollens: {conclusion_not_p}")

# Ejemplo de uso de Resolución.
clause1 = Or(Not(P), Q)
clause2 = Or(P, Not(Q))

# Llamada a la función de resolución.
resolved = resolution(clause1, clause2)
print(f"Resolución: {resolved}")
