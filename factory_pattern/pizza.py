#!/usr/bin/env python
# -*- encoding: utf-8 -*-


class AbsPizza(object):

    def prepare(self):
        raise NotImplementedError

    def bake(self):
        raise NotImplementedError

    def cut(self):
        raise NotImplementedError

    def box(self):
        raise NotImplementedError


class Pizza(AbsPizza):

    def __init__(self):
        print('new a raw {}'.format(self.__class__.__name__))

    def prepare(self):
        print("Prepare {}".format(self.__class__.__name__))

    def bake(self):
        print("Bake {}".format(self.__class__.__name__))

    def cut(self):
        print("Cut {}".format(self.__class__.__name__))

    def box(self):
        print("Box {}".format(self.__class__.__name__))


class CheesePizza(Pizza):
    pass


class PepperoniPizza(Pizza):
    pass


class ClamPizza(Pizza):
    pass


class VeggiePizza(Pizza):
    pass


class NYStyleCheesePizza(Pizza):
    pass


class NYStylePepperoniPizza(Pizza):
    pass


class NYSytleClamPizza(Pizza):
    pass


class NYStyleVeggiePizza(Pizza):
    pass


class ChicagoStyleCheesePizza(Pizza):
    pass


class ChicagoStylePepperoniPizza(Pizza):
    pass


class ChicagoStyleClamPizza(Pizza):
    pass


class ChicagoStyleVeggiePizza(Pizza):
    pass


class CaliforniaStyleCheesePizza(Pizza):
    pass


class CaliforniaStylePepperoniPizza(Pizza):
    pass


class CaliforniaSytleClamPizza(Pizza):
    pass


class CaliforniaStyleVeggiePizza(Pizza):
    pass
