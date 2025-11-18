summ = 126
value = 0
a = 1
found = False

i1, i2, i3, i4, i5 = [0]*5
while True:
    i1 += 1
    while a*i1 <= a:
        i1 += 1
    while True:
        i2 += 1
        while a*i1*i2 <= a*i1:
            i2 += 1
        while True:
            i3 += 1
            while a*i1*i2*i3 <= a*i1*i2:
                i3 += 1
            while True:
                i4 += 1
                while a*i1*i2*i3*i4 <= a*i1*i2*i3:
                    i4 += 1
                while True:
                    i5 += 1
                    while a*i1*i2*i3*i4*i5 <= a*i1*i2*i3*i4:
                        i5 += 1
                    value = a + a*i1 + a*i1*i2 + a*i1*i2*i3 + a*i1*i2*i3*i4 + a*i1*i2*i3*i4*i5
                    print(f"{a} + {a*i1} + {a*i1*i2} + {a*i1*i2*i3} + {a*i1*i2*i3*i4} + {a*i1*i2*i3*i4*i5} = {value}")
                    if value >= summ:
                        break
                if value >= summ:
                    break
            if value >= summ:
                break
        if value >= summ:
            break
    if value >= summ:
        if value > summ:
            a += 1
            i1, i2, i3, i4, i5 = [0]*5
        else:
            break


print("Final Answer:")
print("-"*30)
print(f"{a} + {a*i1} + {a*i1*i2} + {a*i1*i2*i3} + {a*i1*i2*i3*i4} + {a*i1*i2*i3*i4*i5} = {summ}")
print("-"*30)
