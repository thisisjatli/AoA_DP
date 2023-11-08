from util import MinMaxQueue, get_trace

def algo4(n, k, cost):
    mq = MinMaxQueue()

    cost_for_m = cost + [0]
    dp = [100000 for _ in range(n+1)]
    dp[0] = cost_for_m[0]
    pred = [-1 for _ in range(n+1)]

    for i in range(1, n+1):
        mq.enque_element((dp[i-1], i-1))
        prev_cost, prev_id = mq.getMin()    # get the min cost in range
        dp[i] = prev_cost + cost_for_m[i]
        pred[i] = prev_id

        if i >= k:
            mq.deque_element()  # remove if out of range

    trace = get_trace(pred, n)
    for pf in trace:
        print(pf, end=" ")

if __name__ == "__main__":
    n, k = input().split()
    n, k = int(n), int(k)
    cost_str = input().split()
    cost = [int(s) for s in cost_str]

    algo4(n, k, cost)