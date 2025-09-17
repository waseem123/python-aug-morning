class Employee:
    def __init__(self, name, perdaysalary, workingdays):
        self.name = name
        self.perdaysalary = perdaysalary
        self.workingdays = workingdays

    def calculatesalary(self):
        self.salary = self.perdaysalary * self.workingdays

    def getEmployee(self):
        print(f'Name - {self.name}')
        print(f'Perdaysalary - {self.perdaysalary}')
        print(f'Workingdays - {self.workingdays}')
        print(f'Total Salary - {self.salary}')
        print("_____________________________")

emp1 = Employee('John', 250, 10)
emp2 = Employee('Shawn', 2500, 20)
emp3 = Employee('Sam', 500, 20)

emp1.calculatesalary()
emp2.calculatesalary()
emp3.calculatesalary()

emp1.getEmployee()
emp2.getEmployee()
emp3.getEmployee()