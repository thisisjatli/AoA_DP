from util import MinQueue, get_trace

def sol(n, k, cost):
    mq = MinQueue()

    cost = cost + [0]
    dp = [float('inf') for _ in range(n+1)]
    dp[0] = cost[0]
    pred = [-1 for _ in range(n+1)]

    for i in range(1, n+1):
        mq.enque_element(dp[i-1], i-1)
        prev_cost, prev_id = mq.getMin()
        dp[i] = prev_cost + cost[i]
        pred[i] = prev_id

        if i >= k:
            mq.deque_element()

    trace = get_trace(pred, n)
    for pf in trace:
        print(pf, end=" ")


if __name__ == "__main__":
    n = 8
    k = 4
    cost = [12, 5, 8, 9, 11, 13, 16, 1]
    # cost = [12, 5, 7, 9, 7, 6, 16, 1]

    sol(n, k, cost)