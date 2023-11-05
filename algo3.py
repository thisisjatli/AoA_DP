from queue import PriorityQueue
from util import get_trace

def sol(n, k, cost):
    cost = cost + [0]
    pq = PriorityQueue()
    dp = [float('inf') for _ in range(n+1)]
    dp[0] = cost[0]
    pred = [-1 for _ in range(n+1)]
    for i in range(1, n+1):
        pq.put((dp[i-1], i-1))
        prev_cost, prev_id = pq.get()
        while prev_id < i-k and not pq.empty():
            prev_cost, prev_id = pq.get()
        dp[i] = prev_cost+cost[i]
        pred[i] = prev_id
        if prev_id >= i-k+1:
            pq.put((dp[prev_id], prev_id))

    trace = get_trace(pred, n)
    for pf in trace:
        print(pf, end=" ")


if __name__ == "__main__":
    n, k = input().split()
    n, k = int(n), int(k)
    cost_str = input().split()
    cost = [int(s) for s in cost_str]

    sol(n, k, cost)
