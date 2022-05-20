from Lab1.entity.bank import Bank
from Lab1.entity.credit_card import CreditCard
from Lab1.entity.human import Human
from Lab1.entity.phone import Phone


class Model:

    def __init__(self):
        self.bank = Bank({1: CreditCard(123, 1111)}, {'1111': Phone()}, 'bank.pickle')
        self.human = Human({1: CreditCard(123, 1111)}, {'1111': Phone()}, 100000, 'human.pickle')
