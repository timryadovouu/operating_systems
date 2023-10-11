import csv
import matplotlib.pyplot as plt

def graph():
    with open("total_data.csv", "r", encoding="utf-8") as file:
        data = list(csv.reader(file))[1:]
        processes = [int(line[0]) for line in data]
        date_time = [_+1 for _ in range(len(data))]
    plt.xlabel('date_time')
    plt.ylabel('processes')
    plt.plot(date_time, processes, 'o-g', label='prcs(t)')
    plt.legend()
    plt.show()
    return [line[1] for line in data]

print(graph())