from queue import PriorityQueue
from util import get_trace

def algo3(n, k, cost):
    cost_for_m = cost + [0]
    pq = PriorityQueue()
    dp = [100000 for _ in range(n+1)]
    dp[0] = cost_for_m[0]   # the cost for reaching platform 0 is its own cost
    pred = [-1 for _ in range(n+1)]
    for i in range(1, n+1):
        pq.put((dp[i-1], i-1))  # previous platform is considered
        prev_cost, prev_id = pq.get()
        while prev_id < i-k and not pq.empty(): # platform must be within jump range
            prev_cost, prev_id = pq.get()       # remove if out of range
        dp[i] = prev_cost+cost_for_m[i]         # the first in pq is the min cost
        pred[i] = prev_id
        if prev_id >= i-k+1:
            pq.put((dp[prev_id], prev_id))      # if it's still in jump range for the next platform

    trace = get_trace(pred, n)
    for pf in trace:
        print(pf, end=" ")

if __name__ == "__main__":
    n, k = input().split()
    n, k = int(n), int(k)
    cost_str = input().split()
    cost = [int(s) for s in cost_str]

    algo3(n, k, cost)
