import math

points = [(5, 3), (2, 9), (-2, 7), (-3, -4), (0, 6), (7, -2)]
d_list = list()

for co_ord in points:
    x, y = co_ord
    dist_val = math.sqrt((x ** 2) + (y ** 2))
    d_list.append(dist_val)

for i in range(len(d_list) - 1):
    for j in range(len(d_list) - i - 1):
        if d_list[j] < d_list[j + 1]:
            tmp = d_list[j + 1]
            d_list[j + 1] = d_list[j]
            d_list[j] = tmp

for co_ord in points:
    x, y = co_ord
    dist_val = math.sqrt((x ** 2) + (y ** 2))
    if dist_val == d_list[-1]:
        print("Minimum distance =", d_list[-1])
        print("Here the closest point is {} which has a distance of {} from the origin.".format(co_ord, d_list[-1]))
