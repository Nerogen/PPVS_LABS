import unittest
from Lab1.entity.bank import Bank
from Lab1.entity.credit_card import CreditCard
from Lab1.entity.human import Human
from Lab1.entity.phone import Phone
from Lab1.logic.action import Action


class TestProgram(unittest.TestCase):
    def test_area(self):
        credit1 = CreditCard(123, 1111)
        account = {
            1: credit1,
        }
        bank = Bank(account, {}, 'bank.pickle')
        human = Human(account, {}, 10000, 'human.pickle')
        Action.put_money_on_the_card(bank, human, 1, 5000, 123, 1111)
        self.assertEqual(Action.get_account_info(bank, 1, 123, 1111), '5000$')

    def test_area1(self):
        credit1 = CreditCard(123, 1111)
        account = {
            1: credit1,
        }
        phone = Phone()
        phones = {
            '111111': phone
        }
        bank = Bank(account, phones, 'bank.pickle')
        human = Human(account, phones, 10000, 'human.pickle')
        Action.put_money_on_the_card(bank, human, 1, 5000, 123, 1111)
        self.assertEqual(Action.get_account_info(bank, 1, 123, 1111), '5000$')
        Action.put_money_on_phone(bank, human, '111111', 1, 5000, 123, 1111)
        self.assertEqual(Action.get_account_info(bank, 1, 123, 1111), '0$')

    def test_user_info(self):
        bank = Bank({}, {}, 'bank.pickle')
        human = Human({}, {}, 10000, 'human.pickle')
        Action.registration_new_credit_card(bank, human, (1, CreditCard(123, 1111)))
        Action.put_money_on_the_card(bank, human, 1, 5000, 123, 1111)
        self.assertEqual(Action.get_account_info(bank, 1, 123, 1111), '5000$')

    def test_user_info1(self):
        bank = Bank({}, {}, 'bank.pickle')
        human = Human({}, {}, 8000, 'human.pickle')
        Action.registration_new_credit_card(bank, human, (1, CreditCard(123, 1111)))
        Action.put_money_on_the_card(bank, human, 1, 8000, 123, 1111)
        self.assertEqual(Action.get_account_info(bank, 1, 123, 1111), '8000$')
        Action.registration_new_phone(bank, human, ('123', Phone()))
        Action.put_money_on_phone(bank, human, '123', 1, 8000, 123, 1111)
        self.assertEqual(Action.get_account_info(bank, 1, 123, 1111), '0$')

    def test_exception(self):
        bank = Bank({}, {}, 'bank.pickle')
        human = Human({}, {}, 100000, 'human.pickle')
        Action.registration_new_credit_card(bank, human, (1, CreditCard(123, 1111)))
        Action.put_money_on_the_card(bank, human, 1, 10000000, 123, 1111)
        self.assertEqual(Action.get_account_info(bank, 1, 123, 1111), '0$')
        Action.registration_new_phone(bank, human, ('123', Phone()))
        Action.put_money_on_phone(bank, human, '123', 1, 1000000, 123, 1111)
        self.assertEqual(Action.get_account_info(bank, 1, 123, 1111), '0$')

    def test_exception1(self):
        bank = Bank({}, {}, 'bank.pickle')
        human = Human({}, {}, 5000, 'human.pickle')
        Action.registration_new_credit_card(bank, human, (1, CreditCard(123, 1111)))
        Action.registration_new_credit_card(bank, human, (1, CreditCard(111, 1111)))
        self.assertEqual(Action.get_account_info(bank, 1, 123, 1111), '0$')
        Action.registration_new_phone(bank, human, ('123', Phone()))
        Action.registration_new_phone(bank, human, ('122', Phone()))
        Action.put_money_on_phone(bank, human, '123', 1, 1000000, 123, 1111)
        Action.put_money_on_phone(bank, human, '122', 1, 1000000, 123, 1111)
        self.assertEqual(Action.get_account_info(bank, 1, 123, 1111), '0$')
