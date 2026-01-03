import logging
import os

from from_root import from_root
from datetime import datetime

LOG_FILE_PATH = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"


logs_dir=os.path.join(from_root(),"logs")
os.makedirs(logs_dir,exist_ok=True)
logs_path=os.path.join(logs_dir,LOG_FILE_PATH)
logging.basicConfig(
    filename=logs_path, 
    format="[%(asctime)s] %(name)s -%(levelname)s - %(message)s",
    level=logging.DEBUG,
)