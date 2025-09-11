class Employee:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
    def display(self):
        print(f"name {self.name} with salary {self.sal}")
class Manager(Employee):
    def __init__(self, name, sal,dep):
        super().__init__(name, sal)
        self.dep=dep
    def display(self):
        print(f"name {self.name} with salary {self.sal} in the department of {self.dep}")
E1=Employee("sai",1)
m1=Manager("Raghava",1,"se")
E1.display()  
m1.display()  

        
    