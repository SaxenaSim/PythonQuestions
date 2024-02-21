#example of Abstraction

from abc import ABC

class Shape(ABC):         #abstract class
    def area_calc(self):  #abstract method
        pass
class Rect(Shape):
    l=float(input('Enter length :'))
    b=float(input('Enter breadth :'))
    def area_calc(self):
        return(self.l*self.b)
obr = Rect()

print("Area of Rectangle is ",obr.area_calc()) 
