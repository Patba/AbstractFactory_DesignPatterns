from abstractprod import *


class WoodenChair(Chair):
    def sit_on(self):
        print("You are sitting on a wooden chair.")

class PlasticChair(Chair):
    def sit_on(self):
        print("You are sitting on a plastic chair.")

class WoodenSofa(Sofa):
    def sit_on(self):
        print("You are sitting on a wooden sofa.")

class PlasticSofa(Sofa):
    def sit_on(self):
        print("You are sitting on a plastic sofa.")

class WoodenCoffeeTable(CoffeeTable):
    def place_items(self):
        print("You placed items on a wooden coffee table.")

class PlasticCoffeeTable(CoffeeTable):
    def place_items(self):
        print("You placed items on a plastic coffee table.")

