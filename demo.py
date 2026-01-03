from USA_Visa.logger import logging
from USA_Visa.exception import CustomException
import sys

# logging.info("Demo file is runnning")

try:
    a=4/0
except Exception as e:
    logging.info("Divide by zero exception occured")
    raise CustomException(e,sys)