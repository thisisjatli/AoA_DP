from util import get_trace

def bottom_up(n, k, cost):
    cost_for_m = cost + [0] # dummy cost for n
    pred = [-1 for _ in range(n+1)]
    dp = [100000 for _ in range(n+1)]
    dp[0] = cost_for_m[0]
    for i in range(1, n+1):
        for prev_i in range(i-1, max(-1, i-k-1), -1):
            the_cost = dp[prev_i]+cost_for_m[i]
            if dp[i] > the_cost:
                dp[i] = the_cost
                pred[i] = prev_i
    
    trace = get_trace(pred, n)
    for pf in trace:
        print(pf, end=" ")

if __name__ == "__main__":
    n, k = input().split()
    n, k = int(n), int(k)
    cost_str = input().split()
    cost = [int(s) for s in cost_str]

    bottom_up(n, k, cost)

