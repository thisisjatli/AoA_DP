from queue import PriorityQueue
from util import get_trace

def sol(n, k, cost):
    # counter example: cost = [12, 5, 7, 9, 7, 6, 16, 1]
    # sorting w.r.t cost (excluding platform 0) -> O(nlogn)
    id_order_by_cost = [x for _, x in sorted(zip(cost[1:], list(range(1, n))))]
    kept = [True for i in range(n+1)]   # boolean array, a station is kept or removed
    l_neighbors = [i-1 for i in range(n+1)] # left neighbor of each platform
    r_neighbors = [i+1 for i in range(n+1)] # right neighbor of each platform
    
    # iterate from the platform with largest cost
    for i in range(len(id_order_by_cost)-1, -1, -1):
        id = id_order_by_cost[i]
        if abs(r_neighbors[id]-l_neighbors[id]) <= k:
            kept[id] = False
            l_neighbors[r_neighbors[id]] = l_neighbors[id]
            r_neighbors[l_neighbors[id]] = r_neighbors[id]
    
    final_array = []
    for id, id_kept in enumerate(kept[:-1]):
        if id_kept:
            final_array = final_array + [id]
    return final_array

def heapify(start, pq, loc_in_pq):
    pq_len = len(pq)
    l, r = 2*start+1, 2*start+2
    while l < pq_len:
        if r < pq_len:
            if pq[start][1] > pq[l][1] and pq[start][1] > pq[r][1]:
                if pq[l][1] <= pq[r][1]:
                    loc_in_pq[pq[l][0]] = start
                    loc_in_pq[pq[start][0]] = l
                    pq[l], pq[start] = pq[start], pq[l]
                    start = l
                elif pq[l][1] > pq[r][1]:
                    loc_in_pq[pq[r][0]] = start
                    loc_in_pq[pq[start][0]] = r
                    pq[r], pq[start] = pq[start], pq[r]
                    start = r
        else:
            if pq[start][1] > pq[l][1]:
                loc_in_pq[pq[l][0]] = start
                loc_in_pq[pq[start][0]] = l
                pq[l], pq[start] = pq[start], pq[l]
                start = l
        
        l, r = 2*start+1, 2*start+2

    return pq, loc_in_pq    # return new pq and loc_in_pq

def sol2(n, k, cost):
    loc_in_pq = [-1 for _ in range(n)]
    pq = []
    dp = [float('inf') for _ in range(n+1)]
    pred = [-1 for _ in range(n+1)]
    dp[0] = cost[0]
    for i in range(1, n+1):
        pq = [(i-1, dp[i-1])] + pq
        loc_in_pq[i-1] = 0
        pq, loc_in_pq = heapify(0, pq, loc_in_pq)
        prev_id, prev_cost = pq[0]
        dp[i] = prev_cost + cost[i]
        pred[i] = prev_id
        if len(pq) >= k and i < n:
            removed_loc = loc_in_pq[i-k]
            pq[removed_loc] = (i-k, float('inf'))
            pq, loc_in_pq = heapify(i-k, pq, loc_in_pq)
        print(i, loc_in_pq)

    return pred

def sol3(n, k, cost):
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
    n = 8
    k = 4
    cost = [12, 5, 8, 9, 11, 13, 16, 1]
    # cost = [12, 5, 7, 9, 7, 6, 16, 1]

    sol3(n, k, cost)
