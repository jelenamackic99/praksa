import time

class Time:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self,exc_type, exc_val, exc_tb):
        self.end = time.perf_counter()
        self.elapsed = self.end - self.start
        print(self.elapsed)


with Time():
    for i in range(1000000):
        pass