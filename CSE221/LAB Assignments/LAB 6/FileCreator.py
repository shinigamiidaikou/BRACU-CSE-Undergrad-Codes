ID = 22101621

p = 1
q = 1
for i in range(p, q+1):
	for j in range(1, 4):
		try:
			file0 = open(f"input{i}_{j}.txt", "x")
		except FileExistsError:
			continue
		file0.close()
	try:
		file1 = open(f"task{i}_{ID}.py", "x")
	except FileExistsError:
		continue
	file1.close()


"""
===============================================
--> input output template code:
===============================================

in_file = open("input1.txt")
t = int(in_file.readline())
numList = [int(_) for _ in in_file.readline().split()]
in_file.close()

output = taskFunction(arr)

out_file = open("output1.txt", "w")
out_file.write(str(output))
out_file.close()

===============================================
--> directory creation template code:
===============================================

import os
os.makedirs("output files/Task 01/part b/", exist_ok=True)
"""
