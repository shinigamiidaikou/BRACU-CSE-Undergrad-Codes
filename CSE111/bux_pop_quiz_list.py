
print(
    'wow! great! stunning!'.count('!'),
    'wow! great! stunning!'.count('!', 10, 20),
    'wow! great! stunning!'.count('!', 10)
)

lst = ['Ronaldo','Messi', 'Rivaldo', 'Hazard']
val = min(lst[::2] + ['Ronaldinho'])
print(val)

lst1 = [2,4,6,8,10,12,14,16]
print(lst1)
print(lst1[::1][7::-1])
print(lst1[7:0:-1])
print(lst1[-1:-len(lst1)-1:-1])

lst2 = [2,4,6,8,10]
lst2_comp = [sum(lst2[0:i+1]) for i in range(len(lst2))]
print(lst2_comp)
