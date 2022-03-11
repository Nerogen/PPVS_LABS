class CreditCard:

    def __init__(self, card_number: int, pin_code: int):
        self.__card_number = card_number
        self.__pin_code = pin_code
        self.__bank_account = 0

    @property
    def card_number(self) -> int:
        return self.__card_number

    @property
    def pin_code(self) -> int:
        return self.__pin_code

    @property
    def bank_account(self) -> int:
        return self.__bank_account

    @bank_account.setter
    def bank_account(self, value: int) -> None:
        self.__bank_account += value
