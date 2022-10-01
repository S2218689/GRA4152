# made a superclass called person that has a Name and a Birthyear
class Person:
    def __init__(self, Name, Birthyear):
        self._Name = Name
        self._Birthyear = Birthyear
    def getYear(self):
        return self._Birthyear

    def getName(self):
        return self._Name
 # used a __repr__ method to print the class instance
    def __repr__(self) -> str:
        return f"Person {self._Name} {self._Birthyear} " 

class Student(Person):
    def __init__(self, Name, Birthyear, Major) -> str:
        super().__init__(Name, Birthyear)
        self._Major = Major

    def getMajor(self):
        return self._Major
        
 # overrides/ exstends the __repr__ method from person class and salary

    def __repr__(self):
        return f"Student {self._Name} {self._Birthyear} {self._Major}"

class Instructor(Person):
    def __init__(self, Name, Birthyear, Sallary) -> str:
        super().__init__(Name, Birthyear)
        self._salary = Sallary

    def getSallary(self):
        return self._salary
# overrides/ exstends the __repr__ method from person class and salary
    def __repr__(self):
        return f"Instructor {self._Name} {self._Birthyear} {self._salary}"



stud = Student
stud = Student("Saka", 2001, "Baller")
print(stud.getName())
print(stud.__repr__())

inst = Instructor
inst = Instructor("Messi", 1988, "Milions")
print(inst.__repr__())




