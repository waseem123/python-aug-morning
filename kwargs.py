def printdata(**data):
    print(data)
    print(f'My name is {data['name']}')
    print(f'I live in {data['city']}, {data['state']}')
    
printdata(name='Waseem',city='Solapur',state='Maharashtra')