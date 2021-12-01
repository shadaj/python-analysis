def coinChange(coins, value):
    W = []
    j = 0
    while j < value+1:
        W.append(-1)
        j += 1
    W[0] = 0
    i = 1
    while i <= value:
        curMin = -1
        j = 0
        while j < len(coins):
            curValue = coins[j]
            if i - curValue >= 0:
                if curMin == -1 or W[i-curValue] + 1 < curMin:
                    curMin = W[i-curValue] + 1
            j += 1
        W[i] = curMin
        i+=1
    return W[value]
