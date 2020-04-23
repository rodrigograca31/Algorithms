#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    n = 0
    for ingredient, quantity in recipe.items():
        if ingredient not in ingredients:
            return 0
        else:
            if ingredients[ingredient] // recipe[ingredient] == 0:
                return 0
            if n > ingredients[ingredient] // recipe[ingredient] or n == 0:
                n = ingredients[ingredient] // recipe[ingredient]
    return n


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 232, 'butter': 100, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
