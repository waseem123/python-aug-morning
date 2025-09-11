a = {'C','CPP','Java','Python','Ruby','JS','PHP','C#','R'}
print(a)
b = {'C','CPP','Java','Python','Ruby'}
print(b)
c = {'JS','PHP','C#','R','Python','Ruby'}
print(c)
d = {'JS','PHP','C#','Basic','Kotlin','Swift'}
print(c)

print(b.issubset(a))
print(a.issuperset(c))
print(a.issuperset(d))
print(d.issubset(a))
print(b.isdisjoint(c))
print(b.isdisjoint(d))