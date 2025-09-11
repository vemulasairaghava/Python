from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b     
    def area(self):
        print(f"Area is {self.l*self.b}")
class Circle(Shape):
    def __init__(self,r):
        self.r=r   
    def area(self):
        print(f"Area of circle is {3.14*self.r*self.r}")
c1=Circle(2)
c1.area()
r1=Rectangle(2,2)
r1.area()
        
