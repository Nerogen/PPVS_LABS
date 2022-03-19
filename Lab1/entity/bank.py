from Lab1.logic.serialization import Serialization
from Lab1.logic.validation import Validation


class Bank:
    def __init__(self, bank_accounts_of_users: dict, phones: dict, read_file: str):
        self.__phones_info = phones
        self.__bank_info = bank_accounts_of_users
        self.__read_info = read_file

    @property
    def read_info(self) -> str:
        return self.__read_info

    @read_info.setter
    def read_info(self, file_name) -> None:
        bank_accounts, phone_numbers = Serialization.read(file_name)
        self.__phones_info = phone_numbers
        self.__bank_info = bank_accounts
        self.__read_info = file_name

    @property
    def bank_info(self) -> dict:
        return self.__bank_info

    @property
    def phones_info(self) -> dict:
        return self.__phones_info

    @bank_info.setter
    def bank_info(self, value) -> None:
        self.__bank_info = value

    @phones_info.setter
    def phones_info(self, value) -> None:
        self.__phones_info = value

    def update_bank_accounts_of_users(self, new_account: tuple) -> None:
        if not (self.__bank_info.get(new_account[0], None) is None) or len(new_account) != 2:
            raise ValueError
        else:
            self.__bank_info[new_account[0]] = new_account[1]
            Serialization.write((self.__bank_info, self.__phones_info), self.read_info)

    def update_phones_info(self, new_account: tuple) -> None:
        if not (self.__phones_info.get(new_account[0], None) is None) or len(new_account) != 2:
            raise ValueError
        else:
            self.__phones_info[new_account[0]] = new_account[1]
            Serialization.write((self.__bank_info, self.__phones_info), self.read_info)

    def put_money_on_the_card(self, human, money: int, account: int, card_number: int, pin_code: int) -> None:
        if Validation.card_valid(self, card_number, pin_code, account) and Validation.self_balance(human, money):
            self.__bank_info[account].bank_account = money
            Serialization.write((self.__bank_info, self.__phones_info), self.read_info)
        else:
            raise ValueError

    def take_money_from_the_card(self, value: int, account: int, card_num: int, pin_code: int) -> None:
        if Validation.card_valid(self, card_num, pin_code, account) and Validation.balance_valid(self, account, value):
            self.__bank_info[account].bank_account = -value
            Serialization.write((self.__bank_info, self.__phones_info), self.read_info)
        else:
            raise ValueError

    def credit_card_info(self, account: int, card_number: int, pin_code: int) -> str:
        if Validation.card_valid(self, card_number, pin_code, account):
            return str(self.__bank_info[account].bank_account) + '$'
        else:
            raise ValueError

    def put_money_on_phone(self, account: int, phone_number: str, value: int, card_num: int, pin_code: int) -> None:
        if Validation.card_valid(self, card_num, pin_code, account) and Validation.balance_valid(self, account, value):
            self.__phones_info[phone_number].phone_account = value
            self.__bank_info[account].bank_account = -value
            Serialization.write((self.__bank_info, self.__phones_info), self.read_info)
        else:
            raise ValueError
