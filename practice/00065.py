from numba import jit, cuda
import numpy as np
from timeit import default_timer as timer

# Normal function to run on CPU
def zealot(a):
    for i in range(10000000):
        a[i] += 1

# Function optimized to run on GPU
@jit(target_backend='cuda')
def zealot2(a):
    for i in range(10000000):
        a[i] += 1

if __name__ == "__main__":
    n = 10000000
    protoss_army = np.ones(n, dtype=np.float64)

    start = timer()
    zealot(protoss_army)
    print("Without GPU:", timer() - start)
    t1 = timer() - start

    start = timer()
    zealot2(protoss_army)
    print("With GPU:", timer() - start)
    t2 = timer() - start

    print("Speed boost:", round(t1 / t2, 1) * 100, "%")
