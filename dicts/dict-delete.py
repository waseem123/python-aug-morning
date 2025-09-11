student = {'name': 'Steve', 'city': 'Solapur', 'rollno': 202, 'mobileno': 123456, 'marks': 85, 'division': 'A'}
print(student)

student.pop('city')
print(student)

student.popitem()
print(student)

del student['marks']
print(student)


student.clear()
print(student)

del student
print(student)