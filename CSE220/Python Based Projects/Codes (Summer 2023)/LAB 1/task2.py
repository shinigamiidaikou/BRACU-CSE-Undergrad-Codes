def removeElement(arr, size, idx):
    if idx == size - 1:
        arr[idx] = 0
    else:
        i = idx
        while i < size:
            if arr[i+1] == None:
                break
            arr[i] = arr[i+1]
            i += 1
        arr[i] = None


def discardCards(cards,num):
    size = 0
    while size < len(cards):
        if cards[size] == None:
            break
        size += 1
    i = 0
    while i < size:
        if cards[i] == num:
            removeElement(cards, size ,i)
            size -= 1
            continue
        i += 1
    return cards


cards=[10,2,30,2,50,2,2,None,None]
#Function Call:
print(discardCards(cards,2))