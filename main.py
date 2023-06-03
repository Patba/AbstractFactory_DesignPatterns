from concretefactory import WoodenFurnitureFactory, PlasticFurnitureFactory, FurnitureMaker


def main():
    wooden_factory = WoodenFurnitureFactory()
    plastic_factory = PlasticFurnitureFactory()

    furniture_maker = FurnitureMaker(wooden_factory)
    furniture_maker.make_furniture()

    furniture_maker.factory = plastic_factory
    furniture_maker.make_furniture()

if __name__ == '__main__':
    main()