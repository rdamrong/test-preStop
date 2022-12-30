import signal
import os
import sys
import time
import logging

def terminateProcess(signalNumber, frame):
    logging.warning('(SIGTERM) terminating the process')
    ctime = int(time.time())
    while True:
        logging.warning('{:d} secs :: SIGTERM cannot kill me !!! 5555'.format(int(time.time()) - ctime ))
        time.sleep(1)

if __name__ == '__main__':
    signal.signal(signal.SIGTERM, terminateProcess)

    logging.basicConfig(format="%(asctime)s - {} - %(message)s".format(os.getenv('HOSTNAME')),datefmt='%d-%b-%y %H:%M:%S')
    logging.warning('d8k-termloop v1.0')
    logging.warning('Process ID: %d', os.getpid())
    logging.warning('Starting app')

    while True:
        logging.warning('Working...')
        time.sleep(600)
