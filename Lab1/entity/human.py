from Lab1.logic.serialization import Serialization


class Human:
    def __init__(self, bank_accounts: dict, phones: dict, cash: int, read_file: str):
        self.__bank_accounts = bank_accounts
        self.__phones = phones
        self.__cash = cash
        self.__read_info = read_file

    @property
    def bank_accounts(self) -> dict:
        return self.__bank_accounts

    @property
    def phones(self) -> dict:
        return self.__phones

    @property
    def cash(self) -> int:
        return self.__cash

    @property
    def read_file(self) -> str:
        return self.__read_info

    @read_file.setter
    def read_file(self, file_name) -> None:
        bank_accounts, phone_numbers, cash = Serialization.read(file_name)
        self.__cash = cash
        self.__phones = phone_numbers
        self.__bank_accounts = bank_accounts
        self.__read_info = file_name

    @bank_accounts.setter
    def bank_accounts(self, value: dict) -> None:
        self.__bank_accounts = value
        Serialization.write((self.__bank_accounts, self.__phones, self.__cash), self.__read_info)

    @phones.setter
    def phones(self, value: dict) -> None:
        self.__phones = value
        Serialization.write((self.__bank_accounts, self.__phones, self.__cash), self.__read_info)

    @cash.setter
    def cash(self, value: int) -> None:
        self.__cash = value
        Serialization.write((self.__bank_accounts, self.__phones, self.__cash), self.__read_info)

    def get_cash(self, value: int) -> None:
        self.__cash += value
        Serialization.write((self.__bank_accounts, self.__phones, self.__cash), self.__read_info)

    def update_bank_accounts(self, new_account: tuple) -> None:
        self.__bank_accounts[new_account[0]] = new_account[1]
        Serialization.write((self.__bank_accounts, self.__phones, self.__cash), self.__read_info)

    def update_phone_accounts(self, new_account: tuple) -> None:
        self.__phones[new_account[0]] = new_account[1]
        Serialization.write((self.__bank_accounts, self.__phones, self.__cash), self.__read_info)
