import math

class Shape(object):
    def __init__(self, name, colour, area_func,):
        self.name = name
        self.colour = colour
        self._area_func = area_func
        
    def calc_area(self, *args):
        return self._area_func(*args)

def traingle_area(base, height):
    return 0.5 * base * height

triangle_obj = Shape("Triangle", "Yellow", traingle_area)
print(triangle_obj.calc_area(2, 1))

def circle_area(radius):
    return math.pi * (radius ** 2)
        
circle_obj = Shape("Circle", "Red", circle_area)
print(circle_obj.calc_area(1))

