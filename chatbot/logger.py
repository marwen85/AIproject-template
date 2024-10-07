import logging
import os
from datetime import datetime

# Create a log file with a timestamp
log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(), "logs")
os.makedirs(log_path, exist_ok=True)  # Create the logs directory if it does not exist
log_filePath = os.path.join(log_path, log_file)

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Use logging.INFO (constant) instead of logging.info (function)
    filename=log_filePath,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
)

# Test the logging setup
if __name__ == '__main__':
    logging.info("Here again, I am testing the logging setup")