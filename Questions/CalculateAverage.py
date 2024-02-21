#Write a program to create a class Student and include method to calculate the average of marks of a student

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for i in self.marks:
            sum+=i
        print("average is",sum/3)
        
s1 = Student("karan",[98,76,86])
s1.get_avg()
