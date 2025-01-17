import psutil
import os
import logging
import subprocess
from time import sleep

# Configure logging
logging.basicConfig(filename='win_stabilizer.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def check_cpu_usage(threshold=80):
    """Check if CPU usage is above the threshold."""
    usage = psutil.cpu_percent(interval=1)
    if usage > threshold:
        logging.warning(f'High CPU usage detected: {usage}%')
        return True
    return False

def check_memory_usage(threshold=80):
    """Check if Memory usage is above the threshold."""
    memory_info = psutil.virtual_memory()
    usage = memory_info.percent
    if usage > threshold:
        logging.warning(f'High Memory usage detected: {usage}%')
        return True
    return False

def clear_temp_files():
    """Clear temporary files to free up space."""
    temp_dir = os.getenv('TEMP')
    if temp_dir and os.path.exists(temp_dir):
        try:
            for root, dirs, files in os.walk(temp_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
            logging.info('Temporary files cleared successfully.')
        except Exception as e:
            logging.error(f'Error clearing temporary files: {e}')

def adjust_virtual_memory():
    """Adjust virtual memory settings."""
    try:
        subprocess.run('wmic computersystem where name="%computername%" set AutomaticManagedPagefile=True', shell=True)
        logging.info('Virtual memory adjusted successfully.')
    except Exception as e:
        logging.error(f'Error adjusting virtual memory: {e}')

def monitor_system():
    """Monitor system resources and adjust settings."""
    while True:
        if check_cpu_usage() or check_memory_usage():
            clear_temp_files()
            adjust_virtual_memory()
        sleep(60)

if __name__ == "__main__":
    logging.info('WinStabilizer started.')
    monitor_system()