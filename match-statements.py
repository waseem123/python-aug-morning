print('1. ADDITION')
print('2. SUBTRACTION')
print('3. MULTIPLICATION')
choice = int(input('ENTER YOUR CHOICE  - '))

match(choice):
    case 1:
        a = int(input('ENTER FIRST NUMBER  - '))
        b = int(input('ENTER SECOND NUMBER - '))
        print(f'ADDITION OF {a} AND {b} IS {a+b}')
    case 2:
        a = int(input('ENTER FIRST NUMBER  - '))
        b = int(input('ENTER SECOND NUMBER - '))
        print(f'SUBTRACTION OF {a} AND {b} IS {a-b}')
    case 3:
        a = int(input('ENTER FIRST NUMBER  - '))
        b = int(input('ENTER SECOND NUMBER - '))
        print(f'MULTIPLICATION OF {a} AND {b} IS {a*b}')
    case _:
        print('WRONG INPUT! PLEASE SELECT THE OPTION BETWEEN 1 TO 3')