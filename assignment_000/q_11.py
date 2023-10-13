# Create a person class. The person class must contain the name and age properties. 
# Create a student class that inherits the person class. 
# The student class must have the properties, midterm, final and project. 
# The student class must have a method that calculates the student's average.
# Create a list of students, put values for name, age and the 3 grades. 
# After that is done, loop and calculate the overall average of the students on this list.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student (Person):
    def __init__(self, name, age, midterm, final, project):
        Person.__init__(self, name, age)
        self.midterm = midterm
        self.final = final
        self.project = project
    
    def avg(self):
        return (self.midterm + self.final + self.project) / 3
    

students = [ Student('Bruno',18,6,6,6), Student('Marcos',18,7,7,7)]
for s in students :
    print(s.name)
    print(s.avg())