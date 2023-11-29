import csv
import matplotlib.pyplot as plt
def plot_memory_graph(times, free_memory):
    plt.plot(times, free_memory, marker='o')
    plt.title('Свободная память во времени')
    plt.xlabel('Время')
    plt.ylabel('Свободная память (МБ)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
def graph():
    with open("free_memory_1.csv", "r", encoding="utf-8") as file:
        data = list(csv.reader(file))[1:]
        free_memory = [int(line[0]) for line in data]
        date_time = [line[1] for line in data]
        plot_memory_graph(date_time, free_memory)

graph()

