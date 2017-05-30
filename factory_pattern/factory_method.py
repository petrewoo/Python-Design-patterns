#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from .pizza import *
from .pizzz_store import *


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
        else:
            return None


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
        else:
            return None


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
        else:
            return None


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
