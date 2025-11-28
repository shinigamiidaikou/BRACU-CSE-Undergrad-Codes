side1 = int(input())
side2 = int(input())

small_side = 0
Large_side = 0
if side1 < side2:
    small_side = side1
    Large_side = side2
else:
    small_side = side2
    Large_side = side1

side3 = int(input())

Larger_side = 0
if side3 <= small_side <= Large_side:
    Larger_side = Large_side
    Large_side = small_side
    small_side = side3
elif small_side <= side3 <= Large_side:
    Larger_side = Large_side
    Large_side = side3
else:
    Larger_side = side3

if small_side + Large_side > Larger_side:
    print("Valid Triangle")
else:
    print("Not a valid triangle")
