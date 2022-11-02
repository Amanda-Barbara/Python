import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,), daemon=True)
    logging.info("Main    : before running thread")
    x.start() 
    # 如果后面语句中没有x.join()，参数daemon=True，当主线程结束时，进程结束；
    # 如果此时子线程还没有结束，系统会结束当前正在运行的子线程。
    logging.info("Main    : wait for the thread to finish")
    # x.join() 
    logging.info("Main    : all done")