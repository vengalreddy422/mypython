#Program for Demonstrating the logging Concept.
#LogEx4.py
import logging
logging.basicConfig(level=logging.ERROR,format='%(asctime)s  : %(levelname)s: %(message)s',datefmt='%d-%m-%Y  %I:%M:%S %p ')
logging.critical("critical message")
logging.error("error message")
logging.warning("warning message")
logging.info("Informational error message")
logging.debug("Debug error message")