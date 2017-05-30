#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from .pizza import *


class AbsPizzaStore(object):

    def order_pizza(self, pizza_type):
        raise NotImplementedError

    def _create(self):
        raise NotImplementedError


class PizzaStore(AbsPizzaStore):

    def order_pizza(self, pizza_type):
        pizza = self._create(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

    def _create(self, pizza_type):
        raise NotImplementedError


class SimplePizzaStore(PizzaStore):

    def _create(self, pizza_type):
        if pizza_type == 'cheese':
            return CheesePizza()
        elif pizza_type == 'pepperoni':
            return PepperoniPizza()
        elif pizza_type == 'clam':
            return ClamPizza()
        elif pizza_type == 'veggie':
            return VeggiePizza()
        else:
            return None


if __name__ == '__main__':
    sps = SimplePizzaStore()
    sps.order_pizza('cheese')
    sps.order_pizza('pepperoni')
