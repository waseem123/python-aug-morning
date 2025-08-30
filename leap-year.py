year = int(input('ENTER AN YEAR - '))

if (year%4==0 and year%100 !=0) or year%400==0:
    print(f'{year} IS A LEAP YEAR')
else:
    print(f'{year} IS NOT A LEAP YEAR')