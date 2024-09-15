from threading import Thread
from time import sleep


class Knight(Thread):
    num_enemies = 100
    count_days = 0

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.num_enemies != 0:
            self.num_enemies -= self.power
            self.count_days += 1
            print(f'{self.name} сражается {self.count_days} день(дня)..., осталось {self.num_enemies} воинов.')
            sleep(1)
        print(f'{self.name} одержал победу спустя {self.count_days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
