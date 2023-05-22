class Hat:
    def __init__(self, name, colour, material, price):
        self.__name = name
        self.__colour = colour
        self.__material = material
        self.__price = float(price)

    def get_name(self):
        return self.__name

    def get_colour(self):
        return self.__colour

    def get_material(self):
        return self.__material

    def get_price(self):
        return self.__price
    
    def get_price_with_gst(self):
        return self.__price * 1.08

    def set_name(self, name):
        self.__name = name

    def set_colour(self, colour):
        self.__colour = colour

    def set_material(self, material):
        self.__material = material

    def set_price(self, price):
        self.__price = float(price)
