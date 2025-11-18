####### Top-Down Approach #######
def coinChange(idx, val, coins, cList):
    if val < 0:
        return float('inf')
    if idx == 0 and val >= 0:
        if val == 0:
            return 0
        return float('inf')
    val1 = coinChange(idx-1, val, coins, cList)
    val2 = 1 + coinChange(idx, val-coins[idx-1], coins, cList)
    return min(val1, val2)


inputs = 2
for i in range(inputs):
    in_file = open(f"input3_{i+1}.txt")
    n, x = [int(num) for num in in_file.readline().split()]
    coins = [int(num) for num in in_file.readline().split()]
    in_file.close()
    changeList = [[0]*(x+1) for _ in range(n+1)]
    output = coinChange(n, x, coins, changeList)
    with open(f"output3_{i+1}.txt", "w") as out_file:
    	out_file.write(str(output))
