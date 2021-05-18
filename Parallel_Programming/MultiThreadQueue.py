## Multi Threading with Queue

from queue import Queue
from threading import Thread

def producer(q):
    for i in range(5):
        q.put(i)
        print('published', i)
def consumer(q):
    while True:
        data = q.get()
        print('consumed', data)

if __name__ == "__main__":

    q = Queue()

    # creating processes
    t1 = Thread(target=producer, args=(q, ))
    t2 = Thread(target=consumer, args=(q, ))
  
    # starting process 1
    t2.start()
    # starting process 2
    t1.start()

    # wait until process 1 is finished
    t1.join()
    # wait until process 2 is finished
    t2.join()
  
    # both processes finished
    print("Done!")