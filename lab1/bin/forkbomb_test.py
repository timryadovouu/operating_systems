import time
import os

start_point_time = time.perf_counter()
while time.perf_counter() - start_point_time <= 10:
    os.fork()
    time.sleep(1)
