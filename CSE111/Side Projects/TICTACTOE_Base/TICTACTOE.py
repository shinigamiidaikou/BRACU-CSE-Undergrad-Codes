import os
from time import sleep

def clear():
	if os.name == "nt":
		os.system('cls')
	else:
		os.system('clear')


def main_menu():
    long_ebar = "=============================="
    long_mbar = "----------------------------"
    l_space = "                            "
    s_space = "       "
    
    view_game_name = long_ebar + '\n|--------TICTACTOE !!!-------|\n|' + long_mbar + "|"
    view_options = "|" + l_space + '|\n|' + l_space + '\n|' + s_space + '1. Start Game' + s_space + '|\n|' + s_space + '2. Exit' + s_space + '       |\n|' + l_space + '|\n|' + l_space + '|\n' + long_mbar
    print(view_game_name)
    print(view_options)

    global game_start
    global counter
    while True:
        try:
            selection = int(input("Select (1/2): "))
        except EOFError:
            game_start = False
            counter = 9
            clear()
            break
        else:
            if selection == 1:
                game_start = True
                counter = 0
                clear()
                break
            elif selection == 2:
                game_start = False
                counter = 9
                clear()
                break
            else:
                clear()
                print(view_game_name)
                print(view_options)


def first_grid_layout():
	
	print("\n ___ ___ ___      Positions:\n|   |   |   |     1 | 2 | 3\n ___ ___ ___      __ ___ __\n|   |   |   |     4 | 5 | 6\n ___ ___ ___      __ ___ __\n|   |   |   |     7 | 8 | 9\n ___ ___ ___\n")


def name_selection():
	
	global player1_name
	global player2_name
	global force_exit
	
	print("ATTENTION: Player1 will make first move.")
	try:
		player1_name = input("\nEnter Player1 name: ")
		player2_name = input("Enter Player2 name: ")
	except EOFError:
		force_exit = False


def shape_selection():
	global player1_shape
	global player2_shape
	global force_exit
	
	try:
		shape_selection = input(f"\n{player1_name}, which shape do you choose: ")
	except EOFError:
		force_exit = False
	else:
		if 97 <= ord(shape_selection) <= 122:
			player1_shape = chr(ord(shape_selection)-32)
		else:
			player1_shape = shape_selection

		if player1_shape == "O":
			player2_shape = "X"
			print(f"\n{player1_name}'s chosen shape:", player1_shape)
			print(f"{player2_name}'s chosen shape:", player2_shape, "\n")
		else:
			player2_shape = "O"
			print(f"\n{player1_name}'s chosen shape:", player1_shape)
			print(f"{player2_name}'s chosen shape:", player2_shape, "\n")
		sleep(2)
		clear()


def player_move_printing(player_input, player_shape):
	
	clear()
	global counter
	position_in_use = False

	count = 1
	increament = 0
	print("\n ___ ___ ___      Positions:")
	for i in range(3):
		print("|", end="")
		for j in range(3):
			if count == player_input and count == box_pos[i][j]:
				box_pos[i][j] = player_shape
				print(f" {box_pos[i][j]} |", end="")
			elif count == player_input and count != box_pos[i][j]:
				print(f" {box_pos[i][j]} |", end="")
				position_in_use = True
			else:
				if box_pos[i][j] == count:
					print(f"   |", end="")
				else:
					print(f" {box_pos[i][j]} |", end="")
			if j == 2:
				print(f"     {increament+1} | {increament+2} | {increament+3}")
			count += 1
		increament += 3
		if i != 2:
			print(" ___ ___ ___      __ ___ __")
	if position_in_use is True:
		print(" ___ ___ ___\n")
		print("ATTENTION: Position already in use. Please select another one !!")
	else:
		print(" ___ ___ ___\n")
		counter += 1


def match_checking(player_name, player_input, player_shape):

	global counter
	global game_restart
	matched = False
	coordinates = co_ords[player_input]
	for i in range(len(coordinates)):
		if box_pos[coordinates[i][0][0]][coordinates[i][0][1]] == player_shape and box_pos[coordinates[i][1][0]][coordinates[i][1][1]] == player_shape:
			matched = True
			break
	if matched is True:
		print(f"\n{player_name} Wins !!!\nCongratulations!!!")
		restart = input("\n\nRestart Game? Y/N: ")
		if restart in "Yy" or restart == "yes" or restart == "Yes":
			game_restart = True
			counter = 0
			clear()
		else:
			clear()
			main_menu()
	elif counter == 9 and matched is False:
		print("\nThe Game Ends with a Draw !!!!")
		restart = input("Restart? Y/N: ")
		if restart in "Yy" or restart == "yes" or restart == "Yes":
			game_restart = True
			counter = 0
			clear()
		else:
			clear()
			main_menu()


box_pos = [[1,2,3],[4,5,6],[7,8,9]]
co_ords = {
	1: (
		((0,1),(0,2)),
		((1,1),(2,2)),
		((1,0),(2,0))
		),# check for input: 1
	2: (
		((0,0),(0,2)),
		((1,1),(2,1))
		),# check for input: 2
	3: (
		((0,0),(0,1)),
		((1,1),(2,0)),
		((1,2),(2,2))
		),# check for input: 3
	4: (
		((0,0),(2,0)),
		((1,1),(1,2))
		),# check for input: 4
	5: (
		((1,0),(1,2)),
		((0,1),(2,1)),
		((0,0),(2,2)),
		((0,2),(2,0))
		),# check for input: 5
	6: (
		((0,2),(2,2)),
		((1,0),(1,1))
		),# check for input: 6
	7: (
		((0,0),(1,0)),
		((0,2),(1,1)),
		((2,1),(2,2))
		),# check for input: 7
	8: (
		((2,0),(2,2)),
		((0,1),(1,1))
		),# check for input: 8
	9: (
		((0,2),(1,2)),
		((0,0),(1,1)),
		((2,0),(2,1))
		) # check for input: 9
}

game_start = False
game_restart = False
force_exit = True
counter = 0
player1_name = str()
player2_name = str()
player1_shape = str()
player2_shape = str()
clear()
main_menu()

while counter < 9:

	if counter == 0 and game_restart is True:
		box_pos = [[1,2,3],[4,5,6],[7,8,9]]
		change_players = input("Restart with diffrent players? (Y/N):")
		if change_players in "Yy" or change_players == "yes" or change_players == "Yes":
				name_selection()
		if force_exit is True:
			shape_selection()
			if force_exit is True:
				first_grid_layout()
			else:
				clear()
				break
		else:
			clear()
			break
	elif counter == 0 and game_start is True:
		box_pos = [[1,2,3],[4,5,6],[7,8,9]]
		name_selection()
		if force_exit is False:
			shape_selection()
			if force_exit is False:
				first_grid_layout()
			else:
				clear()
				break
		else:
			clear()
			break
	
	if counter % 2 == 0:
		while True:
			try:
				player1_input = int(input(f"{player1_name}, where do you want to place '{player1_shape}': "))
				if not(0 < player1_input <= 9):
					print("Error: Input Out-Of-Bound. Please select again.")
				else:
					break
			except ValueError:
				print("Invalid Character. Please select again.")
			except EOFError:
				force_exit = True
				break
		if force_exit is False:
			player_move_printing(player1_input, player1_shape)
			match_checking(player1_name, player1_input, player1_shape)
		else:
			counter = 9
			clear()
	else:
		while True:
			try:
				player2_input = int(input(f"{player2_name}, select position ({player2_shape}): "))
				if not(0 < player2_input <= 9):
					print("Error: Input Out-Of-Bound. Please select again.")
				else:
					break
			except ValueError:
				print("Invalid Character. Please select again.")
			except EOFError:
				force_exit = True
				break
		if force_exit is False:
			player_move_printing(player2_input, player2_shape)
			match_checking(player2_name, player2_input, player2_shape)
		else:
			counter = 9
			clear()

### Code End ###