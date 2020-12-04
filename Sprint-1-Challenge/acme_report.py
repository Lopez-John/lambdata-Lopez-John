"""Generates an inventory report"""

from random import randint, sample, uniform
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    for i in range(0, num_products):
        prod = Product(
                        name=sample(ADJECTIVES, 1)[0] +
                        ' ' +
                        sample(NOUNS, 1)[0],
                        price=randint(5, 100),
                        weight=randint(5, 100),
                        flammability=uniform(0.0, 2.5))
        products.append(prod)
    return products


def inventory_report(products):
    prices = []
    weights = []
    flammabilities = []

    for i in products:
        prices.append(i.price)
        weights.append(i.price)
        flammabilities.append(i.flammability)

    mean_price = sum(prices) / len(prices)
    mean_weight = sum(weights) / len(weights)
    mean_flammability = sum(flammabilities) / len(flammabilities)

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('Unique product names: ', len(products))
    print('Average price: ', mean_price)
    print('Average weight: ', mean_weight)
    print('Average flammability ', mean_flammability)

if __name__ == '__main__':
    inventory_report(generate_products())
