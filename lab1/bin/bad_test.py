import csv, time, psutil
from datetime import datetime
import matplotlib.pyplot as plt


def fork():
    with open("test_1.csv", "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["process", "time"])
        start_point_time = time.perf_counter()
        while time.perf_counter() - start_point_time <= 10:
            writer.writerow([len(list(psutil.process_iter())), f"{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}"])
            time.sleep(1)
    return True
def graph():
    with open("test_1.csv", "r", encoding="utf-8") as file:
        data = list(csv.reader(file))[1:]
        processes = [int(line[0]) for line in data]
        date_time = [_+1 for _ in range(len(data))]
    plt.xlabel('date_time')
    plt.ylabel('processes')
    plt.plot(date_time, processes, 'o-g', label='prcs(t)')
    plt.legend()
    plt.show()
    return date_time

fork()
print(graph())