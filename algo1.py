def algo1(n, k, cost):
    def func(i, prev_cost):
        if i >= n:
            # list of two elements
            # first is the current cost for next platform
            # second is the path it took
            return [prev_cost, []]
        element = [100000, []]
        for next_i in range(i+1, i+k+1):
            # before passing to the next platform, current cost must add cost of platform i
            next_element = func(next_i, prev_cost+cost[i])
            if element[0] > next_element[0]:
                element = next_element
        # add platform i to the path
        element[1] = [i] + element[1]
        return element
    
    result = func(0, 0)
    for r in result[1]:
        print(r, end=" ")

if __name__ == "__main__":
    n, k = input().split()
    n, k = int(n), int(k)
    cost_str = input().split()
    cost = [int(s) for s in cost_str]

    algo1(n, k, cost)
