from util import get_trace

# def get_trace(pred, n):
#     id_list = []
#     id = pred[n]
#     while id >= 0:
#         id_list = [id] + id_list
#         id = pred[id]
#     return id_list

def memoization(n, k, cost, dp, pred):
    for prev_id in range(n-1, max(-1, n-k-1), -1):
        if dp[prev_id] == float('inf'):
            memoization(prev_id, k, cost, dp, pred)

        the_cost = dp[prev_id]+cost[n]
        if dp[n] > the_cost:
            dp[n] = the_cost
            pred[n] = prev_id

def bottom_up(n, k, cost):
    cost = cost + [0] # dummy cost for n
    pred = [-1 for _ in range(n+1)]
    dp = [float('inf') for _ in range(n+1)]
    dp[0] = cost[0]
    for i in range(1, n+1):
        for prev_i in range(i-1, max(-1, i-k-1), -1):
            the_cost = dp[prev_i]+cost[i]
            if dp[i] > the_cost:
                dp[i] = the_cost
                pred[i] = prev_i
    
    trace = get_trace(pred, n)
    for pf in trace:
        print(pf, end=" ")

if __name__ == "__main__":
    n = 8
    k = 4
    cost = [12, 5, 8, 9, 11, 13, 16, 1]
    # cost = [12, 5, 7, 9, 7, 6, 16, 1]

    bottom_up(n, k, cost)

    dp = [float('inf') for _ in range(n+1)]
    dp[0] = cost[0]
    pred = [-1 for _ in range(n+1)]
    cost_for_m = cost + [0]
    memoization(n, k, cost_for_m, dp, pred)
    trace = get_trace(pred, n)
    for pf in trace:
        print(pf, end=" ")
