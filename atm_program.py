import random
import datetime
from customer import Customer

id = int(input('Please insert your pin: '))

atm = Customer(id, 1234, 10000)

trial = 0

while (id !=(atm.checkPin()) and trial < 3):
    id = int(input('Your pin is incorrect. Please try again: '))
    trial += 1
    if trial == 3:
        print('Error. Please take your card and try again.')
        exit()

while (id ==(atm.checkPin())):
    print('Welcome to Bank of the River!')
    print('----------')
    options = ['Check Balance', 'Withdraw Money', 'Deposit Money', 'Change Pin', 'Exit']
    index = 1
    for option in options:
        print(str(index) + '. ' + option)
        index += 1
    print('----------')
    action = input('What can we help you with? ')
    if action == '1':
        print(atm.checkBalance())
        print('----------')
    if action == '2':
        nominalWithdraw = int(input('How much money would you like to withdraw? '))
        if nominalWithdraw <= atm.custBalance:
            print('Withdraw is successful. Your current balance is $' + str(atm.withdrawBalance(nominalWithdraw)))
            print('----------')
        else:
            print('You do not have enough money to withdraw')
            print('----------')
    if action == '3':
        nominalDeposit = int(input('How much money would you like to deposit? '))
        print('Deposit is successful. Your balance is now $' + str(atm.depositBalance(nominalDeposit)))
        print('----------')
    if action == '4':
        id = int(input('Please insert a new pin: '))
        while (id ==(atm.checkPin()) and trial < 3):
            id = int(input('You have used this pin before. Please try again:'))
            trial += 1
            if trial == 3:
                print('Pin change is unsuccessful. Please take your card and try again.')
                exit()
        while (id !=(atm.checkPin())):
            atm.changePin(id)
            print('You have successfully changed your pin.')
            print('----------')
    if action == '5':
        print('----------')
        print('Thank you for using Bank of the River!')
        print('Record Number: ' + str(random.randint(1000000000, 9999999999)))
        now = datetime.datetime.now()
        print('Date and Time: ' + now.strftime("%c"))
        print('Current Balance: $' + str(atm.callBalance()))
        exit()
    if int(action) > 5 or int(action) < 1:
        print('Error. Please try again:')
