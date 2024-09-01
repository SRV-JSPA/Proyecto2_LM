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

