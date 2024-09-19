import threading
import random as r
from time import sleep


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            deposit_sum = r.randint(50, 500)
            self.balance += deposit_sum
            print(f'Пополнение: {deposit_sum}. Баланс: {self.balance}.')
            sleep(0.001)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

    def take(self):
        for _ in range(100):
            take_sum = r.randint(50, 500)
            print(f'Запрос на {take_sum}.')
            if take_sum <= self.balance:
                self.balance -= take_sum
                print(f'Снятие: {take_sum}. Баланс: {self.balance}.')
            else:
                print('Запрос отклонён, недостаточно средств.')
                self.lock.acquire()


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
