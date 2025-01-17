```
# WinStabilizer

WinStabilizer is a Python program designed to monitor and adjust system settings on Windows to prevent crashes and enhance system stability. It checks for high CPU and memory usage and takes actions to mitigate potential system instability.

## Features

- Monitors CPU and memory usage.
- Clears temporary files to free up space and reduce system load.
- Adjusts virtual memory settings to optimize performance.

## Installation

1. Ensure you have Python installed on your Windows system.
2. Clone this repository or download the `win_stabilizer.py` file.
3. Install required packages using pip:

   ```bash
   pip install psutil
   ```

## Usage

Run the WinStabilizer script using Python:

```bash
python win_stabilizer.py
```

The program will log its activities in the `win_stabilizer.log` file located in the same directory.

## Configuration

- You can adjust the CPU and memory usage thresholds by modifying the `check_cpu_usage(threshold=80)` and `check_memory_usage(threshold=80)` functions.

## Logging

- All activities are logged in `win_stabilizer.log` for troubleshooting and monitoring purposes.

## License

This project is licensed under the MIT License.