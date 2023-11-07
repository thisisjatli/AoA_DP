import numpy as np
import time
from multiprocessing import Pool
import json

import sys
sys.setrecursionlimit(100000)

from algo1 import algo1, top_down
from algo2A import algo2A, algo2A_v2
from algo2B import bottom_up
from algo3 import algo3
from algo4 import algo4
from algorithm import alg5, alg6a, alg6b, alg7, alg8

def generate_input(n, cost):
    # k < n
    # ceil(n/k) <= m <= n
    added_len = abs(n-len(cost))
    rd_cost = np.random.randint(0, 30, size=added_len, dtype='int')
    # k = random.randint(1, min(n+1, 5))
    # m = random.randint(math.ceil(n/k), min(math.ceil(n/k)+5, n))
    # print('n:', n)
    # print('k:', k)
    # print('m:', m)
    # print('Cost:', cost)
    cost = cost + [int(rd_cost[i]) for i in range(rd_cost.size)]   # in order to store in json file
    return cost

def runtime_test(n, k, m, cost, algo='1'):
    start_time = time.time()
    match algo:
        case '1':
            algo1(n, k, cost)
            print("\nalgo1 done")
        case '2A':
            algo2A_v2(n, k, cost)
            print("\nalgo2A done")
        case '2A_v2':
            algo2A_v2(n, k, cost)
            print("\nalgo2A_v2 done")
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

# def runtime_test_v2(n, k, m, cost):
#     runtime_results = {}

#     start_time = time.time()
#     algo1(n, k, cost)
#     print("\nalgo1 done")
#     runtime_results['1'] = time.time() - start_time
    
#     start_time = time.time()
#     algo2A(n, k, cost)
#     print("\nalgo2A done")
#     runtime_results['2A'] = time.time() - start_time
    
#     start_time = time.time()
#     bottom_up(n, k, cost)
#     print("\nalgo2B done")
#     runtime_results['2B'] = time.time() - start_time
    
#     start_time = time.time()
#     algo3(n, k, cost)
#     print("\nalgo3 done")
#     runtime_results['3'] = time.time() - start_time
    
#     start_time = time.time()
#     algo4(n, k, cost)
#     print("\nalgo4 done")
#     runtime_results['4'] = time.time() - start_time
    
#     start_time = time.time()
#     alg5(n, k, m, cost)
#     print("algo5 done")
#     runtime_results['5'] = time.time() - start_time
    
#     start_time = time.time()
#     alg6a(n, k, m, cost)
#     print("algo6A done")
#     runtime_results['6A'] = time.time() - start_time
    
#     start_time = time.time()
#     alg6b(n, k, m, cost)
#     print("algo6B done")
#     runtime_results['6B'] = time.time() - start_time
    
#     start_time = time.time()
#     alg7(n, k, m, cost)
#     print("algo7 done")
#     runtime_results['7'] = time.time() - start_time
    
#     start_time = time.time()
#     alg8(n, k, m, cost)
#     print("algo8 done")
#     runtime_results['8'] = time.time() - start_time
    
#     return runtime_results

def experiment_v1(n, k, m, cost, algo_list):
    # algo_list = ['1', '2A', '2B', '3', '4', '5', '6A', '6B', '7', '8']
    with Pool() as pool:
        async_results = [pool.apply_async(runtime_test, (n, k, m, cost, algo,)) for algo in algo_list]
        results = [ar.get() for ar in async_results]
    pool.close()
    pool.join()
    print(results)
    return results

# def experiment_v2(n):
#     cost, k, m = generate_input(n)
#     results = runtime_test_v2(n, k, m, list(cost))
#     print(results)

if __name__ == "__main__":
    # n_list = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 99999]
    # n_list = [100, 500, 1000, 5000, 10000, 20000, 30000, 40000]
    # n_list = [100, 500, 1000, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000]
    n_list = [100, 500, 1000, 2000, 3000, 4000, 5000]
    # n_list = [10000, 20000, 30000, 40000]
    # n_list = [10, 15, 20, 25, 30, 35]    # for brute-force, the size limit is around 60
    # n_list = [20, 30, 40, 50, 60]
    # k, m = 80, 60
    k, m = 100, 60
    # k, m = 1000, 50
    # k, m = 5, 8
    # k, m = 500, 200 # experimental purpose
    # algo_list = ['2A', '2B', '3', '4', '6A', '6B', '7', '8']
    # algo_list = ['2A', '2B', '3', '4']
    algo_list = ['6A', '6B', '7', '8']
    # algo_list = ['2A', '2B']

    stats = {n: {} for n in n_list}
    cost = []

    for n in n_list:
        cost = generate_input(n, cost)
        # stats[n]["cost"] = cost
        print("n:", n)
        # print("Cost:", cost)
        results = experiment_v1(n, k, m, cost, algo_list)
        stats[n]["runtime"] = {algo: r for algo, r in zip(algo_list, results)}

    json_object = json.dumps(stats, indent=4)
    with open('experimental_results/p2_without_bf_small.json', 'w') as fw:
        fw.write(json_object)
        