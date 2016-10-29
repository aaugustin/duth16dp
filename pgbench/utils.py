from contextlib import contextmanager
from time import perf_counter

@contextmanager
def benchmark():
    t0 = perf_counter()
    try:
        yield
    finally:
        t1 = perf_counter()
        print('{:3f}s'.format(t1 - t0))
