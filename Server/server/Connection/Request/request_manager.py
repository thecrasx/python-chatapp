from threading import Thread
from time import sleep




class RequestManager:
    def __init__(self):
        self._read = False
        self._write = False

        self._readQueue = []
        self._writeQueue = []


    def add_db_queue(self):
        pass







class _Switch:
    def __init__(self, readQueue, writeQueue):
        self.work_time = 2

        self._lock = False

        