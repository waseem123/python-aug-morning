mytuple = ('India', 'China', 'Russia', 'America', 'UK', 'France', 'Germeny',)
print(mytuple)

# mytuple.insert(0,'Japan')
# print(mytuple)

# Its just a work-around
countrylist = list(mytuple)
print(countrylist)
countrylist.append('Ukrain')
mytuple = tuple(countrylist)
print(mytuple)

mytuple[2] = 'Indonesia'
print(mytuple)