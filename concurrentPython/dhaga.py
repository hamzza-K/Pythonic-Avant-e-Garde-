import logging
import threading
import time
import random
import concurrent.futures

def thread_function(name: str) -> str:
    """A thread function."""
    logging.info('thread %s: starting', name)
    time.sleep(random.randint(0, 3))
    logging.info('thread %s: finishing', name)

if __name__ == '_main__':
    FORMAT = '%(asctime)s: %(message)s'
    logging.basicConfig(format=FORMAT, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(thread_function, range(5))
    # logging.info('Main: before creating thread')
    # x = threading.Thread(target=thread_function, args=(1,), daemon=True)
    # logging.info('Main: before running thread')
    # x.start()
    # logging.info('Main: wait for the thread to finish')
    # x.join()
    # logging.info('Main: all done')