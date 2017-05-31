#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from .pizza import *
from .ingredient_factory import IngredientFactory


class AbsPizzaStore(object):

    def order_pizza(self):
        raise NotImplementedError

    def _create(self):
        raise NotImplementedError

    def _ingredient(self):
        raise NotImplementedError


class PizzaStore(AbsPizzaStore):

    def order_pizza(self, pizza_type):
        self._ingredient()
        pizza = self._create(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

    def _create(self, pizza_type):
        raise NotImplementedError

    def _ingredient(self):
        raise NotImplementedError


class SimplePizzaStore(PizzaStore):

    def _create(self, pizza_type):
        if pizza_type == 'cheese':
            return CheesePizza(self.ingredient)
        elif pizza_type == 'pepperoni':
            return PepperoniPizza(self.ingredient)
        elif pizza_type == 'clam':
            return ClamPizza(self.ingredient)
        elif pizza_type == 'veggie':
            return VeggiePizza(self.ingredient)
        else:
            return Pizza(self._ingredient)

    def _ingredient(self):
        self.ingredient = IngredientFactory()


if __name__ == '__main__':
    sps = SimplePizzaStore()
    sps.order_pizza('cheese')
    sps.order_pizza('pepperoni')
