Limit = int(input())

for column_counter in range(1, Limit + 1):
    print(column_counter, end="")
for column_counter in range(Limit-1, 0, -1):
    print(column_counter, end="")