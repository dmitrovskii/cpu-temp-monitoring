# СPU Temp Monitor (Linux)
A lightweight Python utility for monitoring CPU temperature in real-time with data logging and moving average calculation.

# Features
1. **Real-time monitoring:** Smooth console updates using **ANSI escape codes** (no flickering or scrolling).
2. **Smart logging:** Buffered I/O logic that writes to disk every 10 entries to **save disk lifespan**.
3. **Moving average:** Calculates the average temperature over a sliding window (last 60 seconds/10 samples).
4. **Safe shutdown:** Graceful interruption handling with `try...finally` to ensure all buffered logs are saved on `Ctrl + C`.

# Tech Stack

| Technology | Usage |
| :--- | :--- |
| **Python 3.x**          | Core logic and execution | 
| **Pathlib**             | Robust cross-platform path management |
| **Collections (deque)** | Memory-efficient sliding window for AVG |
| **Linux Sysfs**         | Direct reading from the kernel thermal zone |

# Troubleshooting (Error Handling)
If you see incorrect data or errors, it might be due to a different thermal zone index on your hardware.
1. Open `main.py`.
2. Locate the `temperature()` function (around line 14).
3. Change `/thermal_zone1/` to `/thermal_zone0/` or check your `/sys/class/thermal/` directory to find the correct path.

# Screenshot

<img width="1440" height="873" alt="image" src="https://github.com/user-attachments/assets/2620a199-c00e-4581-8cc4-310ab473356a" />


