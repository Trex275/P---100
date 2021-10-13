class ATM(object):
    def __init__(self, cardno, pin, withdrawal, balance):
        self.cardno = cardno
        self.pin = pin
        self.withdrawal = withdrawal
        self.balance = balance
    def read (self, cardno):
        print( "details for " + cardno + " are being shown now")
Card = ATM ((651651641), (1598), (" - "), (380) )
print(Card.cardno)
