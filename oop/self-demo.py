class Bottle:
    brand = ''
    quantity = 0

    def setBottle(self, b, q):
        self.brand = b
        self.quantity = q

    def getBottle(self):
        print('BOTTLE BRAND - ', self.brand)
        print('BOTTLE QUANTITY - ', self.quantity,'Ltr.')

b1 = Bottle()
b2 = Bottle()

b1.setBottle('Bislery',5)
b2.setBottle('Sunrich',1)

b1.getBottle()
b2.getBottle()