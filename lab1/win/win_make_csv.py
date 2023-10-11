import csv
import psutil
import time

# file_path = "process_count.txt"
# file = open(file_path, "w")
# start_point_time = time.perf_counter()
# while time.perf_counter() - start_point_time <= 10:
#     current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#     process_count = len(psutil.pids())
#     file.write(f"{current_time} - {process_count}\n")
#     file.flush()
#     time.sleep(1)

with open("data.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["process", "time"])
    start_point_time = time.perf_counter()
    while time.perf_counter() - start_point_time <= 180:
        current_time = time.strftime("%H:%M:%S", time.localtime())
        process_count = len(psutil.pids())
        writer.writerow([process_count,current_time])
        file.flush()
        time.sleep(1)