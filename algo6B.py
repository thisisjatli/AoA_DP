def alg6b (n, k, m, cost):
#     M = ((n+k) * (m+1)) array
# for each platform p:	   ->O(n)
# 	if p >= n-k:
# 		M[1, p] = cost[p]
# 	else:
# 		M[1, p] = infinity
# for i from n to (n+k-1):  ->O(n)*O(m)
# 	for j from 1 to m:
# 		M[i][j] = infinity
# for j from 2 to m:   ->O(m)*O(n)*O(k)
# for i from n-1 to 0:
# 	minimum = infinity
# 	for l from 1 to k:
# 		minimum = min(minimum, M[i+l, j-1])
# M[i, j] = minimum+ cost[i]
# return M[0, m]
    dp  = [[100000 for _ in range(n+k)] for _ in range(m+1)]
    successor = [[-1 for _ in range(n)] for _ in range(m+1)]
    for i in range(n):
        if(i < n-k):
            dp[1][i] = 100000
        else:
            dp[1][i] = cost[i]
    for j in range(2,m+1):
        for i in range(n-1,-1,-1):
            minimum = 10000
            for l in range(1, k+1):
                if minimum > dp[j-1][i+l]:
                    successor[j][i] = i+l
                    minimum = dp[j-1][i+l]
                
            dp[j][i]=minimum+cost[i]
    # print(dp[m][0])
    # for i in range(1,5):
    #     print(successor[i])
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

if __name__ == "__main__":
    n, k, m = input().split()
    n, k, m = int(n), int(k)
    cost_str = input().split()
    cost = [int(s) for s in cost_str]

    alg6b(n, k, m, cost)