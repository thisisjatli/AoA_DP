def sol(start, n, k, cost, min_cost, min_route):
    if start >= n:  # pass the goal, do nothing
        # return (0, [])
        return
    for d in range(k, 0, -1):   # look for next possible k stations
        # ans = sol(start+d, n, k, cost, min_cost, min_route)
        next_id = start + d
        sol(next_id, n, k, cost, min_cost, min_route)   # recursion
        # the_cost = ans[0] + cost[start]
        # possible min cost if that's the next station
        the_cost = min_cost[next_id] + cost[start] if next_id < n else cost[start]
        if min_cost[start] > the_cost:  # update it it's a new min cost found
            min_cost[start] = the_cost
            # update route as well
            min_route[start] = [start] + min_route[next_id] if next_id < n else [start]
    # return (min_cost[start], min_route[start])
    return

if __name__ == "__main__":
    n = 8
    k = 4
    cost = [12, 5, 8, 9, 11, 13, 16, 1]
    min_cost = [float('inf') for _ in range(n)] # the min cost from station i to the end
    min_route = [[] for _ in range(n)]  # min route if starting from station i

    sol(0, n, k, cost, min_cost, min_route)
    print(min_route[0], min_cost[0])