mytuple = ('India', 'China', 'Russia', 'America', 'UK', 'France', 'Germeny',)
print(mytuple)

print(mytuple[0])
print(mytuple[2])
print(mytuple[-2])
print(mytuple[-4])

print(mytuple[0:5])
print(mytuple[2:6])
print(mytuple[-5:-1])
print(mytuple[0:6:2])
print("------------------------")
for i in mytuple:
    print(i)
print("------------------------")
for i in range(len(mytuple)):
    print(mytuple[i])