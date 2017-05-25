#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from .pizza import *


class SimplePizzaFactory(object):

    @staticmethod
    def create(pizza_type):
        if pizza_type == 'cheese':
            return CheesePizza()
        elif pizza_type == 'pepperoni':
            return PopperoniPizza()
        elif pizza_type == 'clam':
            return ClamPizza()
        elif pizza_type == 'veggie':
            return VeggiePizza()


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
