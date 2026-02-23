import numpy as np
import time

from quicksort import quick_sort
from heapsort import heap_sort
from mergesort import merge_sort

def main():
    np.random.seed(42)
    N = 1000000
    datasets = []
    mi = 0
    ma = 1000000000

    datasets.append(np.sort(np.random.randint(mi, ma, size=N, dtype=np.int32)))
    datasets.append(np.sort(np.random.uniform(mi, ma, size=N))[::-1])
    for i in range(4): datasets.append(np.random.randint(mi, ma, size=N, dtype=np.int32))
    for i in range(4): datasets.append(np.random.uniform(mi, ma, size=N))

    algo = {
        "QuickSort": lambda x: quick_sort(x.tolist()),
        "HeapSort": lambda x: heap_sort(x.tolist()),
        "MergeSort": lambda x: merge_sort(x.tolist()),
        "sort (numpy)": lambda x: np.sort(x)
    }

    for i, data in enumerate(datasets):
        print(f"Dãy {i+1}:")

        for alg_name, alg_func in algo.items():
            data_copy = data.copy()
            t1 = time.perf_counter()
            alg_func(data_copy)
            t2 = time.perf_counter()

            print(f"{alg_name}: {(t2 - t1)*1000}ms")

if __name__ == "__main__":
    main()