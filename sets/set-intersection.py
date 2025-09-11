a = {'C','CPP','Java','Python','Ruby'}
print(a)
b = {'JS','PHP','C#','R','Python','Ruby'}
print(b)

c = a.intersection(b)
print(c)

b.intersection_update(a)
print(a)
print(b)