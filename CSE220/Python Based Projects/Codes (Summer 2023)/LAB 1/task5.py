def repetitionCheck(arr):
    for i in range(len(countArray)):
        if countArray[i] > 1:
            for j in range(i+1, len(countArray)):
                if countArray[i] == countArray[j]:
                    print(f"i,{i},j,{j} = "+str(countArray[i])+", "+str(countArray[j]))
                    return True
    return false


salami = [4,3,5,6,6,4,2,7]

max = salami[0]
for i in range(1, len(salami)):
    if salami[i] > max:
        max = salami[i]

countArray = [0]*(max+1)

for note in salami:
    countArray[note] += 1
print(countArray)

print(repetitionCheck(countArray))