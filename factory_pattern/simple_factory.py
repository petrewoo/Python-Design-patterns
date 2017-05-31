#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from .pizza import *
from .ingredient_factory import IngredientFactory


class SimpleIngredientFactory(object):

    @staticmethod
    def create():
        return IngredientFactory()


class SimplePizzaFactory(object):

    @staticmethod
    def create(pizza_type):
        ingredient_factory = SimpleIngredientFactory.create()
        if pizza_type == 'cheese':
            return CheesePizza(ingredient_factory)
        elif pizza_type == 'pepperoni':
            return PopperoniPizza(ingredient_factory)
        elif pizza_type == 'clam':
            return ClamPizza(ingredient_factory)
        elif pizza_type == 'veggie':
            return VeggiePizza(ingredient_factory)


class SimplePizzaStore(object):

    def __init__(self, pizza_factory):
        self._pizza_factory = pizza_factory

    def order_pizza(self, pizza_type):
        pizza = self._pizza_factory.create(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()


if __name__ == '__main__':
    pizza_store = SimplePizzaStore(SimplePizzaFactory)
    pizza_store.order_pizza('cheese')
    pizza_store.order_pizza('clam')
