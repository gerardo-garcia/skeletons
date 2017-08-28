#!/usr/bin/env python
import multiprocessing
import threading
import time

def good_worker():   
    print "[GoodWorker] Starting"
    time.sleep(4)
    print "[GoodWorker] all good"

def bad_worker():
    print "[BadWorker] Starting"
    time.sleep(2)
    raise Exception("ups!")

class MyProcManager(object):
    def __init__(self):
        self.procs = []
        self.errors_flag = False
        self._threads = []
        self._lock = threading.Lock()

    def terminate_all(self):
        with self._lock:
            for p in self.procs:
                if p.is_alive():
                    print "Terminating %s" % p
                    p.terminate()

    def launch_proc(self, func, args=(), kwargs= {}):
        t = threading.Thread(target=self._proc_thread_runner,
                             args=(func, args, kwargs))
        self._threads.append(t)
        t.start()

    def _proc_thread_runner(self, func, args, kwargs):
        p = multiprocessing.Process(target=func, args=args, kwargs=kwargs)
        self.procs.append(p)
        p.start()
        while p.exitcode is None:
            p.join()
        if p.exitcode > 0:
            self.errors_flag = True
            self.terminate_all()

    def wait(self):
        for t in self._threads:
            t.join()

if __name__ == '__main__':
    proc_manager = MyProcManager()
    proc_manager.launch_proc(good_worker) 
    proc_manager.launch_proc(good_worker) 
    proc_manager.launch_proc(bad_worker) 
    proc_manager.wait()
    if proc_manager.errors_flag:
        print "Errors flag is set: some process crashed"
    else:
        print "Everything closed cleanly"

