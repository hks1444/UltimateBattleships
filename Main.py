
# Ultimate Battleships

def print_ships_to_be_placed():
    print("Ships to be placed:", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Ships to be placed: ")


# elem expected to be a single list element of a primitive type.
def print_single_element(elem):
    print(str(elem), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write(str(elem) + " ")


def print_empty_line():
    print()
    if FILE_OUTPUT_FLAG:
        f.write("\n")


# n expected to be str or int.
def print_player_turn_to_place(n):
    print("It is Player {}'s turn to place their ships.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to place their ships.\n".format(n))


def print_to_place_ships():
    print("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) : \n")
        # There is a \n because we want the board to start printing on the next line.


def print_incorrect_input_format():
    print("Input is in incorrect format, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Input is in incorrect format, please try again.\n")


def print_incorrect_coordinates():
    print("Incorrect coordinates given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect coordinates given, please try again.\n")


def print_incorrect_ship_name():
    print("Incorrect ship name given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect ship name given, please try again.\n")


def print_incorrect_orientation():
    print("Incorrect orientation given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect orientation given, please try again.\n")


# ship expected to be str.
def print_ship_is_already_placed(ship):
    print(ship, "is already placed, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " is already placed, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_outside(ship):
    print(ship, "cannot be placed outside the board, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed outside the board, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_occupied(ship):
    print(ship, "cannot be placed to an already occupied space, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed to an already occupied space, please try again.\n")


def print_confirm_placement():
    print("Confirm placement Y/N :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Confirm placement Y/N : \n")


# n expected to be str or int.
def print_player_turn_to_strike(n):
    print("It is Player {}'s turn to strike.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to strike.\n".format(n))


def print_choose_target_coordinates():
    print("Choose target coordinates :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Choose target coordinates : ")


def print_miss():
    print("Miss.")
    if FILE_OUTPUT_FLAG:
        f.write("Miss.\n")


# n expected to be str or int.
def print_type_done_to_yield(n):
    print("Type done to yield your turn to player {} :".format(n), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Type done to yield your turn to player {} : \n".format(n))


def print_tile_already_struck():
    print("That tile has already been struck. Choose another target.")
    if FILE_OUTPUT_FLAG:
        f.write("That tile has already been struck. Choose another target.\n")


def print_hit():
    print("Hit!")
    if FILE_OUTPUT_FLAG:
        f.write("Hit!\n")


# n expected to be str or int.
def print_player_won(n):
    print("Player {} has won!".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("Player {} has won!\n".format(n))


def print_thanks_for_playing():
    print("Thanks for playing.")
    if FILE_OUTPUT_FLAG:
        f.write("Thanks for playing.\n")


# my_list expected to be a 3-dimensional list, formed from two 2-dimensional lists containing the boards of each player.
def print_3d_list(my_list):
    first_d = len(my_list[0])
    for row_ind in range(first_d):
        second_d = len(my_list[0][row_ind])
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[0][row_ind][col_ind], end=' ')
        print("\t\t\t", end='')
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[1][row_ind][col_ind], end=' ')
        print()
    print("", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\t\t", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\nPlayer 1\t\t\t\t\t\tPlayer 2")
    print()

    if FILE_OUTPUT_FLAG:
        first_d = len(my_list[0])
        for row_ind in range(first_d):
            second_d = len(my_list[0][row_ind])
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[0][row_ind][col_ind] + " ")
            f.write("\t\t\t")
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[1][row_ind][col_ind] + " ")
            f.write("\n")
        f.write("   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\t\t   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\nPlayer 1\t\t\t\t\t\tPlayer 2\n")
        f.write("\n")


def print_rules():
    print("Welcome to Ultimate Battleships")
    print("This is a game for 2 people, to be played on two 10x10 boards.")
    print("There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).")
    print("First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.")
    print("Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.")
    print("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.")
    print("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.")
    print("Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.")
    print("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.")
    print("The last player to have an unsunk ship wins.")
    print("Have fun!")
    print()

    if FILE_OUTPUT_FLAG:
        f.write("Welcome to Ultimate Battleships\n")
        f.write("This is a game for 2 people, to be played on two 10x10 boards.\n")
        f.write(
            "There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).\n")
        f.write(
            "First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.\n")
        f.write(
            "Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.\n")
        f.write("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.\n")
        f.write("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.\n")
        f.write(
            "Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.\n")
        f.write("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.\n")
        f.write("The last player to have an unsunk ship wins.\n")
        f.write("Have fun!\n")
        f.write("\n")


# Create the game
board_size = 10
f = open('UltimateBattleships.txt', 'w')
FILE_OUTPUT_FLAG = False  # can be changed to true if you want to see the output as a text file
print_rules()

try:  # The entire code is in this try block, if there ever is an error during execution, we can safely close the file.
    ships = {"carrier": 5, "battleship": 4, "cruiser": 3, "submarine": 3, "destroyer": 2}
    ships1cont = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
    ships2cont = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
    ships1cont_checker = ["carrier", "battleship", "cruiser", "submarine", "destroyer"]
    ships2cont_checker = ["carrier", "battleship", "cruiser", "submarine", "destroyer"]
    check222 = True  # this bool helped fixing a bug at confirming placement
    t = 1 # checking which player's turn at the moment
    record1 = []  # this variable records where the first player placed his/her ships
    record_shot1o = []  # this variable records coordinates which was shot by first player and hit second player's ships
    record_miss1o = []  # this variable records coordinates which was shot by first player and did no hit second player's ships
    record2 = []  # this variable records where the second player placed his/her ships
    record_shot2o = []  # this variable records coordinates which was shot by second player and hit first player's ships
    record_miss2o = []  # this variable records coordinates which was shot by second player and did not hit first player's ships
    while t != 0:  # this while keeps players from continuing until they both fill the board correctly
        if check222:
            v = []
            b1 = [["#" if [x+1, y+1] in record1 and t == 1 else "-" for x in range(board_size)] for y in range(board_size)]  # filling first board list
            b2 = [["#" if [x+1, y+1] in record2 and t == 2 else "-" for x in range(board_size)]for y in range(board_size)]  # filling second board list
            c = [b1, b2]  # creating 3d board list
            print_3d_list(c)  # prints board
        if t == 1:
            if not ships1cont:  # if all the ships are placed player will be asked to confirm the final placement for player 1
                print_confirm_placement()
                dn = input().lower()
                if dn == "y":  # if input is y placement is confirmed
                    t = 2
                    check222 = True
                    continue
                elif dn == "n":  # if input is n everything is reset
                    record1 = []
                    ships1cont = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
                    ships1cont_checker = ["carrier", "battleship", "cruiser", "submarine", "destroyer"]
                    check222 = True
                    continue
                else:  # keeps player in confirmation loop until acceptable input is entered
                    check222 = False
                    continue
        if t == 2:  # if all the ships are placed player will be asked to confirm the final placement for player 2
            if not ships2cont:
                print_confirm_placement()
                dn = input().lower()
                if dn == "y":  # if input is y placement is confirmed
                    t = 0
                    check222 = True
                    continue
                elif dn == "n":  # if input is n everything is reset
                    ships2cont = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
                    record2 = []
                    ships2cont_checker = ["carrier", "battleship", "cruiser", "submarine", "destroyer"]
                    check222 = True
                    continue
                else:  # keeps player in confirmation loop until acceptable input is entered
                    check222 = False
                    continue
        print_ships_to_be_placed()
        if t == 1:
            ship = [print_single_element(ship) for ship in ships1cont]  # printing remaining ships to be placed for player 1
        elif t == 2:
            ship = [print_single_element(ship) for ship in ships2cont]  # printing remaining ships to be placed for player 2
        print_empty_line()
        print_player_turn_to_place(t)
        print_to_place_ships()
        deployment = input()
        dep = deployment.split(" ")
        try:  # checking whether the coordinates are given as integers
            dep[1] = int(dep[1])
            dep[2] = int(dep[2])
        except:
            print_incorrect_input_format()
            continue
        if len(dep) != 4:  # checking for the correct number of arguments
            print_incorrect_input_format()
            continue
        if not(0 < int(dep[1]) < 11 and 0 < int(dep[2]) < 11):  # checking whether coordinates are inside the board
            print_incorrect_coordinates()
            continue
        if not(dep[0].lower() in ships):  # checking whether the ship's name is correct
            print_incorrect_ship_name()
            continue
        if not(dep[3].lower() == "h" or dep[3].lower() == "v"):  # checking whether the orientation is correct
            print_incorrect_orientation()
            continue
        if t == 1:
            if not (dep[0].lower() in ships1cont_checker):  # checking if the ship is placed or not
                print_ship_is_already_placed(dep[0][0].upper()+dep[0][1:].lower())
                continue
            if dep[3].lower() == "h":  # placing ship horizontally
                cor = [[int(dep[1])+q, int(dep[2])]for q in range(ships[dep[0].lower()])] # adds coordinates without considering anything
                cor_check1 = [x for x in cor if 0 < x[0] < 11 and 0 < x[1] < 11]  # adds coordinates with respect to boundaries
                if len(cor_check1) != len(cor):  # checks if the placement of ship exceeds boundaries
                    print_ship_cannot_be_placed_outside(dep[0][0].upper()+dep[0][1:].lower())
                    continue
                cor_check2 = [x for x in cor if not (x in record1)]  # adding coordinates which does not intersect already placed ships
                if len(cor_check2) != len(cor):  # checks if ship intersects another ship
                    print_ship_cannot_be_placed_occupied(dep[0][0].upper()+dep[0][1:].lower())
                    continue
                record1 = record1 + [x for x in cor]
            elif dep[3].lower() == "v":  # placing ship vertically
                cor = [[int(dep[1]), int(dep[2])+q] for q in range(ships[dep[0].lower()])]  # adds coordinates without considering anything
                cor_check1 = [x for x in cor if 0 < x[0] < 11 and 0 < x[1] < 11]  # adds coordinates with respect to boundaries
                if len(cor_check1) != len(cor):  # checks if the placement of ship exceeds boundaries
                    print_ship_cannot_be_placed_outside(dep[0][0].upper()+dep[0][1:].lower())
                    continue
                cor_check2 = [x for x in cor if not(x in record1)]  # adding coordinates which does not intersect already placed ships
                if len(cor_check2) != len(cor):  # checks if ship intersects another ship
                    print_ship_cannot_be_placed_occupied(dep[0][0].upper()+dep[0][1:].lower())
                    continue
                record1 = record1 + [x for x in cor]  # adding ship's placement into record if there is no problem
            ships1cont = [ships1cont[x] for x in range(len(ships1cont)) if dep[0].lower() != ships1cont[x].lower()]
            ships1cont_checker = [ships1cont[x].lower() for x in range(len(ships1cont)) if dep[0].lower() != ships1cont[x].lower()]
            # removing placed ship's name from container lists if there is no problem
        elif t == 2:
            if not (dep[0].lower() in ships2cont_checker):
                print_ship_is_already_placed(dep[0][0].upper()+dep[0][1:].lower())
                continue
            if dep[3].lower() == "h":  # placing ship horizontally
                if dep[0].lower() in ships:
                    cor = [[int(dep[1]) + q, int(dep[2])] for q in range(ships[dep[0].lower()])]  # adds coordinates without considering anything
                    cor_check1 = [x for x in cor if 0 < x[0] < 11 and 0 < x[0] < 11]  # adds coordinates with respect to boundaries
                    if len(cor_check1) != len(cor):  # checks if the placement of ship exceeds boundaries
                        print_ship_cannot_be_placed_outside(dep[0][0].upper()+dep[0][1:].lower())
                        continue
                    cor_check2 = [x for x in cor if not (x in record2)]  # adding coordinates which does not intersect already placed ships
                    if len(cor_check2) != len(cor):  # checks if ship intersects another ship
                        print_ship_cannot_be_placed_occupied(dep[0][0].upper()+dep[0][1:].lower())
                        continue
                    record2 = record2 + [x for x in cor]  # adding ship's placement into record if there is no problem
            elif dep[3].lower() == "v":  # placing ship vertically
                if dep[0].lower() in ships:
                    cor = [[int(dep[1]), int(dep[2]) + q] for q in range(ships[dep[0].lower()])]  # adds coordinates without considering anything
                    cor_check1 = [x for x in cor if 0 < x[0] < 11 and 0 < x[0] < 11]  # adds coordinates with respect to boundaries
                    if len(cor_check1) != len(cor):  # checks if the placement of ship exceeds boundaries
                        print_ship_cannot_be_placed_outside(dep[0][0].upper()+dep[0][1:].lower())
                        continue
                    cor_check2 = [x for x in cor if not (x in record2)]  # adding coordinates which does not intersect already placed ships
                    if len(cor_check2) != len(cor):  # checks if ship intersects another ship
                        print_ship_cannot_be_placed_occupied(dep[0][0].upper()+dep[0][1:].lower())
                        continue
                    record2 = record2 + [x for x in cor]  # adding ship's placement into record if there is no problem
            ships2cont = [ships2cont[x] for x in range(len(ships2cont)) if dep[0].lower() != ships2cont[x].lower()]
            ships2cont_checker = [ships2cont[x].lower() for x in range(len(ships2cont)) if dep[0].lower() != ships2cont[x].lower()]
            # removing placed ship's name from container lists if there is no problem
    t = 1
    while True:
        if t == 1:
            b1 = [["#" if [x + 1, y + 1] in record1 else "!" if [x + 1, y + 1] in record_shot2o else "O" if [x + 1, y + 1] in record_miss2o else "-" for x in range(board_size)]for y in range(board_size)]
            b2 = [["!" if [x + 1, y + 1] in record_shot1o else "O" if [x + 1, y + 1] in record_miss1o else "-" for x in range(board_size)]for y in range(board_size)]
            # creates boards according to miss,shot,placement(record) records and creates fog of war at the player 2's board at the player 1's turn
            c = [b1, b2] # creates 3d board list
            print_3d_list(c)
            if not record2:  # ends game if all the ships of player 2 is sunk
                break
            print_player_turn_to_strike(t)
            print_choose_target_coordinates()
            hit = input()
            fire = hit.split(" ")
            if not(len(fire) == 2):  # checks whether firing coordinates input has enough argument
                print_incorrect_input_format()
                continue
            try:   # checks whether firing coordinates input has 2 integers
                fire[0] = int(fire[0])
                fire[1] = int(fire[1])
            except:
                print_incorrect_input_format()
                continue
            fire = [int(fire[x]) for x in range(len(fire))]  # converts strings to integer coordinates
            if not(0 < fire[0] < 11 and 0 < fire[1] < 11):  # checks whether firing coordinates input is in the board
                print_incorrect_coordinates()
                continue
            if fire in record_shot1o or fire in record_miss1o:  # checks if the tile is already struck or not
                print_tile_already_struck()
                continue
            fire2 = [fire[x] for x in range(len(fire))]
            if fire2 in record2:  # checks whether the struck tile has a piece of ship
                record_shot1o = record_shot1o + [fire2 for x in range(1)]  # adds coordinates to shooting recording
                print_hit()
                record2 = [x for x in record2 if x != fire2]  # removing coordinates from remaining ships
                continue
            else:
                record_miss1o = record_miss1o + [fire2 for x in range(1)]  # if player misses coordinates are added to miss record
                print_miss()
            dn = ""
            while dn != "done":  # player expected to provide done input to yield turn
                t = 2
                print_type_done_to_yield(t)
                dn = input().lower()
        elif t == 2:
            b1 = [["!" if [x + 1, y + 1] in record_shot2o else "O" if [x + 1, y + 1] in record_miss2o else "-" for x in range(board_size)] for y in range(board_size)]
            b2 = [["#" if [x + 1, y + 1] in record2 else "!" if [x + 1, y + 1] in record_shot1o else "O" if [x + 1, y + 1] in record_miss1o else "-" for x in range(board_size)] for y in range(board_size)]
            # creates boards according to miss,shot,placement(record) records and creates fog of war at the player 1's board at the player 2's turn
            c = [b1, b2]  # creates 3d board list
            print_3d_list(c)
            if not record1:  # ends game if all the ships of player 1 is sunk
                break
            print_player_turn_to_strike(t)
            print_choose_target_coordinates()
            hit = input()
            fire = hit.split(" ")
            if not(len(fire) == 2):   # checks whether firing coordinates input has enough argument
                print_incorrect_input_format()
                continue
            try:  # checks whether firing coordinates input has 2 integers
                fire[0] = int(fire[0])
                fire[1] = int(fire[1])
            except:
                print_incorrect_input_format()
                continue
            fire = [int(fire[x]) for x in range(len(fire))]  # converts strings to integer coordinates
            if not(0 < fire[0] < 11 and 0 < fire[1] < 11):  # checks whether firing coordinates input is in the board
                print_incorrect_coordinates()
                continue
            if fire in record_shot2o or fire in record_miss2o:  # checks if the tile is already struck or not
                print_tile_already_struck()
                continue
            fire2 = [fire[x] for x in range(len(fire))]
            if fire2 in record1:  # checks whether the struck tile has a piece of ship
                record_shot2o = record_shot2o + [fire2 for x in range(1)]  # adds coordinates to shooting recording
                print_hit()
                record1 = [x for x in record1 if x != fire2]  # removing coordinates from remaining ships
                continue
            else:
                record_miss2o = record_miss2o + [fire2 for x in range(1)]  # if player misses coordinates are added to miss record
                print_miss()
            dn = ""
            while dn != "done":  # player expected to provide done input to yield turn
                t = 1
                print_type_done_to_yield(t)
                dn = input().lower()
    print_player_won(t)  # prints winner at the end
    print_thanks_for_playing()
except:
    f.close()

