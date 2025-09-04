mylist =['Chennai', 'Solapur', 'Vijaypura', 'Pune', 'Mumbai', 'Delhi', 'Bengaluru', 'Hyderabad', 'Nasik', 'Patna']
print(mylist)

for i in mylist:
    print(i)
    
for i in mylist:
    if i=='Mumbai':
        print(i)
print("_______________________")

for i in range(len(mylist)):
    print(i)
    print(mylist[i])
print("_______________________")

for i in range(len(mylist)):
    if i%2==0:
        print(i,mylist[i])