from CustomMergeSort import sortTasks

numOfInputs = 3
for i in range(numOfInputs):
    in_file = open(f"input1_{i+1}.txt")
    t = int(in_file.readline())
    tasks = []
    for line in in_file:
        tasks.append([int(num) for num in line.split()])
    in_file.close()

    tasks = sortTasks(tasks)

    # ======== Scheduling algorithm =========
    # =============== Start =================
    outputArr = [tasks[0]]
    occupied = tasks[0][1]
    for j in range(1, len(tasks)):
        if occupied < tasks[j][1]:
            if occupied <= tasks[j][0]:
                occupied = tasks[j][1]
                outputArr.append(tasks[j])
    # ================ End ==================
    # =======================================

    out_file = open(f"output1_{i+1}.txt", "w")
    output = f"{len(outputArr)}\n"+"\n".join([f"{s} {f}" for s, f in outputArr])
    print(f"-----------\n{output}\n-----------")
    out_file.write(output)
    out_file.close()
