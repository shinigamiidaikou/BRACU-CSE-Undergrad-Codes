amount = int(input("Please enter total amount: "))
note_list = [500, 100, 50, 20, 10, 5, 2, 1]

for note in note_list:
    if amount // note != 0:
        note_quantity = amount // note
        if amount - (note_quantity * note) == 0:
            amount = 0
        else:
            amount -= note_quantity * note
        print("{} Taka: {} note(s)".format(note, note_quantity))
