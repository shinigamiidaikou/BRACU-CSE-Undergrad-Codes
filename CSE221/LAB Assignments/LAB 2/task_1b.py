def order_of_n_finder(numList, s):
    idxDict = {f"{numList[0]}":[0]}
    i = 1
    while i < len(numList):
        if str(s - numList[i]) in idxDict.keys():
            j = idxDict[str(s - numList[i])][0]
            if i < j:
                return f"{i + 1} {j + 1}"
            else:
                return f"{j + 1} {i + 1}"
        else:
            if str(numList[i]) not in idxDict.keys():
                idxDict[f"{numList[i]}"] = [i]
            else:
                idxDict[f"{numList[i]}"].append(i)
        i += 1
    return "IMPOSSIBLE"


def order_of_nLogN_finder(numList, s):
    sortedList = sorted(numList)
    i, j = 0, len(numList) - 1
    while i < j:
        if sortedList[i] + sortedList[j] == s:
            i = numList.index(sortedList[i])
            j = numList.index(sortedList[j])
            if i < j:
                return f"{i + 1} {j + 1}"
            else:
                return f"{j + 1} {i + 1}"
        elif sortedList[i] + sortedList[j] < s:
            i += 1
        else:
            j -= 1
    return "IMPOSSIBLE"


def summableFinder(numList, s, order="nLogN"):
    if order == "n":
        return order_of_n_finder(numList, s)
    else:
        return order_of_nLogN_finder(numList, s)


in_file = open("input1.txt")
n, s = [int(x) for x in in_file.readline().split()]
numList = [int(x) for x in in_file.readline().split()]
in_file.close()

out_file = open("output1.txt", "w")
out_file.write(summableFinder(numList, s, "n"))
out_file.close()
