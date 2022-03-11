class Validation:
    @staticmethod
    def card_valid(bank, card_number: int, pin_code: int, account: int) -> bool:
        return bank.bank_info[account].card_number == card_number and bank.bank_info[account].pin_code == pin_code

    @staticmethod
    def balance_valid(bank, account: int, amount_of_money: int) -> bool:
        return bank.bank_info[account].bank_account >= amount_of_money

    @staticmethod
    def self_balance(human, amount_of_money: int) -> bool:
        return human.cash >= amount_of_money
