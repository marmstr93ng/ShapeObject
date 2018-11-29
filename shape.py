import math

class Shape(object):
    def __init__(self, name, colour, area_func, circumference_func):
        self.name = name
        self.colour = colour
        self._area_func = area_func
        self._circumference_func = circumference_func

    def calc_area(self, *args):
        return self._area_func(*args)
    
    def calc_circumference(self, *args):
        return self._circumference_func(*args)
    

def triangle_area(base, height):
    return 0.5 * base * height
    
def triangle_circumference(base, height):
    return base + height + math.sqrt((base ** 2) + (height ** 2))

triangle_obj = Shape("Triangle", "Yellow", triangle_area, triangle_circumference)
print("{} {} Area: {}".format(triangle_obj.colour, triangle_obj.name, triangle_obj.calc_area(2, 1)))
print("{} {} Circumference: {}".format(triangle_obj.colour, triangle_obj.name, triangle_obj.calc_circumference(2, 1)))

def circle_area(radius):
    return math.pi * (radius ** 2)

def circle_circumference(radius):
    return 2 * math.pi * radius
        
circle_obj = Shape("Circle", "Red", circle_area, circle_circumference)
print("{} {} Area: {}".format(circle_obj.colour, circle_obj.name, circle_obj.calc_area(1)))
print("{} {} Circumference: {}".format(circle_obj.colour, circle_obj.name, circle_obj.calc_circumference(1)))

def square_area(height):
    return float(height ** 2)
    
def square_circumference(height):
    return 4 * height
        
square_obj = Shape("Square", "Blue", square_area, square_circumference)
print("{} {} Area: {}".format(square_obj.colour, square_obj.name, square_obj.calc_area(2)))
print("{} {} Circumference: {}".format(square_obj.colour, square_obj.name, square_obj.calc_circumference(2)))
