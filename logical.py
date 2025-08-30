# 1. and
# 2. or
# 3. not

a = 40
b = 50
c = 10

print(a>b and b<c)
print(b>a and b>c)
print(b<a and b>c)
print("_____________________")

a,b,c = 40,50,10
print(a<b or b>c)
print(a>b or a>c)
print(a<b or a<c)
print(b<a or b<c)
print("__________________")

print(not(a<b))
print(not(not(a<b)))