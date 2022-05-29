import random

#the first thing we will do is create lists to create four 10 by 10 boards.

LENGTH_OF_SHIPS = [2,3,3,4,5] #These are the different types of ships that exist in the game
PLAYER_BOARD = [[" "] * 8 for i in range(8)] #We are here creating the board for the player on which he will play
COMPUTER_BOARD = [[" "] * 8 for i in range(8)] #And here the board of the computer on which it'll play
PLAYER_GUESS_BOARD = [[" "] * 8 for i in range(8)] #This is the board on which are placed the ships chosen by the computer, which the player will have to guess on PLAYER_BOARD
COMPUTER_GUESS_BOARD = [[" "] * 8 for i in range(8)] #This is the board on which are placed the ships chosen by the player, which the computer will have to guess on COMPUTER_BOARD
LETTERS_TO_NUMBERS = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7} #A dictionary of converting letters to numbers, we will have rows defined by numbers and columns defined by letters



def print_board(board): #In this function we will create the boards such that they are clearly visible, the board variable is used to use all four board we created in the lists above
    print('  A B C D E F G H') #Each letter appears above each column for us to make it simpler to choose the letter of the column we want to guess
    print('  +-+-+-+-+-+-+-+') #Works uniquely as a saperator
    row_number = 1 #We start by the row number 1 and not 0 as it makes it easier to guess and more logical
    for row in board: #Creating a loop such that the grid fully appears by starting with the row number
        print("%d|%s|" % (row_number, "|".join(row))) #"%d is decimal and %s is string. Creating the grid with the row number in the beginning of each row and | as a seperator between each cells
        row_number +=1 #for each iteration, we increase by one for each row to have its appropriate number



def place_ships(board): #In this function, we start by placing the ships of different length also using the board variable for it to work on any of the boards we have created
    #We now want to loop through the length of each ship
    for ship_length in LENGTH_OF_SHIPS: #we loop in the length of each of the ships
        #and now, we loop until the ship fits and doesn't overlap any other ship that has already been placed
        while True: #first, we check if it fits, the while loop will keep retrying until we get a fit
            if board == COMPUTER_BOARD: #we start by coding how the computer will randomly choose where are located the ships, so the if is used for "if this is the computer ?"
                orientation = random.choice(["H", "V"]) #computer randomly chooses between horizontal (H) and vertical (V) placement of the ship
                row = random.randint(0,7) #computer randomly chooses a row from 1 to 8 on which the first cell of the ship will be placed.  
                column = random.randint(0,7) ##computer randomly chooses a column from 1 to 8 on which the first cell of the ship will be placed.
                if check_ship_fit(ship_length, row, column, orientation): #using the check_ship_fit we will see if the ship length, its orientation, its row and its column do actually fit 
                    #check if ship overlaps 
                    if ship_overlaps(board, row, column, orientation, ship_length) == False:
                        #place ship
                        if orientation == "H":
                            for i in range (column, column + ship_length):
                                board[row][i] = "X"
                        else: 
                            for i in range (row, row + ship_length):
                                board[i][column] = "X"
                        break
            else:
                place_ship = True #here it is to verify that we are placing the ships and not guessing them 
                print('Place the ship with a length of ' + str(ship_length))
                row, column, orientation = user_input(place_ship)
                if check_ship_fit(ship_length, row, column, orientation):
                    #check if ship overlaps 
                    if ship_overlaps(board, row, column, orientation, ship_length) == False:
                        #place ship
                        if orientation == "H":
                            for i in range (column, column + ship_length):
                                board[row][i] = "X"
                        else: 
                            for i in range (row, row + ship_length):
                                board[i][column] = "X"
                        print_board(PLAYER_BOARD)
                        break
                 
                    
#check if ship fits in board
def check_ship_fit(SHIP_LENGTH, row, column, orientation):
    if orientation == "H":
        if column + SHIP_LENGTH > 8:
            return False
        else:
            return True
    else:
        if row + SHIP_LENGTH > 8:
            return False
        else:
            return True
        
        

def ship_overlaps(board, row, column, orientation, ship_length):
    if orientation == "H":
        for i in range(column, column + ship_length):
            if board[row][i] == "X":
                return True
    else:
        for i in range (row, row + ship_length):
            if board[i][column] == "X":
                return True
    return False
           
 

def user_input(place_ship): 
    if place_ship == True: #If we are placing the ships and not guessing their location 
        #since we are placing the ships, we want an input of the orientation, the row and the column
        while True:
            try:
                orientation = input("Enter orientation, H for horizontal or V for vertical: ").upper()
                if orientation == "H" or orientation == "V":
                    break 
            except TypeError:
                print("Please enter a valid orientation, H for horizontal or V for vertical")
        while True:
            try:
                row = input("Enter the row 1-8 of the ship: ")
                if row in '12345678':
                    row = int(row)-1
                    break
            except ValueError:
                print("Please enter a valid number between 1 and 8")
        while True:
            try:
                column = input("Enter the column of the ship A to H: ").upper()
                if column in "ABCDEFGH":
                    column = LETTERS_TO_NUMBERS[column]
                    break
            except KeyError:
                print ("Please enter a valid column letter between A-H")

        return row, column, orientation
    else:
        #Since we are now guessing the ships, we don't need to guess the orientation but only the row and the column
        while True:
            try:
                row = input("Enter the row 1-8 of the ship: ")
                if row in '12345678':
                    row = int(row) - 1
                    break
            except ValueError:
                print("Please enter a valid number between 1 and 8")
        while True:
            try:
                column = input("Enter the column of the ship A to H: ").upper()
                if column in "ABCDEFGH":
                    column = LETTERS_TO_NUMBERS[column]
                    break
            except KeyError:
                print ("Please enter a valid column letter between A-H")
        return row, column
            

def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count
    

def turn(board):
    if board == PLAYER_GUESS_BOARD:
        row, column = user_input(PLAYER_GUESS_BOARD)
        if board[row][column] == "-":
            turn(board)
        elif board[row][column] == "X":
            turn(board)
        elif COMPUTER_BOARD[row][column] == "X":
            board[row][column] = "X"
        else:
            board[row][column] = "-"
    else:
        row, column = random.randint(0,7), random.randint(0,7)
        if board[row][column] == "-":
            turn(board)
        elif board[row][column] == "X":
            turn(board)
        elif PLAYER_BOARD[row][column] == "X":
            board[row][column] = "X"
        else:
            board[row][column] = "-"

place_ships(COMPUTER_BOARD)
print_board(PLAYER_BOARD)
place_ships(PLAYER_BOARD)
print_board(COMPUTER_GUESS_BOARD)
                

while True:
    #player turn
    while True:
        print("Guess a battleship location")   #
        print_board(PLAYER_GUESS_BOARD)  #Prints the board each time we play a turn
        turn(PLAYER_GUESS_BOARD)
        break
    if count_hit_ships(PLAYER_GUESS_BOARD) == 17:
        print(" __     __   ____    _    _        __          __  _____   _   _   _ ")
        print(" \ \   / /  / __ \  | |  | |       \ \        / / |_   _| | \ | | | |")
        print("  \ \_/ /  | |  | | | |  | |        \ \  /\  / /    | |   |  \| | | |")
        print("   \   /   | |  | | | |  | |         \ \/  \/ /     | |   | . ` | | |")
        print("    | |    | |__| | | |__| |          \  /\  /     _| |_  | |\  | |_|")
        print("    |_|     \____/   \____/            \/  \/     |_____| |_| \_| (_)")
        break
    #COMPUTER TURN
    while True:
        turn(COMPUTER_GUESS_BOARD)
        break
    print_board(COMPUTER_GUESS_BOARD)
    if count_hit_ships(COMPUTER_GUESS_BOARD) == 17:
        print(" __     __   ____    _    _        _         ____     _____   _______   _ ")
        print(" \ \   / /  / __ \  | |  | |      | |       / __ \   / ____| |__   __| | |")
        print("  \ \_/ /  | |  | | | |  | |      | |      | |  | | | (___      | |    | |")
        print("   \   /   | |  | | | |  | |      | |      | |  | |  \___ \     | |    | |")
        print("    | |    | |__| | | |__| |      | |____  | |__| |  ____) |    | |    |_|")
        print("    |_|     \____/   \____/       |______|  \____/  |_____/     |_|    (_)")
        print("                        THE COMPUTER WON !                ")
        break
