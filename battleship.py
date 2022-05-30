import random
import os
import colorama
from colorama import Fore
import platform

PLATFORM_COMMAND = {'Windows':'cls', 'Linux':'clear'}
CLEAR_STRING = PLATFORM_COMMAND[platform.system()] #in these two lines we ask the computer what operating system is running so that we can assign the right command to clear the terminal later

#the first thing we will do is create lists to create four 10 by 10 boards.

LENGTH_OF_SHIPS = [2,3,3,4,5] #These are the different types of ships that exist in the game
PLAYER_BOARD = [[" "] * 8 for i in range(8)] #We are here creating the board for the player on which he will play
COMPUTER_BOARD = [[" "] * 8 for i in range(8)] #And here the board of the computer on which it'll play
PLAYER_GUESS_BOARD = [[" "] * 8 for i in range(8)] #This is the board on which are placed the ships chosen by the computer, which the player will have to guess on PLAYER_BOARD
COMPUTER_GUESS_BOARD = [[" "] * 8 for i in range(8)] #This is the board on which are placed the ships chosen by the player, which the computer will have to guess on COMPUTER_BOARD
LETTERS_TO_NUMBERS = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7} #A dictionary of converting letters to numbers, we will have rows defined by numbers and columns defined by letters
WIN = False
SPACES = " " * 65
spaces_lists = " "* 30
small_console_size = 75


os.system('mode con: cols=200 lines=50')
os.system(CLEAR_STRING)

print(Fore.WHITE + "")
print(Fore.GREEN +"______  ___ _____ _____ _      _____ _____ _   _ ___________  ".center(200))
print(Fore.GREEN +"| ___ \/ _ \_   _|_   _| |    |  ___/  ___| | | |_   _| ___ \ ".center(200))
print(Fore.GREEN +"| |_/ / /_\ \| |   | | | |    | |__ \ `--.| |_| | | | | |_/ / ".center(200))
print(Fore.GREEN +"| ___ \  _  || |   | | | |    |  __| `--. \  _  | | | |  __/  ".center(200))
print(Fore.GREEN +"| |_/ / | | || |   | | | |____| |___/\__/ / | | |_| |_| |     ".center(200))
print(Fore.GREEN +"\____/\_| |_/\_/   \_/ \_____/\____/\____/\_| |_/\___/\_|     ".center(200))
print("")
print("By Michel Kayal, Shayn Cardella and Jean Desazeaud".center(200))
for i in range (5):
    print("")
                                                                                             
                                                                                                    
SPACES = " " * 35                                                                                                   
print(Fore.WHITE + "                                                                                    ..°*°. ....°              ".center(200))
print("                                                                                 °*oOOOooooooOo°....°°*°      ".center(200))
print("                                                                              .*oOoooOOooooooOoooOOOOo°       ".center(200))
print("                                                                             oOo***ooooooooooooooOo°.         ".center(200))
print("                                                                            oo°°°************ooOo°.           ".center(200))
print("                                                                          .*o°..°...°°°°°**oooOooo*.          ".center(200))
print("                                                                      .°*o*OO. ......°°**ooooooOo°            ".center(200))
print("                                                                ..°***oooOooOo .....°°****oooOo°              ".center(200))
print("                                                          ...°**oooooooooOOoOO° ..°°°**oooOOo.                ".center(200))
print("                                                      ..°*ooooooooooooooooOOO#O°..°°**ooOOOo°                 ".center(200))
print("                                                 ..°**ooooOOooooooooooOOOOOOo***oooooOOoo*.                   ".center(200))
print("                                            .°*ooOOOOOOoooOOOoooooOOOOOo*°.      .°°...                       ".center(200))
print("                                       °***oOOo**°°**oOOOooOOOOOOOOo*°.                                       ".center(200))
print("                                 ..°***ooOOo°°°******°°°*OOOO#Oo*°.                                           ".center(200))
print("                              ****ooooooOO°.*OOOOOOOOOOo°.oOOo.                                               ".center(200))
print("                             *oooooooooOo.°OOOooOOoOOoooO*.*#.                                                ".center(200))
print("                            *ooOOOooooOO.°OOOOOoOooooooooOo.*O                                                ".center(200))
print("                            oooOOOoooO#°.OOooooooooooOOOOOO*.O°                                               ".center(200))
print("                         °ooOOooOOOOOOO.*OoooOooOOOOOoo*°. o.oo                                               ".center(200))
print("                         .oo.*OOOOOooOo.oOoOOOOOO*.OO******o.*O                                               ".center(200))
print("                              .OoooooOO.o#OOoOOoOOOOo*°.   o.*o                                               ".center(200))
print("                               °OOOOO##°°O°***.°o*o**.*o*.°* O°                                               ".center(200))
print("                                oOO#O°*O.*o°  .O.°o o*  .oO *O                                                ".center(200))
print("                               *OO#o   oo.*° .o. °o  o* °*.°#.                                                ".center(200))
print("                 .o***        *OO#o     oO°°*o*  °o  °O*°.oO.                                                 ".center(200))
print("                  oO°.       *OO#o       °Oo°°°°°*o°°°°°*O*                                                   ".center(200))
print("                *OOOooOOOOOOOO##*          °ooo***°***oo*.                                                    ".center(200))
print("                °°°°°°°°°°°°°°°°         .   .°°*****°.   ....  ..                                            ".center(200))
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    

                                                               
                                                                                                                                  
                                                                                                                                  
for i in range (3):
    print("")                                                                                                                         

start = input("Press enter to start...".center(200))

os.system(CLEAR_STRING)
os.system('mode con: cols=75 lines=27')

def print_board(board): #In this function we will create the boards such that they are clearly visible, the board variable is used to use all four board we created in the lists above
    print(spaces_lists + '  A B C D E F G H') #Each letter appears above each column for us to make it simpler to choose the letter of the column we want to guess
    print(spaces_lists + '  +-+-+-+-+-+-+-+') #Works uniquely as a saperator
    row_number = 1 #We start by the row number 1 and not 0 as it makes it easier to guess and more logical
    for row in board: #Creating a loop such that the grid fully appears by starting with the row number
        print(spaces_lists + "%d|%s|" % (row_number, "|".join(row))) #"%d is decimal and %s is string. Creating the grid with the row number in the beginning of each row and | as a seperator between each cells
        row_number +=1 #for each iteration, we increase by one for each row to have its appropriate number



def place_ships(board): #In this function, we start by placing the ships of different length also using the board variable for it to work on any of the boards we have created
    #We now want to loop through the length of each ship
    for ship_length in LENGTH_OF_SHIPS: #we loop in the length of each of the ships
        computer_ships_placed = False
        player_ships_placed = False        
        #and now, we loop until the ship fits and doesn't overlap any other ship that has already been placed
        while not computer_ships_placed and not player_ships_placed: #first, we check if it fits, the while loop will keep retrying until we get a fit
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
                        #os.system("cls")
                        #print_board(COMPUTER_BOARD)
                        computer_ships_placed = True
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
                        os.system(CLEAR_STRING)
                        print_board(PLAYER_BOARD)
                        player_ships_placed = True
                 
                    
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
    orientation_locked = False
    if place_ship == True: #If we are placing the ships and not guessing their location 
        #since we are placing the ships, we want an input of the orientation, the row and the column
        orientation = input("Enter orientation, H for horizontal or V for vertical: ".center(small_console_size)).upper()
        while not orientation_locked:
          if orientation == "H" or orientation == "V":
            orientation_locked = True
          else:
            orientation = input("Enter orientation, H for horizontal or V for vertical: ".center(small_console_size)).upper()

        row = input("Enter the row 1-8 of the ship: ".center(small_console_size))  
        while row not in '12345678':
          row = input("Enter the row 1-8 of the ship: ".center(small_console_size))
                
        row = int(row)-1

        column = input("Enter the column of the ship A to H: ".center(small_console_size)).upper()
        while column not in "ABCDEFGH":
          column = input("Enter the column of the ship A to H: ".center(small_console_size)).upper()
        column = LETTERS_TO_NUMBERS[column]

        return row, column, orientation
    else:
        #Since we are now guessing the ships, we don't need to guess the orientation but only the row and the column
        row = input("Enter the row 1-8 of the ship: ".center(small_console_size))
        while row not in '12345678':
          row = input("Enter the row 1-8 of the ship: ".center(small_console_size))
        row = int(row)-1

        column = input("Enter the column of the ship A to H: ".center(small_console_size)).upper()
        while column not in "ABCDEFGH":
          column = input("Enter the column of the ship A to H: ".center(small_console_size)).upper()
        column = LETTERS_TO_NUMBERS[column]
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
                


    #player turn
while not WIN:
    os.system(CLEAR_STRING)
    print(Fore.RED + "Computer's guessing board:".center(small_console_size))
    print_board(COMPUTER_GUESS_BOARD)
    print("")
    print(Fore.BLUE +"Guess a battleship location on the board:".center(small_console_size))   
    print_board(PLAYER_GUESS_BOARD)  #Prints the board each time we play a turn
    turn(PLAYER_GUESS_BOARD)
    if count_hit_ships(PLAYER_GUESS_BOARD) == 17: #Once you hit all parts of all the ships, you win
        os.system(CLEAR_STRING)
        print_board(PLAYER_GUESS_BOARD)
        print(Fore.GREEN + " __     __   ____    _    _        __          __  _____   _   _   _ ")
        print(" \ \   / /  / __ \  | |  | |       \ \        / / |_   _| | \ | | | |")
        print("  \ \_/ /  | |  | | | |  | |        \ \  /\  / /    | |   |  \| | | |")
        print("   \   /   | |  | | | |  | |         \ \/  \/ /     | |   | . ` | | |")
        print("    | |    | |__| | | |__| |          \  /\  /     _| |_  | |\  | |_|")
        print("    |_|     \____/   \____/            \/  \/     |_____| |_| \_| (_)")
        WIN = True

    #COMPUTER TURN
    if not WIN:
        turn(COMPUTER_GUESS_BOARD)
        if count_hit_ships(COMPUTER_GUESS_BOARD) == 17:
            print_board(COMPUTER_GUESS_BOARD)
            print(Fore.GREEN + " __     __   ____    _    _        _         ____     _____   _______   _ ")
            print(" \ \   / /  / __ \  | |  | |      | |       / __ \   / ____| |__   __| | |")
            print("  \ \_/ /  | |  | | | |  | |      | |      | |  | | | (___      | |    | |")
            print("   \   /   | |  | | | |  | |      | |      | |  | |  \___ \     | |    | |")
            print("    | |    | |__| | | |__| |      | |____  | |__| |  ____) |    | |    |_|")
            print("    |_|     \____/   \____/       |______|  \____/  |_____/     |_|    (_)")
            print("                        THE COMPUTER WON !                ")
            WIN = True
