# Dictionaries are the mutable, unrepeated and ordered collection of data. The data is represented using key-value pairs.

student = {'name':'Steve',
           'city':'Paris',
           'rollno':202,
           'mobileno':[123456,246810]
           }
print(student)
print(type(student))
print(student['name'])
print(student.get('city'))
# print(student[202]) NOT POSSIBLE
print("--------------------------")

employee = dict((
                    ('empId',101),
                    ('empName','George'),
                    ('empSalary',45000),
                    ('empDesignation','Jr. Engineer')
                ))
print(employee)
print(type(employee))