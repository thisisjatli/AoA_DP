import numpy as np
import time
from multiprocessing import Pool
import json

import sys
sys.setrecursionlimit(100000)

from algo1 import algo1
from algo2A import algo2A
from algo2B import bottom_up
from algo3 import algo3
from algo4 import algo4
from algorithm import alg5, alg6a, alg6b, alg7, alg8

def generate_input(n, cost):
    added_len = abs(n-len(cost))
    rd_cost = np.random.randint(0, 30, size=added_len, dtype='int')
    cost = cost + [int(rd_cost[i]) for i in range(rd_cost.size)]   # in order to store in json file
    return cost

def runtime_test(n, k, m, cost, algo='1'):
    start_time = time.time()
    match algo:
        case '1':
            algo1(n, k, cost)
            print("\nalgo1 done")
        case '2A':
            algo2A(n, k, cost)
            print("\nalgo2A done")
        case '2B':
            bottom_up(n, k, cost)
            print("\nalgo2B done")
        case '3':
            algo3(n, k, cost)
            print("\nalgo3 done")
        case '4':
            algo4(n, k, cost)
            print("\nalgo4 done")
        case '5':
            alg5(n, k, m, cost)
            print("algo5 done")
        case '6A':
            alg6a(n, k, m, cost)
            print("algo6A done")
        case '6B':
            alg6b(n, k, m, cost)
            print("algo6B done")
        case '7':
            alg7(n, k, m, cost)
            print("algo7 done")
        case '8':
            alg8(n, k, m, cost)
            print("algo8 done")
    total_time = time.time() - start_time
    return total_time

def experiment_v1(n, k, m, cost, algo_list):
    with Pool() as pool:
        async_results = [pool.apply_async(runtime_test, (n, k, m, cost, algo,)) for algo in algo_list]
        results = [ar.get() for ar in async_results]
    pool.close()
    pool.join()
    print(results)
    return results

if __name__ == "__main__":
    n_list = [100, 500, 1000, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000]
    k, m = 100, 60
    algo_list = ['1', '2A', '2B', '3', '4', '5', '6A', '6B', '7', '8']

    stats = {n: {} for n in n_list}
    cost = []

    for n in n_list:
        cost = generate_input(n, cost)
        print("n:", n)
        results = experiment_v1(n, k, m, cost, algo_list)
        stats[n]["runtime"] = {algo: r for algo, r in zip(algo_list, results)}

    json_object = json.dumps(stats, indent=4)
    with open('experimental_results/p2_without_bf_small.json', 'w') as fw:
        fw.write(json_object)
        