class SoftwareEngineer:
    
    alias = "Keyboard Magician"

    def __init__ (self, name, age, level, salary):
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary
    
    @classmethod
    def juniorEng(self, name,age):
        ff = SoftwareEngineer(name, age, 'junior', 1000)
        return ff

    def __str__(self) -> str:
        return (f"name is: {self.name},\nage is: {self.age},\nlevel is: {self.level},\nsalary is: {self.salary}")
    def coding(self):
        print(f"{self.name} be cauwid..")
    def codingLang(self,lang):
        print(f"{self.name} be cauwid.. {lang}")
    def __eq__(self,other):
        return self.name == other.name and self.age == other.age
    
    @staticmethod
    def calcSallary(age):
        if age < 25:
            return 1200
        elif age < 35:
            return 3500
        else:
            return 9600


Joury = SoftwareEngineer("ahmad",25,"junior", 4300)
Jou = SoftwareEngineer("ahmad",25,"Senior", 9600)
Ayyash = SoftwareEngineer.juniorEng("khalil", 24)
print(Ayyash)

# print(Joury)
# print("age",Joury.age)
# print("Name ",Joury.name)
# print(SoftwareEngineer.alias)
# print(Joury.alias)
# print(f"lala falala {Joury}")
# Joury.coding()
# Joury.codingLang(48)
# Joury.codingLang("python")
# print(Joury==Jou)
# print(SoftwareEngineer.calcSallary(18))
# print(SoftwareEngineer.calcSallary(27))
# print(SoftwareEngineer.calcSallary(40))