from util import get_trace

def algo2A(n, k, cost):
    dp = [100000 for _ in range(n+1)]
    dp[0] = cost[0]
    pred = [-1 for _ in range(n+1)] # predecessor for each platform
    cost_for_m = cost + [0] # add dummy cost for n
    
    def memoization(i):
        for prev_id in range(max(i-k, 0), i):
            if dp[prev_id] < 100000:    # if initialized
                the_cost = dp[prev_id] + cost_for_m[i]
            else:   # if not, do recursion
                the_cost = memoization(prev_id) + cost_for_m[i]
            if dp[i] > the_cost:
                dp[i] = the_cost    # update with a smaller cost
                pred[i] = prev_id   # update its predecessor
        return dp[i]
    
    memoization(n)
    trace = get_trace(pred, n)
    for pf in trace:
        print(pf, end=" ")

if __name__ == "__main__":
    n, k = input().split()
    n, k = int(n), int(k)
    cost_str = input().split()
    cost = [int(s) for s in cost_str]

    algo2A(n, k, cost)
