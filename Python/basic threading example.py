from queue import Queue
from threading import Thread

def do_stuff(q):
  while True:
    print (q.get())
    q.task_done()

q = Queue(maxsize=0)

worker = Thread(target=do_stuff, name='thread',args=(q,))
worker.setDaemon(True)
worker.start()


for i in range(10):
    q.put(i)

q.join()
