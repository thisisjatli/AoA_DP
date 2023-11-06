from util import get_trace

def memoization(n, k, cost, dp, pred):
    for prev_id in range(n-1, max(-1, n-k-1), -1):
        if dp[prev_id] >= 100000:
            dp, pred = memoization(prev_id, k, cost, dp, pred)

        the_cost = dp[prev_id]+cost[n]
        if dp[n] > the_cost:
            dp[n] = the_cost
            pred[n] = prev_id

    return dp, pred

def algo2A(n, k, cost):
    dp = [100000 for _ in range(n+1)]
    dp[0] = cost[0]
    pred = [-1 for _ in range(n+1)]
    cost_for_m = cost + [0]
    dp, pred = memoization(n, k, cost_for_m, dp, pred)
    trace = get_trace(pred, n)
    for pf in trace:
        print(pf, end=" ")

if __name__ == "__main__":
    n, k = input().split()
    n, k = int(n), int(k)
    cost_str = input().split()
    cost = [int(s) for s in cost_str]

    algo2A(n, k, cost)
