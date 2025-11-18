####### Bottom-Up Approach #######
def stairPathCount(n, nList, k=0):
    if k >= n:
        if k > n:
            return 0
        return 1
    
    def getPathVal(p):
        if p >= len(nList):
            return 0
        if nList[p] == -1:
            val = stairPathCount(n, nList, p)
            nList[p] = val
            return val
        return nList[p]
    
    val1 = getPathVal(k+1)
    if val1 == 0:
        return 0
    val2 = getPathVal(k+2)
    if val2 == 0:
        return val1
    return val1 + val2


inputs = 4
for i in range(inputs):
    with open(f"input2_{i+1}.txt") as in_file:
        n = int(in_file.readline())
    total = stairPathCount(n, [-1]*(n+1))
    with open(f"output2_{i+1}.txt", "w") as out_file:
    	out_file.write(str(total))
