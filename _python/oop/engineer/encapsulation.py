class Engineer:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        #if there is two leading underscore that indicates a private attribute
        #leading underscore indicates a protected attribute
        self._salary = None
        self._solvedBugs = 0

    def workHard(self,times):
        self._solvedBugs+=6*times
    def getSalary(self):
        return self._salary
    def setSalary(self,baseVal):
        self._salary = self._calculateSalary(baseVal)
    def _calculateSalary(self, numb):
        if self._solvedBugs<30:
            return numb
        elif self._solvedBugs<120:
            return numb*1.7
        return numb*2.5


Ghouli = Engineer("Abdulrahman",24)
# Ghouli.setSalary(1000)
# print(Ghouli.getSalary())
Ghouli.workHard(6)
Ghouli.setSalary(1000)
print(Ghouli.getSalary())
