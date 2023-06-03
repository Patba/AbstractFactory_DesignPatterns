from concreteprod import *


class FurnitureFactory:
    def create_chair(self):
        pass

    def create_sofa(self):
        pass

    def create_coffee_table(self):
        pass


class WoodenFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return WoodenChair()

    def create_sofa(self):
        return WoodenSofa()

    def create_coffee_table(self):
        return WoodenCoffeeTable()

class PlasticFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return PlasticChair()

    def create_sofa(self):
        return PlasticSofa()

    def create_coffee_table(self):
        return PlasticCoffeeTable()



#Maker
class FurnitureMaker:
    def __init__(self, factory):
        self.factory = factory

    def make_furniture(self):
        chair = self.factory.create_chair()
        chair.sit_on()

        sofa = self.factory.create_sofa()
        sofa.sit_on()

        coffee_table = self.factory.create_coffee_table()
        coffee_table.place_items()
