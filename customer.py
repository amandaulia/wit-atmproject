from atm_card import ATMCard
class Customer:
    def __init__(self, id, custPin, custBalance):
        self.id = id
        self.custPin = 1234
        self.custBalance = 10000

    def checkId(self):
        return self.id

    def checkPin(self):
        return self.custPin

    def callBalance(self):
        return self.custBalance

    def checkBalance(self):
        return 'Your balance is $' + str(self.custBalance)

    def depositBalance(self, nominalDeposit):
        self.custBalance += nominalDeposit
        return self.custBalance

    def withdrawBalance(self, nominalWithdraw):
        self.custBalance -= nominalWithdraw
        return self.custBalance

    def changePin(self, id):
        self.custPin = id
        return self.custPin
