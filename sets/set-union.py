a = {'C','CPP','Java','Python','Ruby'}
print(a)
b = {'JS','PHP','C#','R','Python','Ruby'}
print(b)

c = a.union(b)
print(c)

b.update(a)
print(a)
print(b)