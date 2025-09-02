def fact(n):
    f = 1
    for i in range(1,n+1):
        f *=  i # 120*5=120
    return f

print(fact(5))
print(fact(6))
print(fact(10))