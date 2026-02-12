import time
import sys
import datetime
import pathlib
from collections import deque

ROOT = pathlib.Path(__file__).resolve().parent

def temperature() -> float:
    with open("/sys/class/thermal/thermal_zone1/temp", "r") as f:
        return int(f.read()) / 1000

def clear(value: int) -> None:
    for _ in range(value): 
        sys.stdout.write('\x1b[1A\x1b[2K')
    sys.stdout.flush()

def logs(info: list) -> None:
    with open(ROOT / 'logs.txt', 'a') as f:
        f.writelines(info)

windows = deque(maxlen=60)
def moving_avg(data: float) -> float:
    windows.append(data)
    return sum(windows) / len(windows)

def main():
    first_read = temperature()
    maximum = minimum = first_read
    logs_list = []

    print("\n           --- CPU Monitoring ---")
    try:
        while True:
            result = temperature()
            if result > maximum: # max temp of cpu
                maximum = result
            if result < minimum: # min temp of cpu
                minimum = result            
            avg = moving_avg(result)

            string_format = f'TEMP: {result} | AVG: {avg:.1f} | MIN: {minimum} | MAX: {maximum}'
            print(string_format)
            logs_list.append(f'{string_format} | {datetime.datetime.now().strftime("%H:%M:%S")}\n')    

            if len(logs_list) >= 10:
                logs(logs_list)
                logs_list.clear()
            
            time.sleep(1)
            clear(1)

    except KeyboardInterrupt:
        print("\nStop monitoring...")
    finally: 
        logs(logs_list)

if __name__ == "__main__":
    main()