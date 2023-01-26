class Person():
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

class Student(Person):
    pass

#Now the Student class has the same properties and methods as the Person class.
#Use the Student class to create an object, and then execute the printname method:
x = Student("Mike", "Olsen")
x.printname()
