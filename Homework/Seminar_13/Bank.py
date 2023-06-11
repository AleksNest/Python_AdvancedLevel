"""
банкомат по выдачи и зачислению cash  с учетом комиссии на снятие денег и начисленнию процентов
"""

from datetime import date
from My_exception import ValueBankError


class Bankomat:
    __bank: float = 0
    count: int = 0

    def __init__(self, account_num: int, name_bank: str, percent_take: float = 0.015, percent_add: float = 0.03, percent_tax: float = 0.01):
        self.account_num = account_num
        self.name_bank = name_bank
        self.percent_add = percent_add
        self.percent_tax = percent_tax
        self.percent_take = percent_take

    def add_bank(self, cash: float) -> None:
        self.__bank += cash
        self.count += 1
        if self.count % 3 == 0:
            self.__bank = self.__bank + self.percent_add * self.__bank
            print("начислены проценты в размере: ", self.percent_add * self.__bank)

    def take_bank(self, cash: float) -> None:
        self.__bank -= cash
        self.count += 1

        if cash * self.percent_take < 30:
            self.__bank -= 30
            print("списаны проценты за cash: ", 30)
        elif cash * self.percent_take > 600:
            self.__bank -= 600
            print("списаны проценты за cash: ", 600)
        else:
            self.__bank -= cash * self.percent_take
            print("списаны проценты за cash: ", cash * self.percent_take)
        if self.count % 3 == 0:
            self.__bank = self.__bank + self.percent_take * self.__bank
            print("начислены проценты в размере: ", self.percent_add * self.__bank)

    def exit_bank(self):
        print("Рады вас видетеь снова!\n")
        exit()

    def check_bank(self) -> int:
        while True:
            cash = int(input("Введите сумму опреации кратно 50\n"))
            if cash % 50 == 0:
                return cash

    def get_bank(self):
        return self.__bank

    def set_bank(self, bank: float):
        self.__bank = bank


if __name__ == '__main__':
    accounts = []
    list_operation = []

    while(True):
        try:
            account_num = int(input("введите номер счета(целое число): "))
            break
        except ValueError as e:
            print(f"\nНеправильный формат ввода данных: {e}.\n")

    name_bank = input("введите название банка: ")
    accounts.append(Bankomat(account_num, name_bank))
    i = 0
    j = 0


    while True:
        action = input("1 - снять деньги\n2 - пополнить\n3 - баланс\n4 - вывести историю всех операций\n5 "
                       "- создать новый аккаунт(счет)\n6 - перейти на аккаунт(счет)\n7 - список акаунтов\n8 - выход\n")

        if action == '1':
            if accounts[i].get_bank() > 5_000_000:
                accounts[i].set_bank(accounts[i].get_bank() - accounts[i].get_bank() * accounts[i].percent_tax)
                print("списан налог на богатство: ", accounts[i].get_bank() * accounts[i].percent_tax)
            cash = accounts[i].check_bank()
            if cash < accounts[i].get_bank():
                accounts[i].take_bank(cash)
                list_operation.append([i, str(date.today()), -1 * cash,accounts[i].get_bank()])
            else:
                print("no money\n")
            if accounts[i].get_bank() > 5_000_000:
                accounts[i].set_bank(accounts[i].get_bank() - accounts[i].get_bank() * accounts[i].percent_tax)
                print("списан налог на богатство: ", accounts[i].get_bank() * accounts[i].percent_tax)
            print("Баланс = ", accounts[i].get_bank())
        elif action == '2':
            cash = accounts[i].check_bank()

            if cash < 0:
               raise ValueBankError(cash)

            accounts[i].add_bank(cash)
            if accounts[i].get_bank() > 5_000_000:
                accounts[i].set_bank(accounts[i].get_bank() - accounts[i].get_bank() * accounts[i].percent_tax)
                print("списан налог на богатство: ", accounts[i].get_bank() * accounts[i].percent_tax)
            print("Баланс = ", accounts[i].get_bank())

            list_operation.append([i, str(date.today()), cash, accounts[i].get_bank()])

        elif action == '3':
            print("Баланс = ", accounts[i].get_bank())
        elif action == '4':
            print("id  Date  Cash  Balance")
            print(list_operation)
        elif action == '5':
            account_num = int(input("введите номер счета(целое число): "))
            name_bank = input("введите название банка: ")
            accounts.append(Bankomat(account_num, name_bank))
            j = j + 1
            i = j
        elif action == '6':
            i = int(input(f'Введите целое число от 0 до {j}\n'))
            while i > j:
                i = int(input(f'аккаунт не существует\nВведите целое число от 0 до {j}'))
        elif action == '7':
            print(f'id      №сч       банк    баланс')
            for i in range(len(accounts)):
                print(f'{i:<8}{accounts[i].account_num:<10}{accounts[i].name_bank:<8}{accounts[i].get_bank():<8}')
            print('\n')
        else:
            accounts[i].exit_bank()