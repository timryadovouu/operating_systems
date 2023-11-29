import psutil
from datetime import datetime
import time
import csv


def main():
    with open("free_memory_1.csv", "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["free_memory", "time"])
        start_point_time = time.perf_counter()
        while time.perf_counter() - start_point_time <= 20:
            current_time = datetime.now().strftime('%H:%M:%S')
            free_memory = psutil.virtual_memory().available // (1024 ** 2)   #МБ
            writer.writerow([free_memory, current_time])
            file.flush()
            time.sleep(1)

main()
