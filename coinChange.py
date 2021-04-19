def nonConstructibleChange(coins):
    coins.sort()
    currentChange = 0
    for idx in range(len(coins)):
        coin = coins[idx]
        if coin > currentChange+1:
            return currentChange+1
        currentChange += coin
    return currentChange+1
