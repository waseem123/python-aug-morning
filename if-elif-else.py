# if CONDITION :
#     statement 1
#     ...
#     statement N
# elif CONDITION :
#     statement 1
#     ...
#     statement N
# else:
#     statement 1
#     ...
#     statement N

n1,n2,n3 = 390,390,390

if n1>n2 and n1>n3:print(f'{n1} IS GREATER THAN {n2} AND {n3}')
elif n2>n1 and n2>n3:print(f'{n2} IS GREATER THAN {n1} AND {n3}')
elif n3>n1 and n3>n2:print(f'{n3} IS GREATER THAN {n1} AND {n2}')
else:print(f'ALL NUMBERS ARE EQUAL')