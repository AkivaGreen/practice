import logging
import threading
import time
from datetime import datetime

front_lidar_logger = logging.getLogger('front_lidar')
fll_fh = logging.FileHandler('./logging/logs/front_lidar.log')
fll_fh.setLevel(logging.INFO)
fll_ch = logging.StreamHandler()
fll_ch.setLevel(logging.INFO)
fll_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
fll_fh.setFormatter(fll_formatter)
fll_ch.setFormatter(fll_formatter)
front_lidar_logger.addHandler(fll_fh)
front_lidar_logger.addHandler(fll_ch)
front_lidar_logger.info("Hello World!")
front_lidar_logger.debug('debug message')
front_lidar_logger.info('info message')
front_lidar_logger.warn('warn message')
front_lidar_logger.error('error message')
front_lidar_logger.critical('critical message')

back_lidar_logger = logging.getLogger('back_lidar')
bll_fh = logging.FileHandler('./logging/logs/back_lidar.log')
bll_fh.setLevel(logging.DEBUG)
bll_ch = logging.StreamHandler()
bll_ch.setLevel(logging.ERROR)
bll_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
bll_fh.setFormatter(bll_formatter)
bll_ch.setFormatter(bll_formatter)
back_lidar_logger.addHandler(bll_fh)
back_lidar_logger.addHandler(bll_ch)

def readFrontLidar():
    print("Front Lidar Thread Starting...")
    try:
        start = datetime.now()
        while (datetime.now() - start).seconds < 10:
            #data = {'lidar': 'F', 'distance': 200, 'strength': 3000, 'now': datetime.now()}
            front_lidar_logger.info("test")
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Front Lidar Thread Stopping...")

def readBackLidar():
    print("Back Lidar Thread Starting...")
    try:
        start = datetime.now()
        while (datetime.now() - start).seconds < 10:
            #data = {'lidar': 'B', 'distance': 300, 'strength': 2000, 'now': datetime.now()}
            back_lidar_logger.info("test")
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Back Lidar Thread Stopping...")

if __name__ == '__main__':
    try:
        print("Program Starting...")
        front_lidar_thread = threading.Thread(target=readFrontLidar)
        front_lidar_thread.start()
        
        back_lidar_thread = threading.Thread(target=readBackLidar)
        back_lidar_thread.start()

        front_lidar_thread.join()
        back_lidar_thread.join()
    except KeyboardInterrupt:
        print("Program Stopping...")
        time.sleep(2)
