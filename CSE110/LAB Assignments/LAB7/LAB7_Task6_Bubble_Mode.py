my_list = [4, 2, 3, 1, 6, 5]

swap_count = 0
swap_state = False

for i in range(len(my_list) - 1):
    current_swap = my_list[0]
    for j in range(len(my_list) - i - 1):
        if my_list[j] > my_list[j + 1]:
            swap = my_list[j + 1]
            my_list[j + 1] = my_list[j]
            my_list[j] = swap
        if current_swap == my_list[j]:
            current_swap = my_list[j+1]
            if swap_state is True:
                swap_count += 1
                swap_state = False
        else:
            swap_state = True

print("Numbers Swapped :", swap_count)
