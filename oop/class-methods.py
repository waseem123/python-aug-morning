class Employee:
    empId = 0
    empName = ''

    def setEmployee(self):
        self.empId = int(input('Enter Employee ID: '))
        self.empName = input('Enter Employee Name: ')

    def getEmployee(self):
        print('EMPLOYEE ID - ', self.empId)
        print('EMPLOYEE NAME - ', self.empName)

emp1 = Employee()
emp2 = Employee()

print('ENTER THE DATA FOR FIRST EMPLOYEE')
emp1.setEmployee()
print('ENTER THE DATA FOR SECOND EMPLOYEE')
emp2.setEmployee()

print('DATA OUTPUT FOR EMPLOYEE 1')
emp1.getEmployee()

print('DATA OUTPUT FOR EMPLOYEE 2')
emp2.getEmployee()