from threading import Lock




class DBLocker:
    def __init__(self):
        self._locker = Lock()

    def lock(self):
        if not self.isLocked():
            self._locker.acquire()


    def release(self):
        if self.isLocked():
            self._locker.release()


    def isLocked(self):
        return self._locker.locked()

    def wait(self):
        while self.isLocked():
            continue