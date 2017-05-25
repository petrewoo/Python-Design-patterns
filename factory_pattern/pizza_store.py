#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from .pizza import *


class AbsPizzaStore(object):

    def order_pizza(self, pizza_type):
        pizza = self._create(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

    def _create(self, pizza_type):
        raise NotImplementedError


class SimplePizzaStore(AbsPizzaStore):

    def _create(self, pizza_type):
        if pizza_type == 'cheese':
            return CheesePizza()
        elif pizza_type == 'pepperoni':
            return PepperoniPizza()
        elif pizza_type == 'clam':
            return ClamPizza()
        elif pizza_type == 'veggie':
            return VeggiePizza()


class ChicagoPizzaStore(AbsPizzaStore):

    def _create(self, pizza_type):
        if pizza_type == 'cheese':
            return ChicagoStyleCheesePizza()
        elif pizza_type == 'pepperoni':
            return ChicagoStylePepperoniPizza()
        elif pizza_type == 'clam':
            return ChicagoStyleClamPizza()
        elif pizza_type == 'veggie':
            return ChicagoStyleVeggiePizza()


class NYPizzaStore(AbsPizzaStore):

    def _create(self, pizza_type):
        if pizza_type == 'cheese':
            return NYStyleCheesePizza()
        elif pizza_type == 'pepperoni':
            return NYStylePepperoniPizza()
        elif pizza_type == 'clam':
            return NYStyleClamPizza()
        elif pizza_type == 'veggie':
            return NYStyleVeggiePizza()


class CaliforniaPizzaStore(AbsPizzaStore):

    def _create(self, pizza_type):
        if pizza_type == 'cheese':
            return CaliforniaStyleCheesePizza()
        elif pizza_type == 'pepperoni':
            return CaliforniaStylePepperoniPizza()
        elif pizza_type == 'clam':
            return CaliforniaStyleClamPizza()
        elif pizza_type == 'veggie':
            return CaliforniaStyleVeggiePizza()


if __name__ == '__main__':
    sps = SimplePizzaStore()
    sps.order_pizza('cheese')
    sps.order_pizza('pepperoni')

    cps = ChicagoPizzaStore()
    cps.order_pizza('cheese')
    cps.order_pizza('pepperoni')

    nyps = NYPizzaStore()
    nyps.order_pizza('cheese')
    nyps.order_pizza('pepperoni')

    caps = CaliforniaPizzaStore()
    caps.order_pizza('cheese')
    caps.order_pizza('pepperoni')
