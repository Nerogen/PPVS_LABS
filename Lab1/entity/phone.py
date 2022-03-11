class Phone:
    def __init__(self):
        self.__phone_account = 0

    @property
    def phone_account(self) -> int:
        return self.__phone_account

    @phone_account.setter
    def phone_account(self, value) -> None:
        self.__phone_account += value
