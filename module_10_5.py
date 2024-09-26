import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name) as file:
        while file.readline():
            all_data.append(file.readline())


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
start = datetime.now()
for i in filenames:
    read_info(i)
end = datetime.now()
print(end - start)

# # Многопроцессный вызов
# if __name__ == '__main__':
#     start = datetime.now()
#     with multiprocessing.Pool(processes=4) as pool:
#         pool.map(read_info, filenames)
#     end = datetime.now()
#     print(end - start)
