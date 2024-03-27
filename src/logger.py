import logging
import os
from datetime import datetime

# Logging is essential for monitoring and debugging aplications
# It allows developers to record information about the program's execution, errors, warnings, and other relevant events. 

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
 # 'LOG_FILE' is a string variable that contains the name of the log file.

# 'logs_path' is a string variable that contains the path to the directory where log files will be stored.
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

# 'LOG_FILE_PATH' is a string variable that contains the full path to the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
