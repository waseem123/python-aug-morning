a = {'C','CPP','Java','Python','Ruby'}
print(a)
b = {'JS','PHP','C#','R','Python','Ruby'}
print(b)

c = a.symmetric_difference(b)
print(c)

b.symmetric_difference_update(a)
print(a)