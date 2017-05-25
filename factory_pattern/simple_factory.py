#!/usr/bin/env python
# -*- encoding: utf-8 -*-


class Pizza(object):

    def prepare(self):
        print("Prepare {}".format(self.__class__.__name__))

    def bake(self):
        print("Bake {}".format(self.__class__.__name__))

    def cut(self):
        print("Cut {}".format(self.__class__.__name__))

    def box(self):
        print("Box {}".format(self.__class__.__name__))


class ChicagoPizza(Pizza):
    pass


class NewYorkPizza(Pizza):
    pass


class SimplePizzaFactory(object):

    @staticmethod
    def create(pizza_name):
        if pizza_name.lower() == 'chicago':
            return ChicagoPizza()
        elif pizza_name.lower() == 'newyork':
            return NewYorkPizza()


class PizzaStore(object):

    def __init__(self, pizza_factory):
        self._pizza_factory = pizza_factory

    def order_pizza(self, pizza_name):
        pizza = self._pizza_factory.create(pizza_name)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()


if __name__ == '__main__':
    pizza_store = PizzaStore(SimplePizzaFactory)
    pizza_store.order_pizza('newyork')
    pizza_store.order_pizza('chicago')
