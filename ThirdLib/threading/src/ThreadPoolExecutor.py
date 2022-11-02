import concurrent.futures
import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    # time.sleep(2)
    logging.info("Thread %s: finishing", name)
# [rest of code]

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    loop_num = 1000000
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(thread_function, range(loop_num))