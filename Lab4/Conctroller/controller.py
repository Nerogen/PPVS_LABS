from Lab1.entity.credit_card import CreditCard
from Lab1.entity.phone import Phone
from Lab1.logic.action import Action
from Lab4.Model.model import Model
from Lab4.View.view import View


class Controller(View, Model):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return self.screen

    def put_money(self):
        Action.put_money_on_the_card(
            self.bank,
            self.human,
            int(self.screen.ids.account_number_of_put_money_on_the_card.text),
            int(self.screen.ids.amount_of_money_of_put_money_on_the_card.text),
            int(self.screen.ids.card_number_of_put_money_on_the_card.text),
            int(self.screen.ids.pin_code_of_put_money_on_the_card.text)
        )

        self.update_view_menu(self.bank.bank_info, self.human.cash)

    def take_money(self):
        Action.take_money_from_the_card(
            self.bank,
            self.human,
            int(self.screen.ids.account_number_of_take_money_from_the_card.text),
            int(self.screen.ids.amount_of_money_of_take_money_from_the_card.text),
            int(self.screen.ids.card_number_of_take_money_from_the_card.text),
            int(self.screen.ids.pin_code_of_take_money_from_the_card.text)
        )

        self.update_view_menu(self.bank.bank_info, self.human.cash)

    def get_info(self):
        self.user_info(
            Action.get_account_info(
                self.bank,
                int(self.screen.ids.account_number_of_get_account_info.text),
                int(self.screen.ids.card_number_of_get_account_info.text),
                int(self.screen.ids.pin_code_of_get_account_info.text)
            )
        )

    def put_on_phone(self):
        Action.put_money_on_phone(
            self.bank,
            self.human,
            self.screen.ids.phone_of_put_money_on_phone.text,
            int(self.screen.ids.account_of_put_money_on_phone.text),
            int(self.screen.ids.amount_of_money_of_put_money_on_phone.text),
            int(self.screen.ids.card_number_of_put_money_on_phone.text),
            int(self.screen.ids.pin_code_of_put_money_on_phone.text)
        )

        self.update_view_menu(self.bank.phones_info, self.human.cash, True)

    def registration_new_account(self):
        Action.registration_new_credit_card(
            self.bank,
            self.human,
            (
                int(self.screen.ids.account_of_registration_new_credit_card.text),
                CreditCard(
                    int(self.screen.ids.credit_card_number_of_registration_new_credit_card.text),
                    int(self.screen.ids.pin_code_of_registration_new_credit_card.text))
            )
        )
        self.user_info("Added new credit card!")

    def registration_new_phone(self):
        Action.registration_new_phone(
            self.bank,
            self.human,
            (self.screen.ids.phone_number_of_registration_new_phone.text, Phone())
        )
        self.user_info("Added new phone!")

    def read_from_file(self):
        self.bank.read_info = 'bank.pickle'
        self.human.read_file = 'human.pickle'

