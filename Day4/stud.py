class Student:
    def __init__(self,name,rollno,marks):
        self.name=name#public
        self.__rollno=rollno#private
        self._marks=marks#protected
    def display(self):
        print("name",self.name,"roll.no",self.__rollno,"marks",self._marks)
    
s1=Student("sai",1,10)
s1.display()