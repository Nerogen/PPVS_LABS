from os import system

from Lab1.entity.bank import Bank
from Lab1.entity.credit_card import CreditCard
from Lab1.entity.human import Human
from Lab1.entity.phone import Phone
from Lab1.logic.action import Action
from Lab4.Conctroller.controller import Controller


def test_main() -> None:
    credit1 = CreditCard(123, 1111)
    credit2 = CreditCard(321, 2222)
    phone = Phone()
    account = {
        1: credit1,
        2: credit2
    }
    phones = {
        '111111': phone
    }
    bank = Bank(account, phones, 'bank.pickle')
    human = Human(account, phones, 100000, 'human.pickle')
    Action.put_money_on_the_card(bank, human, 1, 3000, 123, 1111)
    print(Action.get_account_info(bank, 1, 123, 1111))
    Action.take_money_from_the_card(bank, human, 1, 1000, 123, 1111)
    print(Action.get_account_info(bank, 1, 123, 1111))
    Action.put_money_on_phone(bank, human, '111111', 1, 1000, 123, 1111)
    print(Action.get_account_info(bank, 1, 123, 1111))
    Action.registration_new_credit_card(bank, human, (3, CreditCard(456, 1234)))
    Action.put_money_on_the_card(bank, human, 3, 1000, 456, 1234)
    print(Action.get_account_info(bank, 3, 456, 1234))


def cli():
    bank = None
    human = None
    trigger = True
    while trigger:
        print('Input command:')
        print('1: Create bank entity')
        print('2: Create human entity')
        print('3: Actions')
        print('4: Read from file')
        print('0: Complete')
        num = int(input(': '))
        match num:
            case 0:
                trigger = False
                print('Program complete!')
            case 1:
                read_write_file = input('Input file for thread: ')
                bank = Bank({}, {}, read_write_file + '.pickle')
            case 2:
                read_write_file = input('Input file for thread: ')
                money = int(input('Input number of money: '))
                human = Human({}, {}, money, read_write_file + '.pickle')
            case 3:
                flag = True
                if bank is None and human is None:
                    print("Entity doesn't exist")
                    flag = False
                while flag:
                    print('Input action:')
                    print('1: Put money on the card')
                    print('2: Take money from the card')
                    print('3: Get account info')
                    print('4: Registration new credit card')
                    print('5: Registration new phone')
                    print('6: Put money on phone')
                    print('0: exit')
                    action = int(input(': '))
                    match action:
                        case 0:
                            flag = False
                        case 1:
                            account = int(input('Input number of bank account: '))
                            number_of_money = int(input('Input number of money which you need put: '))
                            card_number = int(input('Input card number: '))
                            pin_code = int(input('Input pin code: '))
                            Action.put_money_on_the_card(bank, human, account, number_of_money, card_number, pin_code)
                        case 2:
                            account = int(input('Input number of bank account: '))
                            value = int(input('Input number of money which you need put: '))
                            card_number = int(input('Input card number: '))
                            pin_code = int(input('Input pin code: '))
                            Action.take_money_from_the_card(bank, human, account, value, card_number, pin_code)
                        case 3:
                            account = int(input('Input number of bank account: '))
                            card_number = int(input('Input card number: '))
                            pin_code = int(input('Input pin code: '))
                            print(Action.get_account_info(bank, account, card_number, pin_code))
                        case 4:
                            credit_card_number = int(input('Input number of bank credit card: '))
                            pin_code = int(input('Input pin code: '))
                            credit_card = CreditCard(credit_card_number, pin_code)
                            Action.registration_new_credit_card(bank, human, (len(human.bank_accounts), credit_card))
                        case 5:
                            phone_number = input('Input phone number: ')
                            phone = Phone()
                            Action.registration_new_phone(bank, human, (phone_number, phone))
                        case 6:
                            account = int(input('Input number of bank account: '))
                            value = int(input('Input number of money which you need put: '))
                            phone_number = input('Input phone number: ')
                            card_number = int(input('Input card number: '))
                            pin_code = int(input('Input pin code: '))
                            Action.put_money_on_phone(bank, human, phone_number, account, value, card_number, pin_code)
                        case _:
                            print("Action doesn't exist!")
                    system('cls')
            case 4:
                if bank is None and human is None:
                    print("Entity doesn't exist")
                else:
                    bank.read_info = input('Input file for thread bank: ') + '.pickle'
                    human.read_file = input('Input file for thread human: ') + '.pickle'
            case _:
                print('Not has any actions!')
        system('cls')


def choice():
    flag = input("Input 1 if want ui:")
    if flag == '1':
        Controller().run()
    else:
        cli()


if __name__ == '__main__':
    choice()
