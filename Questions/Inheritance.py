#Define a employee class with attributes role, department and salary.This class also has a showDetails() method. Create an engineer class that inherit properties and has additional attributes name and age.


class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary
        
    def showDetails(self):
        print("role is",self.role)
        print("department is",self.dept)
        print("salary is",self.salary)
        
class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT","75000")
        
engg = Engineer("karan",40)
engg.showDetails()
