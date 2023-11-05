from minmaxQueue import MinMaxQueue
def alg8 (n, k, m, cost):
# M = ((n) * (m+1)) array
# for each platform p:
# 	if p >= n-k:
# 		M[1, p] = cost[p]
# 	else:
# 		M[1, p] = infinity
# for j from 2 to m:
# 	pq = priorityQueue<min_value, index>
# for i from n-1 to 0:
# 	minimum = infinity
# 	if i != (n-1):
# 		pq.put(M[i+1, m-1], i+1) 	->O(logn)
# 	if not pq.isEmpty():
# 		min_value, index = pq.peek()
# 		while index > (i+k):	   ->This while-loop with for-loop will repeat at most n times
# 			pq.pop()
# 			min_value, index = pq.peek()
# 		minimum= cost[i] + min_value
# 	M[i, j] = minimum
# return M[0, m]

    dp  = [[100000 for _ in range(n)] for _ in range(m+1)]
    successor = [[-1 for _ in range(n)] for _ in range(m+1)]
    for i in range(n):
        if(i < n-k):
            dp[1][i] = 100000
        else:
            dp[1][i] = cost[i]
    for j in range(2,m+1):
        mq = MinMaxQueue()
        for i in range(n-1,-1,-1):
            if i != (n-1):
                mq.enque_element((dp[j-1][i+1], (i+1)))
                # print((dp[j-1][i+1], (i+1)))
            if not mq.isEmpty():
                min_ele = mq.getMin()
                dp[j][i] = min_ele[0]+cost[i]
                successor[j][i] = min_ele[1]
                if i < n-k:
                    mq.deque_element() 
                
            
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
    n, k, m = int(n), int(k), int(m)
    cost_str = input().split()
    cost = [int(s) for s in cost_str]

    alg8(n, k, m, cost)