from queue import PriorityQueue
from minmaxQueue import MinMaxQueue
def alg5 (n, k, m, cost):
    def helper(i, m, current_cost): # return the cost to jump to i
        if m==0 and i>=n:
            return [current_cost, []]
        if m==0 or i>=n:
            return [100000,[]]
        min_cost = [100000,[]]
        for j in range(1, k+1):
            min_return = helper(i+j, m-1, current_cost+cost[i])
            if min_return[0] < min_cost[0]:
                min_cost = min_return
        min_cost[1].append(i)
        return min_cost
    
    ans = helper(0,m,0)
    string = ""
    for i in range(len(ans[1])-1, -1, -1):
        string += str(ans[1][i])
        string += " "
    print(string)

def alg6a (n, k, m, cost):
    dp  = [[-1 for _ in range(n)] for _ in range(m+1)]
    successor = [[-1 for _ in range(n)] for _ in range(m+1)]
    def helper(i, m): # return the cost to jump to i
        if m==0 and i>=n:
            return 0
        if m==0 or i>=n:
            return 100000
        if dp[m][i] != -1:
            return dp[m][i]
        min_cost = 100000
        for j in range(1, k+1):
            helper_result = helper(i+j, m-1)
            if min_cost > helper_result:
                successor[m][i] = i+j
                min_cost = helper_result
        dp[m][i] = min_cost+cost[i]
        return dp[m][i]

    helper(0,m)
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

def alg7 (n, k, m, cost):
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
        pq = PriorityQueue()
        for i in range(n-1,-1,-1):
            if i != (n-1):
                pq.put((dp[j-1][i+1], (i+1)))
                # print((dp[j-1][i+1], (i+1)))
            if not pq.empty():
                min_ele = pq.get()
                # print(min_ele)
                while min_ele[1] > (i+k):
                    min_ele = pq.get()
                dp[j][i] = min_ele[0]+cost[i]
                successor[j][i] = min_ele[1]
                pq.put(min_ele)
                
            
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