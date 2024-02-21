#Write a python program to create a class Circle. Include methods to calculate it's area and perimeter.


import math
class Circle:
    def __init__(self,radius):
        self.radius=radius
    
    def calculateArea(self):
        return math.pi * self.radius**2
        
    def calculatePerimeter(self):
        return math.pi*2*self.radius

radius=float(input("Enter radius"))
circle=Circle(radius)
print("Area is {0}",circle.calculateArea())
print("Perimeter is {0}",circle.calculatePerimeter())
