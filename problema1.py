import itertools

class Literal:
    def __init__(self, variable, negated=False):
        self.variable = variable
        self.negated = negated

    def __repr__(self):
        return f'¬{self.variable}' if self.negated else str(self.variable)


class Clause:
    def __init__(self, literals):
        self.literals = literals  # lista de Literales

    def is_satisfied(self, valuation):
        # Verificar si al menos un literal en la cláusula es verdadero
        return any((not literal.negated and valuation[literal.variable]) or
                   (literal.negated and not valuation[literal.variable]) for literal in self.literals)

class Formula:
    def __init__(self, clauses):
        self.clauses = clauses  # lista de Cláusulas

    def is_satisfiable(self):
        # Extraer todas las variables de la fórmula
        variables = set()
        for clause in self.clauses:
            for literal in clause.literals:
                variables.add(literal.variable)

        # Generar todas las asignaciones posibles
        n = len(variables)
        all_assignments = list(itertools.product([False, True], repeat=n))

        # Probar cada asignación
        for assignment in all_assignments:
            # Crear un diccionario que asocia variables con su valor de verdad
            valuation = dict(zip(variables, assignment))

            # Verificar si la fórmula es satisfacible bajo la asignación actual
            if all(clause.is_satisfied(valuation) for clause in self.clauses):
                return True, valuation

        return False, None

# Fórmula: (p OR q) AND (NOT p OR r) AND (NOT q OR NOT r)
#p=1
#q=2
#r=3
# La represento como: [{1, 2}, {-1, 3}, {-2, -3}]
clauses = [
    Clause([Literal(1), Literal(2)]),  # p OR q
    Clause([Literal(1, negated=True), Literal(3)]),  # NOT p OR r
    Clause([Literal(2, negated=True), Literal(3, negated=True)])  # NOT q OR NOT r
]

formula = Formula(clauses)
result, assignment = formula.is_satisfiable()

if result:
    print("La fórmula es satisfacible con la asignación:", assignment)
else:
    print("La fórmula no es satisfacible.")