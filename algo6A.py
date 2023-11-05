def alg6a (n, k, m, cost):
    dp  = [[100000 for _ in range(n)] for _ in range(m+1)]
    successor = [[-1 for _ in range(n)] for _ in range(m+1)]
    def helper(i, m, current_cost): # return the cost to jump to i
        if m==0 and i>=n:
            return current_cost
        if m==0 or i>=n:
            return 100000
        if dp[m][i] < 100000:
            return dp[m][i]
        min_cost = 100000
        for j in range(1, k+1):
            helper_result = helper(i+j, m-1, current_cost+cost[i])
            if min_cost > helper_result:
                successor[m][i] = i+j
                min_cost = helper_result
        dp[m][i] = min_cost
        return min_cost
    helper(0,m,0)
    string = "0 "
    m_s = m
    i_s = 0
    while m_s > 1:
        index = successor[m_s][i_s]
        string += str(index)
        string += " "
        i_s = index
        m_s = m_s - 1
    print(string)
    # for i in range(1,5):
    #     print(successor[i])

if __name__ == "__main__":
    n, k, m = input().split()
    n, k, m = int(n), int(k)
    cost_str = input().split()
    cost = [int(s) for s in cost_str]

    alg6a(n, k, m, cost)