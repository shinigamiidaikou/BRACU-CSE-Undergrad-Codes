my_list = [4, 2, 3, 1, 6, 5]
swap_count = 0

for i in range(len(my_list) - 1):
    min_idx = i
    pos_swap = 0
    for j in range(i + 1, len(my_list)):
        if my_list[j] < my_list[min_idx]:
            min_idx = j
            pos_swap += 1
    if pos_swap > 0:
        swap_count += 2
        pos_swap = 0
    temp = my_list[i]
    my_list[i] = my_list[min_idx]
    my_list[min_idx] = temp

print(swap_count)
