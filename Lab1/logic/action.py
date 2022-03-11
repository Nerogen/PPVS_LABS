class Action:

    @staticmethod
    def put_money_on_the_card(bank, human, account: int, money: int, card_number: int, pin_code: int):
        try:
            bank.put_money_on_the_card(human, money, account, card_number, pin_code)
            human.get_cash(-money)
        except ValueError:
            print("Account doesn't exist or not have enough of money!")

    @staticmethod
    def take_money_from_the_card(bank, human, account: int, money: int, card_number: int, pin_code: int):
        try:
            bank.take_money_from_the_card(money, account, card_number, pin_code)
            human.get_cash(money)
        except ValueError:
            print("Account doesn't exist or not have enough of money!")

    @staticmethod
    def get_account_info(bank, bank_account: int, card_number: int, pin_code: int) -> str:
        try:
            return bank.credit_card_info(bank_account, card_number, pin_code)
        except ValueError:
            print("Account doesn't exist!")

    @staticmethod
    def registration_new_credit_card(bank, human, new_account: tuple):
        try:
            bank.update_bank_accounts_of_users(new_account)
            human.update_bank_accounts(new_account)
        except ValueError:
            print("Incorrect data!")

    @staticmethod
    def registration_new_phone(bank, human, new_account: tuple):
        try:
            bank.update_phones_info(new_account)
            human.update_phone_accounts(new_account)
        except ValueError:
            print("Incorrect data!")

    @staticmethod
    def put_money_on_phone(bank, human, phone: str, account: int, value: int, card_num: int, pin_code: int):
        try:
            bank.put_money_on_phone(account, phone, value, card_num, pin_code)
            human.get_cash(-value)
        except ValueError:
            print("Account doesn't exist or not have enough of money!")
