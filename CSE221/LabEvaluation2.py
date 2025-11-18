n = int(input())

adjList = [[] for i in range(n+1)]

for i in range(2, n):
    num = i + i
    while num <= n:
        adjList[num].append(i)
        num += i

for i in range(2, len(adjList)):
    print(f"{i} : {adjList[i]}")

num = int(input())
temp = num
factor = []
while True:
    if len(adjList[temp]) != 0:
        factor.append(adjList[temp][0])
        temp = temp // (adjList[temp][0])
    else:
        factor.append(temp)
        break

print(f"Prime Factorization of {num} = {factor}")

num1, num2 = [int(_) for _ in input().split()]
temp1, temp2 = num1, num2

print(temp1, temp2)
gcd = 1
while True:
    if len(adjList[temp1]) == 0 or len(adjList[temp2]) == 0:
        break
    else:
        i = 0
        j = 0
        while True:
            if adjList[temp1][i] == adjList[temp2][j]:
                factor = adjList[temp1][i]
                gcd *= factor
                temp1 = temp1 // factor
                temp2 = temp2 // factor
                break
            elif adjList[temp1][i] < adjList[temp2][j]:
                i += 1
            else:
                j += 1
            if i == len(adjList[temp1]) or j == len(adjList[temp2]):
                break

print(f"GCD of {temp1}, {temp2} = {gcd}")