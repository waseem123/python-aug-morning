class Employee:
    def setEmployee(self,x,empSalary,empDesignation):
        self.empName = x
        self.empSalary = empSalary
        self.empDesignation = empDesignation

    def getEmployee(self):
        print('EMPLOYEE NAME - ', self.empName)
        print('EMPLOYEE SALARY - ', self.empSalary)
        print('EMPLOYEE DESIGNATION - ', self.empDesignation)
        print("____________________________________________")

e1 = Employee()
e2 = Employee()
e3 = Employee()
allemployees = [e1, e2, e3]

for e in allemployees:
    name = input('Enter your name: ')
    salary = input('Enter your salary: ')
    designation = input('Enter your designation: ')
    e.setEmployee(name,salary,designation)

for e in allemployees:
    e.getEmployee()