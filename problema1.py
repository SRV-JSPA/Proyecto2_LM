import itertools

class Literal:
    def __init__(self, variable, negated=False):
        self.variable = variable
        self.negated = negated

    def __repr__(self):
        return f'¬{self.variable}' if self.negated else str(self.variable)


