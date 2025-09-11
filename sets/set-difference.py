a = {'C','CPP','Java','Python','Ruby'}
print(a)
b = {'JS','PHP','C#','R','Python','Ruby'}
print(b)

c = a.difference(b)
print(c)

d = b - a
print(d)

b.difference_update(a)
print(a)
print(b)