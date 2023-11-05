from util import get_trace

# dynamic start point
def sol(start, n, k, cost, min_cost, succ):
    if start >= n:  # pass the goal, do nothing
        return
    for d in range(k, 0, -1):   # look for next possible k stations
        next_id = start + d
        sol(next_id, n, k, cost, min_cost, succ)   # recursion

        # possible min cost if that's the next platform
        the_cost = min_cost[next_id] + cost[start] if next_id < n else cost[start]
        if min_cost[start] > the_cost:  # update it it's a new min cost found
            min_cost[start] = the_cost

            # update successor as well
            succ[start] = min(n, next_id)
    return

# dynamic end point
def sol2(n, k, cost, min_cost, pred):
    if n <= 0:
        return
    for prev_id in range(n-1, max(-1, n-k-1), -1):
        sol2(prev_id, k, cost, min_cost, pred)
        the_cost = min_cost[prev_id] + cost[n]
        if min_cost[n] > the_cost:
            min_cost[n] = the_cost
            pred[n] = prev_id
    return

if __name__ == "__main__":
    n, k = input().split()
    n, k = int(n), int(k)
    cost_str = input().split()
    cost = [int(s) for s in cost_str]
    
    # sol: the min cost for starting from platform i
    # min_cost = [float('inf') for _ in range(n+1)]    
    # succ = [-1 for _ in range(n)] # successor of the platform (sol)
    # sol(0, n, k, cost, min_cost, succ)
    # next_pf = succ[0]
    # print(0, end=" ")
    # while next_pf < n:
    #     print(next_pf, end=" ")
    #     next_pf = succ[next_pf]
    
    # print("")

    # sol2: the min cost for reaching platform i
    cost = cost + [0]   # dummy cost for after all platforms (sol2)
    min_cost = [float('inf') for _ in range(n+1)]
    min_cost[0] = cost[0]
    pred = [-1 for _ in range(n+1)] # predecessor of the platform (sol2)
    sol2(n, k, cost, min_cost, pred)
    trace = get_trace(pred, n)
    for pf in trace:
        print(pf, end=" ")