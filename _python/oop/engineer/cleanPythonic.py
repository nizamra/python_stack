class Engineer:
    def __init__(self):
        self._salary = None

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self,baseVal):
        self._salary = baseVal

    @salary.deleter
    def salary(self):
        del self._salary


Ghouli = Engineer()
Ghouli.salary = 1000
print(Ghouli.salary)
# del Ghouli.salary
# print(Ghouli.salary)