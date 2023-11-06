from util import get_trace

def sol(n, k, cost):
    if n <= 0:
        return cost[0], [0]

    min_cost = 100000
    min_trace = []
    for prev_id in range(n-1, max(-1, n-k-1), -1):
        the_cost, the_trace = sol(prev_id, k, cost)
        the_cost = the_cost + cost[n]
        if min_cost > the_cost:
            min_cost = the_cost
            min_trace = the_trace + [n]
    return min_cost, min_trace

# def top_down(n, k, cost):
#     def func(i, prev_cost):
#         if i >= n:
#             return [prev_cost, []]
#         element = [100000, []]
#         for next_i in range(i+1, i+k+1):
#             next_element = func(next_i, prev_cost+cost[i])
#             if element[0] > next_element[0]:
#                 element = next_element
#         element[1].append(i)
#         return element
    
#     result = func(0, 0)
#     for r in result[1][::-1]:
#         print(r, end=" ")

def algo1(n, k, cost):
    cost = cost + [0]   # dummy cost for after all platforms (sol2)
    min_cost, trace = sol(n, k, cost)
    for pf in trace[:-1]:
        print(pf, end=" ")


if __name__ == "__main__":
    n, k = input().split()
    n, k = int(n), int(k)
    cost_str = input().split()
    cost = [int(s) for s in cost_str]
    
    # sol: the min cost for starting from platform i
    # min_cost = [100000 for _ in range(n+1)]    
    # succ = [-1 for _ in range(n)] # successor of the platform (sol)
    # sol(0, n, k, cost, min_cost, succ)
    # next_pf = succ[0]
    # print(0, end=" ")
    # while next_pf < n:
    #     print(next_pf, end=" ")
    #     next_pf = succ[next_pf]

    algo1(n, k, cost)