from CustomMergeSort import sortTasks

numOfInputs = 4
for i in range(numOfInputs):
    in_file = open(f"input2_{i+1}.txt")
    t, s = [int(num) for num in in_file.readline().split()]
    tasks = []
    for line in in_file:
        tasks.append([int(num) for num in line.split()])
    in_file.close()
    tasks = sortTasks(tasks)

    # ======== Scheduling algorithm =========
    # =============== Start =================
    count = 1
    sQ = [0]*s
    sQ[0] = tasks[0][1]
    for j in range(1, len(tasks)):
        server = -1
        maxTime = -1
        for k in range(len(sQ)):
            if sQ[k] < tasks[j][1]:
                if sQ[k] <= tasks[j][0] and sQ[k] > maxTime:
                    server = k
                    maxTime = sQ[k]
        if server != -1:
            sQ[server] = tasks[j][1]
            count += 1
    # ================ End ==================
    # =======================================

    out_file = open(f"output2_{i+1}.txt", "w")
    out_file.write(str(count))
    out_file.close()
