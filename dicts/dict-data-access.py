student = {'name': 'Steve', 'city': 'Solapur', 'rollno': 202, 'mobileno': 123456, 'marks': 85, 'division': 'A'}
print(student)

for i in student:
    print(i, student[i])
print('_________________')

print(student.keys())
print(student.values())
print(student.items())
print('_________________')

for i in student.keys():
    print(i)
print('_________________')

for i in student.values():
    print(i)
print('_________________')

for (i,j) in student.items():
    print(i,'-',j)