def even_odd(sentence):
    even_string = "02468"
    even_present = False

    for i in even_string:
        if i in sentence:
            even_present = True
            break

    if even_present == True:
        numList = list()
        for char in sentence:
            if char in even_string:
                numList.append(int(char))
        return numList
    else:
        evenList = list()
        for i in range(1, len(sentence)):
            if i % 2 == 0:
                evenList.append(i)
        even_tuple = tuple(evenList)
        return even_tuple

print(even_odd("This is not 2021"))