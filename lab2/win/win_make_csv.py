import psutil
import time
import csv
def get_free_memory():
    mem = psutil.virtual_memory()
    return mem.available

def log_metrics():
    with open("free_memory.csv", "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["free_memory", "time"])
        start_point_time = time.perf_counter()
        while time.perf_counter() - start_point_time <= 120:
            current_time = time.strftime("%H:%M:%S", time.localtime())
            free_memory = get_free_memory()//(1024**2)    #МБ
            writer.writerow([free_memory, current_time])
            file.flush()
            time.sleep(1)

if __name__ == "__main__":
    log_metrics()