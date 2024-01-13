import logging
from datetime import datetime

def print_debug(message):
    filename = "../log/LOG " + datetime.now().strftime("%d-%m-%Y %H-%M-%S")
    logging.basicConfig(filename=filename, filemode='a',
                        format="%(asctime)s, %(msecs)d %(name)s %(levelname)s [%(filename)s-%(lineno)d-%(funcName)s]  : %(message)s",
                        datefmt="%H:%M:%S",
                        level=logging.INFO)
    logging.info(message)




