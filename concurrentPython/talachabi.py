import logging
import threading
import time
import concurrent.futures


class FakeDatabase:
    def __init__(self) -> None:
        self.value = 0
        self._lock = threading.Lock()

    #Mutex = MUTual EXclusion a.k.a lock
    def locked_update(self, name: str) -> None:
        logging.info('Thread %s: starting update', name)
        logging.debug('Thread %s: about to start', name)
        with self._lock:
            logging.debug('Thread %s has lock', name)
            local_copy = self.value
            local_copy += 1 # race condition happens here.
            time.sleep(0.2)
            self.value = local_copy
            logging.debug('Thread %s about to release lock', name)
        logging.debug('Thread %s after release', name)
        logging.info('Thread %s: finishing update', name)

