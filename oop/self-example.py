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

e1.setEmployee('Maviya',25000,'Data Analyst')
e2.setEmployee('Aman',23000,'Developer')
e3.setEmployee('Alex',60000,'Manager')

e1.getEmployee()
e2.getEmployee()
e3.getEmployee()



e4 = Employee()
name = input('Enter your name: ')
salary = input('Enter your salary: ')
designation = input('Enter your designation: ')
e4.setEmployee(name,salary,designation)
e4.getEmployee()