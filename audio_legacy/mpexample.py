from multiprocessing import Process
import time

class pseudoclass:
    def __init__(self):
        self.val=114514
        pass
    def a(self):
        while(1):
            time.sleep(0.1)
            print(self.val)
            print("hello a")

    def b(self):
        while(1):
            time.sleep(0.2)
            print(self.val)
            print("hello b")

PC=pseudoclass()
if __name__ == '__main__':
    p = Process(target=PC.a, args=())
    p.start()
    q = Process(target=PC.b, args=())
    q.start()
    p.join()
    q.join()
