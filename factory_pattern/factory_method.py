#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from .pizza import *
from .pizza_store import *
from .ingredient_factory import (ChicagoPizzaIngredientFactory,
                                 NYPizzaIngredientFactory,
                                 CaliforniaPizzaIngredientFactory)


class ChicagoPizzaStore(PizzaStore):

    def _create(self, pizza_type):
        if pizza_type == 'cheese':
            return ChicagoStyleCheesePizza(self.ingredient)
        elif pizza_type == 'pepperoni':
            return ChicagoStylePepperoniPizza(self.ingredient)
        elif pizza_type == 'clam':
            return ChicagoStyleClamPizza(self.ingredient)
        elif pizza_type == 'veggie':
            return ChicagoStyleVeggiePizza(self.ingredient)
        else:
            return Pizza(self._ingredient)

    def _ingredient(self):
        self.ingredient = ChicagoPizzaIngredientFactory()


class NYPizzaStore(PizzaStore):

    def _create(self, pizza_type):
        if pizza_type == 'cheese':
            return NYStyleCheesePizza(self.ingredient)
        elif pizza_type == 'pepperoni':
            return NYStylePepperoniPizza(self.ingredient)
        elif pizza_type == 'clam':
            return NYStyleClamPizza(self.ingredient)
        elif pizza_type == 'veggie':
            return NYStyleVeggiePizza(self.ingredient)
        else:
            return Pizza(self.ingredient)

    def _ingredient(self):
        self.ingredient = NYPizzaIngredientFactory()


class CaliforniaPizzaStore(PizzaStore):

    def _create(self, pizza_type):
        if pizza_type == 'cheese':
            return CaliforniaStyleCheesePizza(self.ingredient)
        elif pizza_type == 'pepperoni':
            return CaliforniaStylePepperoniPizza(self.ingredient)
        elif pizza_type == 'clam':
            return CaliforniaStyleClamPizza(self.ingredient)
        elif pizza_type == 'veggie':
            return CaliforniaStyleVeggiePizza(self.ingredient)
        else:
            return Pizza(self.ingredient)

    def _ingredient(self):
        self.ingredient = CaliforniaPizzaIngredientFactory()


if __name__ == '__main__':
    cps = ChicagoPizzaStore()
    cps.order_pizza('cheese')
    cps.order_pizza('pepperoni')

    nyps = NYPizzaStore()
    nyps.order_pizza('cheese')
    nyps.order_pizza('pepperoni')

    caps = CaliforniaPizzaStore()
    caps.order_pizza('cheese')
    caps.order_pizza('pepperoni')
