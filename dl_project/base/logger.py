import os
import sys
import logging
from datetime import datetime

# Define log file and log directory
log_dir = 'logs'
log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(log_dir, log_file)
logging_format = "%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"

# Ensure the log directory exists
os.makedirs(log_dir, exist_ok=True)

log_level = os.getenv("LOG_LEVEL", "DEBUG").upper()

# Get logger
logger = logging.getLogger(__name__)
logger.setLevel(getattr(logging, log_level))  # Set the default log level

# Avoid adding handlers multiple times
if not logger.handlers:
    # Create handlers
    file_handler = logging.FileHandler(logs_path)
    stream_handler = logging.StreamHandler(sys.stdout)

    # Set logging format
    formatter = logging.Formatter(logging_format)
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)