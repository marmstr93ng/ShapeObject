import math

class Shape(object):
    def __init__(self, shape_calc_obj, **dimensions):
        self.name = shape_calc_obj.__name__
        self._shape_calc_obj = shape_calc_obj
        self.__dict__.update(dimensions)
        self._update_calcs(**dimensions)
    
    def set_dimension(self, **dimensions):
        self.__dict__.update(dimensions)
        self._update_calcs(**dimensions)

    def _update_calcs(self, **dimensions):
        self.area = self._shape_calc_obj(**dimensions).calc_area()
        self.circumference = self._shape_calc_obj(**dimensions).calc_circumference()
    
class Triangle(object):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def calc_area(self):
        return 0.5 * self.base * self.height
    
    def calc_circumference(self):
        return self.base + self.height + math.sqrt((self.base ** 2) + (self.height ** 2))

class Circle(object):
    def __init__(self, radius):
        self.radius = radius
    
    def calc_area(self):
        return math.pi * (self.radius ** 2)
    
    def calc_circumference(self):
        return 2 * math.pi * self.radius

class Square(object):
    def __init__(self, height):
        self.height = height
    
    def calc_area(self):
        return float(self.height ** 2)
    
    def calc_circumference(self):
        return 4 * self.height

triangle_obj = Shape(Triangle, base=2, height=1)
print("{} Area: {}".format(triangle_obj.name, triangle_obj.area))
print("{} Circumference: {}".format(triangle_obj.name, triangle_obj.circumference))
triangle_obj.set_dimension(base=1, height=3)
print("{} Area: {}".format(triangle_obj.name, triangle_obj.area))
print("{} Circumference: {}".format(triangle_obj.name, triangle_obj.circumference))

circle_obj = Shape(Circle, radius=1)
print("{} Area: {}".format(circle_obj.name, circle_obj.area))
print("{} Circumference: {}".format(circle_obj.name, circle_obj.circumference))

square_obj = Shape(Square, height=1)
print("{} Area: {}".format(square_obj.name, square_obj.area))
print("{} Circumference: {}".format(square_obj.name, square_obj.circumference))
