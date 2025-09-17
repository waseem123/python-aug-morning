class MobilePhone:
    def __init__(self, brand='', ram=0, price=0):
        self.brand = brand
        self.ram = ram
        self.price = price

    def getMobilePhone(self):
        print(f'BRAND - {self.brand}')
        print(f'RAM - {self.ram} GB')
        print(f'PRICE - INR. {self.price}')
        print("___________________________")

n = int(input('ENTER THE NUMBER OF MOBILES - '))
mobiles = []

for i in range(n):
    b = input('ENTER THE BRAND OF THE MOBILE - ')
    r = int(input('ENTER THE RAM OF THE MOBILE   - '))
    p = int(input('ENTER THE PRICE OF THE MOBILE - '))
    m = MobilePhone(b, r, p)
    mobiles.append(m)

for i in mobiles:
    i.getMobilePhone()