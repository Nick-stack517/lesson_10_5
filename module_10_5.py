"""
Для избежания некорректного вывода запускайте линейный вызов и многопроцессный по отдельности,
предварительно закомментировав другой.
"""
import multiprocessing
import time


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline().strip()
            all_data.append(line)
            if not line:
                break


filenames = [f'./file {number}.txt' for number in range(1, 5)]

start_t1 = time.time()

# Линейный вызов
for filename in filenames:
    print(filename)
    read_info(filename)

stop_t1 = time.time()
line_time = stop_t1 - start_t1
print(f'Время работы линейного вызова : {line_time} сек.')


# Многопроцессный
if __name__ == '__main__':
    start_t2 = time.time()

    with multiprocessing.Pool(processes=4) as p:
        p.map(read_info, filenames)

    stop_t2 = time.time()

    multiprocessing_time = stop_t2 - start_t2
    print(f'Время работы многопроцессного : {multiprocessing_time} сек.')
