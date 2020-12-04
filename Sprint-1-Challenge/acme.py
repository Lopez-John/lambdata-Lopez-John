"""Classes and fuctions for Sprint 1 Challege"""

from random import randint


class Product:
    def __init__(
                self,
                name,
                price=10,
                weight=20,
                flammability=0.5,
                identifier=randint(1000000, 9999999)):
        """Constructor for Product object"""
        self.name = str(name)
        self.price = int(price)
        self.weight = int(weight)
        self.flammability = float(flammability)
        self.identifier = identifier

    def stealability(self):
        """Calculates how 'stealable' a product is"""
        ratio = self.price / self.weight
        if ratio < 0.5:
            return 'Not so stealable...'
        elif ratio >= 1.0:
            return 'Very stealable!'
        else:
            return 'Kinda Stealable.'

    def explode(self):
        """Determine how explodable a product is"""
        explodable = self.flammability * self.weight
        if explodable < 10:
            return '...fizzle'
        elif explodable >= 50:
            return '...BABOOM!!'
        else:
            return '...boom!'


class BoxingGlove(Product):
    def __init__(
                self,
                name,
                price=10,
                weight=10,
                flammability=0.5,
                identifier=randint(1000000, 9999999)):
        """Constructor for a Boxing Glove"""
        super().__init__(name, price, weight, flammability, identifier)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return 'That tickles'
        elif self.weight >= 15:
            return 'OUCH!'
        else:
            return 'Hey that hurt!'
