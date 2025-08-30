base_fare = 30
print('Daund','Pune','Thane','CST')
destination = input('ENTER YOUR DESTINATION - ')

if destination=='Daund':
    print(f'Your Cost of Ticket for {destination} is - RS. {base_fare}')
elif destination=='Pune':
    print(f'Your Cost of Ticket for {destination} is - RS. {base_fare*2}')
elif destination=='Thane':
    print(f'Your Cost of Ticket for {destination} is - RS. {base_fare*3}')
elif destination=='CST':
    print(f'Your Cost of Ticket for {destination} is - RS. {base_fare*4}')
else:
    print('INVALID DESTINATION VALUE')