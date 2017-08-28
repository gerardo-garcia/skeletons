#!/usr/bin/env python
from multiprocessing import Process, Queue, cpu_count
import random
import time


def serve(queue):
    works = ["task_1", "task_2"]
    while True:
        time.sleep(0.1)
        queue.put(random.choice(works))


def work(id, queue):
    while True:
        task = queue.get()
        if task is None:
            break
        time.sleep(0.5)
        print "%d task:" % id, task
    queue.put(None)


class Manager:
    def __init__(self):
        self.queue = Queue()
        #self.NUMBER_OF_PROCESSES = cpu_count()
        self.NUMBER_OF_PROCESSES = 2

    def start(self):
        print "starting %d workers" % self.NUMBER_OF_PROCESSES
        self.workers = [Process(target=work, args=(i, self.queue,))
                        for i in xrange(self.NUMBER_OF_PROCESSES)]
        for w in self.workers:
            w.start()

        serve(self.queue)

    def stop(self):
        self.queue.put(None)
        for i in range(self.NUMBER_OF_PROCESSES):
            self.workers[i].join()
        self.queue.close()


if __name__ == '__main__':
    m = Manager()
    m.start()

