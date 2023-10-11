import csv
import matplotlib.pyplot as plt

def graph():
    with open("linux_make_csv.py", "r", encoding="utf-8") as file:
        data = list(csv.reader(file))[1:]
        free_memory = [int(line[0]) for line in data]
        date_time = [_+1 for _ in range(len(data))]
    plt.xlabel('date_time')
    plt.ylabel('free_memorry')
    plt.plot(date_time, free_memory, 'o-g', label='prcs(t)')
    plt.legend()
    plt.show()
    return [line[1] for line in data]

print(graph())