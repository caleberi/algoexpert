def minNumberOfCoinsForChange(n, denoms):
    numberOfCoins = [float("inf") for amount in range(n+1)]
    numberOfCoins[0] = 0
    for denom in denoms:
        for amount in range(1, len(numberOfCoins)):
            if denom <= amount:
                numberOfCoins[amount] = min(numberOfCoins[amount-denom]+1, numberOfCoins[amount])
    return -1 if numberOfCoins[n] == float("inf") else numberOfCoins[n]
