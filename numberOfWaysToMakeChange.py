def numberOfWaysToMakeChange(n, denoms):
    ways = [0 for amount in range(n+1)]
    ways[0] = 1
    for i in range(len(denoms)):
        for amount in range(1, len(ways)):
            if denoms[i] <= amount:
                ways[amount] += ways[amount - denoms[i]]
    return ways[n]
