import os
import sys
import logging 

logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir = "logs"
log_filepath = os.path.join(log_dir,'running_logs.log')
os.makedirs(log_dir, exist_ok=True) 

logging.basicConfig(
    level = logging.INFO,
    format = logging_str, 
    handlers = [
        logging.FileHandler(log_filepath),          #Logs into the mentioned file   
        logging.StreamHandler(sys.stdout)           #Shows logs in the terminal
    ]
)


logger = logging.getLogger("deepClassifierLogger")      #getLogger() function accepts a single argument - the logger's name.