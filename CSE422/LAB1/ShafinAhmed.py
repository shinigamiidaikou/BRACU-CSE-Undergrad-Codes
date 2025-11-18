import heapq

Graph = dict()
infile = open("input_file.txt")
for line in infile:
    line = line.split()
    Graph[line[0]] = [int(line[1])] + [(line[i], int(line[i+1])) for i in range(2,len(line),2)]
infile.close()

# for key, value in Graph.items():
#     print(key, ":", value)

start = input("Start node: ")
dest = input("Destination: ")

# start = "Arad"
# dest = "Bucharest"

parent = {(Graph[start][0], start): None}
Q = [(Graph[start][0], start)]
heapq.heapify(Q)
found = False
while len(Q) != 0:
    item = heapq.heappop(Q)
    f_cn, cn = item
    if cn == dest:
        lastItem = item
        found = True
        break
    for v in Graph[cn][1:]:
        n = v[0]
        h_n = Graph[n][0]
        g_n = f_cn - Graph[cn][0] + v[1]
        f_n = h_n + g_n
        heapq.heappush(Q, (f_n, n))
        parent[(f_n, n)] = item

def printPath(item):
    if item == None:
        return
    printPath(parent[item])
    if item == lastItem:
        print(item[1])
    else:
        print(item[1], "->", end=" ")

if found:
    print("Path: ", end="")
    printPath(lastItem)
    print("Total Distance:", lastItem[0], "km")
else:
    print("NO PATH FOUND")