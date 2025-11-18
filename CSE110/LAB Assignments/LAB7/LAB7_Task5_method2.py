sub_name = input()


def subject_sorter(marks_list):
    for i in range(len(marks_list) - 1):
        maximum = marks_list[i]
        max_index = i
        for j in range(i + 1, len(marks_list)):
            if marks_list[j] > maximum:
                maximum = marks_list[j]
                max_index = j
        temp = marks_list[i]
        marks_list[i] = marks_list[max_index]
        marks_list[max_index] = temp


lst = [["Ashik", 96, 85, 71], ["Turjo", 82, 90, 83], ["Milon", 87, 92, 80], ["Sikder", 98, 94, 90]]

marks_List = list()

if sub_name == "CSE110":
    for i in range(len(lst)):
        marks_List.append(lst[i][1])
elif sub_name == "PHY111":
    for i in range(len(lst)):
        marks_List.append(lst[i][2])
else:
    for i in range(len(lst)):
        marks_List.append(lst[i][3])

subject_sorter(marks_List)

if sub_name == "CSE110":
    for i in range(len(lst)):
        for j in range(len(lst)):
            if marks_List[i] == lst[j][1]:
                print(lst[j][0])
elif sub_name == "PHY111":
    for i in range(len(lst)):
        for j in range(len(lst)):
            if marks_List[i] == lst[j][2]:
                print(lst[j][0])
else:
    for i in range(len(lst)):
        for j in range(len(lst)):
            if marks_List[i] == lst[j][3]:
                print(lst[j][0])
