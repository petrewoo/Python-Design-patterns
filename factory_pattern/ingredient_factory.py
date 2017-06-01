#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
Abstract Factory patterns.
~~~~~~~~~~~~~~~~~~~~~~~~

This is a Abstract Factory Sample.

AbsIngredientFactory define a big interface to create six ingredients.
Use factory method implement ingredient create method.
"""


class AbsIngredientFactory(object):

    def create_dough(self):
        raise NotImplementedError

    def create_sauce(self):
        raise NotImplementedError

    def create_cheese(self):
        raise NotImplementedError

    def create_veggie(self):
        raise NotImplementedError

    def create_peppernoi(self):
        raise NotImplementedError

    def create_clam(self):
        raise NotImplementedError


class IngredientFactory(AbsIngredientFactory):

    def create_dough(self):
        print('ceate dough of {}'.format(self.__class__.__name__))

    def create_sauce(self):
        print('ceate sauce of {}'.format(self.__class__.__name__))

    def create_cheese(self):
        print('ceate cheesse of {}'.format(self.__class__.__name__))

    def create_veggie(self):
        print('ceate veggies of {}'.format(self.__class__.__name__))

    def create_peppernoi(self):
        print('ceate peppernoi of {}'.format(self.__class__.__name__))

    def create_clam(self):
        print('ceate clam of {}'.format(self.__class__.__name__))


class NYPizzaIngredientFactory(IngredientFactory):
    pass


class ChicagoPizzaIngredientFactory(IngredientFactory):
    pass


class CaliforniaPizzaIngredientFactory(IngredientFactory):
    pass
