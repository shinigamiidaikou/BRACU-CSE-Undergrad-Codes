file = open('goal stats.txt') 

players_dict = {}
for line in file:
	temp = line.split('|')
	name = temp[0]
	goal = int(temp[-1].strip())
	players_dict[goal] = name 
goal_list = sorted(players_dict, reverse=True) 

print(goal_list)

sorted_dict = { } 
for goal in goal_list:
	name = players_dict[goal]
	sorted_dict[name] = goal

new_file = open('best player list.txt', 'w') 
for name, goal in sorted_dict.items():
	new_file.write(name+'    '+str(goal)+"\n")

new_file.close() 