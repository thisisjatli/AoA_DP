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

if __name__ == "__main__":
    n, k, m = input().split()
    n, k, m = int(n), int(k)
    cost_str = input().split()
    cost = [int(s) for s in cost_str]

    alg5(n, k, m, cost)