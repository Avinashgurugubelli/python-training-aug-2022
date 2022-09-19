
"""
Association:

If two classes in a model need to communicate with each other, there must be a link between them. This link can be represented by an association. Associations can be represented in a class diagram by a line between these classes with an arrow indicating the navigation direction.
By default, associations are always assumed to be bi-directional; this means that both classes are aware of each other and their relationship.
By contrast, in a uni-directional association, two classes are related - but only one class knows that the relationship exists.
In terms of coding:
An Object of class B is passed as an argument to a method of Class A. (or)

An object of class B is a local variable in a method of class A.

"""


class Account:

    def __init__(self, account_number, amount) -> None:
        self.__account_number = account_number
        self.__balance_amount = amount

    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance_amount

    def deposit(self, amount):
        self.__balance_amount += amount

    def withdraw(self, amount):
        if(self.__balance_amount > amount):
            self.__balance_amount -= amount
        else:
            print("In sufficient balance in account")


class ATM:

    # Association: Here account is used as a argument in a method of ATM class
    def show_balance(self, account):
        print(
            f'Balance: {account.balance}, in account {account.account_number}')

    def withdraw_amount(self, account, amount):
        print(
            f'Withdrawing the amount {amount}, from given account : {account.account_number}')
        account.withdraw(amount)


account_1 = Account(2566893, 5000)
account_2 = Account(8996236, 6000)

atm = ATM()
atm.show_balance(account=account_1)
atm.withdraw_amount(account=account_1, amount=1000)
atm.show_balance(account=account_1)
atm.show_balance(account_2)
