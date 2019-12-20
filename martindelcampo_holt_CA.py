# Names: Liam Holt, Alvaro Martin del Campo
# Date: December 16th, 2019
# Program Name: Connect Four (martindelcampo_holt_CA.py)
# Description: User and CPU compete on the battlefield in a treacherous Connect Four Board Game.

# Infomation:
# Grid is 6x7
# 7 horizontal
# 6 vertical

# Sources:
# https://en.wikipedia.org/wiki/List_of_Unicode_characters
# https://unicode-search.net/unicode-namesearch.pl?term=CIRCLE

# Import Statments here:
import random  # Import the random library


# ================================= Functions here ====================================


# Alvaro 
# Function that checks if the CPU won the game.          
def check_lose(array, lose_type):
    ## COLUMN/ VERTICAL CHECK
    # checks all 7 seven columns in grid(a.k.a array).
    for column in range(7):
        # checks rows, starting from the 5th/ bottom one until the 3rd upmost column, going up by one each time.
        # Other rows above dont have enough space for a full connect 4, so no need to check them.
        for row in range(5, 2, -1):
            # 2 on a grid means a CPU placed piece.
            # For loops pick a starting position, and then if statement checks the next 3 consecutive rows by going up by 1 each time.
            if array[column][row] == 2 and array[column][row-1]== 2 and array[column][row-2] == 2 and array[column][row-3]== 2:
                # All 4 places, had a CPU piece so connect 4 in column.
                lose = True # User loses
                lose_type.append('Vertical') # Type of loss is vertical.
                return lose
            else:
                lose = False # User didn't lose
                lose_type.clear() # Clear the list, no lose to add.
    ### ROW/HORIZONTAL CHECK
    # checks all rows in the grid.
    for row in range(5, -1, -1):
        # Going from left, Checks the leftmost 4 columns, the other ones don't have enough space for connect 4.
        for column in range(0,4):
            # 2 on a grid means a CPU placed piece.
            # For loops pick a starting position, and then if statement checks the next 4 consecutive columns going left by 1 each time.
            if array[column][row] == 2 and array[column+1][row]== 2 and array[column+2][row] == 2 and array[column+3][row]== 2:
                lose = True # All 4 places, had a CPU piece so connect 4 in row.
                lose_type.append('Horizontal') # Type of loss is horizontal.
                return lose
            else:
                lose = False # User didn't lose
                lose_type.clear()# Clear the list, no lose to add.

    # Diagonals are split into an X with one loop checking  \ direction and the other checking / direction. 
    
    ## RIGHT UP DIAGONAL CHECK  
    # checks rows, starting from the 5th/ bottom one until the 3rd upmost column, going up by one each time.
    # Other rows above dont have enough space for a full connect 4, so no need to check them.     
    for row in range(5, 2, -1):
        # Going from left, Checks the leftmost 4 columns, the other ones don't have enough space for connect 4.
        for column in range(0,4):
            # 2 on a grid means a CPU placed piece.
            # For loops pick a starting position, and then if statement checks the next 4 places in a diagonal going up by 1 row and right by 1 column each time.
            if array[column][row] == 2 and array[column+1][row-1] == 2 and array[column+2][row-2] == 2 and array[column+3][row-3] == 2:

                lose = True # All 4 places, had a CPU piece so connect 4 in a diagonal.
                lose_type.append('Diagonal') # Type of loss is diagonal.
                return lose
            else:
                lose = False# User didn't lose
                lose_type.clear()# Clear the list, no lose to add.
    ## RIGHT DOWN DIAGONAL CHECK
    # checks top 3 rows, other rows are either checked by prev. for loop, or don't have enough space for connect 4.
    # Other rows above dont have enough space for a full connect 4, so no need to check them.   
    for row in range(0,3):
     # Going from left, Checks the leftmost 4 columns, the other ones don't have enough space for connect 4.
        for column in range(0,4):
            # 2 on a grid means a CPU placed piece.
            # For loops pick a starting position, and then if statement checks the next 4 places in a diagonal going down by 1 row and right by 1 column each time.           
            if array[column][row] == 2 and array[column+1][row+1] == 2 and array[column+2][row+2] == 2 and array[column+3][row+3] == 2:
                lose = True# All 4 places, had a CPU piece so connect 4 in a diagonal.
                lose_type.append('Diagonal') # Type of loss is diagonal.
                return lose
            else:
                lose = False# User didn't lose
                lose_type.clear()# Clear the list, no lose to add.
    return lose # If all 4 loops, produced a False Lose value, return lose.

# Alvaro
# Function that checks if user won game.
def check_win(array, win_type):
     ## COLUMN/ VERTICAL CHECK
     #checks all 7 seven columns in grid(a.k.a array) 
    for column in range(7): 
        # checks rows, starting from the 5th/ bottom one until the 3rd upmost column, going up by one each time.
        # Other rows above dont have enough space for a full connect 4, so no need to check them.
        for row in range(5, 2, -1):
            # 1 on a grid means a user placed piece.
            # For loops pick a starting position, and then if statement checks the next 3 consecutive rows by going up by 1 each time.
            if array[column][row] == 1 and array[column][row-1]==1 and array[column][row-2] == 1 and array[column][row-3]==1:
                win = True # User wins
                win_type.append('Vertical')# Type of win is vertical.
                return win
            else:
                win = False # User didn't win
                win_type.clear() # Clear the list, no win to add.
    ### ROW/HORIZONTAL CHECK
    # checks all rows in the grid.
    for row in range(5, -1, -1): 
        # Going from left, Checks the leftmost 4 columns, the other ones don't have enough space for connect 4.
        for column in range(0,4):
            # 1 on a grid means a user placed piece.
            # For loops pick a starting position, and then if statement checks the next 4 consecutive columns going left by 1 each time.
            if array[column][row] == 1 and array[column+1][row]==1 and array[column+2][row] == 1 and array[column+3][row]==1:
                win = True# User wins
                win_type.append('Horizontal') # Type of win is vertical.
                return win
            else:
                win = False# User didn't win
                win_type.clear() # Clear the list, no win to add.
     # Diagonals are split into an X with one loop checking  \ direction and the other checking / direction. 
    ## RIGHT UP DIAGONAL CHECK  
# checks rows, starting from the 5th/ bottom one until the 3rd upmost column, going up by one each time.
    # Other rows above dont have enough space for a full connect 4, so no need to check them.
    for row in range(5, 2, -1): # UPWARD DIAGONAL
        for column in range(0,4): 
            # 1 on a grid means a user placed piece.
        # For loops pick a starting position, and then if statement checks the next 4 places in a diagonal going up by 1 row and right by 1 column each time.
            if array[column][row] == 1 and array[column+1][row-1] == 1 and array[column+2][row-2] == 1 and array[column+3][row-3] == 1:
                win = True# User wins
                win_type.append('Diagonal')# Type of win is vertical.
                return win
            else:
                win = False# User didn't win
                win_type.clear() # Clear the list, no win to add.
     ## RIGHT DOWN DIAGONAL CHECK
    # checks top 3 rows, other rows are either checked by prev. for loop, or don't have enough space for connect 4.
    # Other rows above dont have enough space for a full connect 4, so no need to check them.     
    for row in range(0,3):
        # Going from left, Checks the leftmost 4 columns, the other ones don't have enough space for connect 4.
        for column in range(0,4): # DOWNWARDS DIAGONAL
        # 1 on a grid means a user placed piece.
     # For loops pick a starting position, and then if statement checks the next 4 places in a diagonal going down by 1 row and right by 1 column each time.
            if array[column][row] == 1 and array[column+1][row+1] == 1 and array[column+2][row+2] == 1 and array[column+3][row+3] == 1:
                win = True # User wins
                win_type.append('Diagonal')# Type of win is vertical.
                return win
            else:
                win = False# User didn't win
                win_type.clear() # Clear the list, no win to add.
    return win # If all 4 loops, produced a False win value, return win.


# Alvaro
# get users desired column that they would like to place a peice
def ask_userchoice():
    # get user input, desired column or quit the game and assign to choice
    choice = input('Input a column header to play or (Q) to Quit: ')
    # return choice
    return choice


# Alvaro
# check the users choice, if the move is in the movelist
def check_userchoice(move, movelist):
    check = move in movelist  # check if move is in the list movelist
    if check == True:  # if check is eqaul to True, then it is a valid choice.
        invalid_choice = False
    elif move == 'Quit': #if the user quit, its a valid move.
        invalid_choice = False
    else: # Anything else is invalid
        invalid_choice = True # Invalid move is true, print msg to user.
        print('That column is not on the board. ')
        print('Pick a different column.')
        print('')
    return invalid_choice # Return boolean of invalid_choice.


# Alvaro
# Assign a number used in lists from the grid based on user input column choice.
def find_pos(move):
    if move == 'A' or move == 'a':
        pos = 0
    elif move == 'B' or move == 'b':
        pos = 1
    elif move == 'C' or move == 'c':
        pos = 2
    elif move == 'D' or move == 'd':
        pos = 3
    elif move == 'E' or move == 'e':
        pos = 4
    elif move == 'F' or move == 'f':
        pos = 5
    elif move == 'G' or move == 'g':
        pos = 6
    elif move == 'Q' or move == 'q': # User quit
        pos = 'Quit'
    else:  # Anything else
        pos = 'Null'
    return pos


# Alvaro
# check if the bottom most row in the column already has a piece in it.
def check_move(pos, gridlist, row):
    row = int(row)
    # 2D array. depending on column and row chosen, if 1 or 2 is in the pos in the grid it's full.
    if gridlist[pos][row] == 1 or gridlist[pos][row] == 2:
        spot_full = True
    # If anything else, most likely a 0, then it's empty.
    else:
        spot_full = False # set spot_full to False sss
    return spot_full 


# Alvaro
# check if the column chosen is completely full.
def check_fullcol(gridlist, pos):
    # pos 0 in list repr. the top row, so if 1 or 2 is in pos, then it's full.
    if gridlist[pos][0] == 1 or gridlist[pos][0] == 2:
        print('The column is full.')
        spot_full = True
        return spot_full
    # If anything else, then it's not full.
    else:
        spot_full = False
        return spot_full


# Alvaro
# create random cpu move.
def get_cpumove(moves):
    # generates a random move from the list of moves possible.
    choice = random.choice(moves)
    # prints move chosen.
    print('The computer moved in the ' + str.upper(choice) + ' row.')
    return choice

# Liam
# Function for messages if user loses the game.
def print_lose_msg(lose, lose_type):
    # User did lose.
    if lose == True:
        # FOR THE FOLLWING IFS
        # If the item in the first position appended to the list from the fxn: check_lose, is 'x'', then print 'y'.
        # If vertical cpu win, print  msg. 
        if lose_type[0] == 'Vertical':
            print()
            print('We have a vertical Connect 4! CPU has Won!')
            print(' ⌽')
            print(' ⌽')
            print(' ⌽')
            print(' ⌽')
        # If horizontal cpu win, print  msg.
        elif lose_type[0] == 'Horizontal':
            print()
            print('We have a Horizontal Connect 4! CPU has Won!')
            print(' ⦵⦵⦵⦵')
        # If diagonal cpu win, print  msg
        elif lose_type[0] == 'Diagonal':
            print('We have a Diagonal Connect 4! CPU has Won!')
            print(' ⍉')
            print('   ⍉')
            print('     ⍉')
            print('       ⍉') 
        else: # Failsafe, prints error.
           print('List Error 2')
    else: # Prints nothing
        print()
        
# Liam 
# Function for messages if user wins game.
def print_win_msg(win, win_type):
   # User won game. 
    if win == True:
        # FOR THE FOLLOWING IFS
         # If the item in the first position appended to the list from the fxn: check_win, is 'x'', then print 'y'.
        # Vertical win, print msg.
        if win_type[0] == 'Vertical':
            print()
            print('We have a vertical Connect 4! You have Won!')
            print(' ⌽')
            print(' ⌽')
            print(' ⌽')
            print(' ⌽')
        # Horizontal win, print msg.
        elif win_type[0] == 'Horizontal':
            print()
            print('We have a Horizontal Connect 4! You have Won!')
            print(' ⦵⦵⦵⦵')
        # Diagonal win, print msg.
        elif win_type[0] == 'Diagonal':
            print('We have a Diagonal Connect 4! You have Won!')
            print(' ⍉')
            print('   ⍉')
            print('     ⍉')
            print('       ⍉') 
        else: # Failsafe, prints error.
           print('List Error 2')
    else: # Prints nothing.
        print()

# Liam
# display opening message
def opening_message():
    # print opening message
    print('')
    print('just a couple dudes and recursion ಠ_ಠ')
    print('##### Welcome to Connect Four! #######')
    print('')


# Liam
# display menu options
def showMenu():
    # print menu options
    print(' Connect 4!')
    print('============')
    print(' 1 to Start')
    print(' 2 for Help')
    print(' 3 to Quit')
    print('============')
    print(' ')


# Liam
# get users choice to either start, quit or see the help menu
def getChoice():
    try: # exception handling 
        choice = int(input('Option?: ')) # get user option
        return choice  # return choice
    except ValueError:  # exception handling if value error occurs, print message 
        print('Invalid Option! Try Again...')


# Liam
# show help menu
def showHelp():
    print('')
    print('           Connect Four Rules: ')  # print header 
    print('')
    print('  - To play Connect 4, try to get 4 of your')  # print connect four rules 
    print('    checkers in a row horizontally,') 
    print('    vertically, or diagonally before your')
    print('    opponent. When its your turn, drop one of') 
    print('    your checkers into one of the slots at the') 
    print('    top of the grid.')
    print('')
    print('  - refer to martindelcampo_holt_CA_readme.txt for more info')  # refer to additional read me
    print('')   # print blankline 

# Liam
# display welcome message - connect four
def display_wlcome():
    # print ascii title
    print('')
    print('###############################################################')
    print(' _________                                     __       _____  ')
    print(' \_   ___ \  ____   ____   ____   ____   _____/  |_    /  |  | ')
    print(' /    \  \/ /  _ \ /    \ /    \_/ __ \_/ ___\   __\  /   |  |_')
    print('       \___(  <_> )   |  \   |  \  ___/\  \___|  |   /    ^   /')
    print('  \______  /\____/|___|  /___|  /\___  >\___  >__|   \____   | ')
    print('         \/            \/     \/     \/     \/            |__| ')
    print('')
    print('###############################################################')


# Liam
# create the board 6 by 7
def create_board(board):
    # append to the board in range of 6 (create board)
    for i in range(6):
        board.append([' '] * 9)


# Liam
# print the board
def print_board(board):
    print('')  # print a blank line
    print("  A B C D E F G")  # print columns headers
    for row in range(len(board)):  # seperates each column/list with |
        print('║'.join(board[row]))  # join items in the array with the charcter ║
    print('') # print a blank line  


# Liam
# add player peice to the board
def add_player_peice(grid, user_pos, row_pos, board):
    grid[user_pos][row_pos] = 1  # Grid used for recursion add a num
    board[row_pos][user_pos + 1] = 'o'  # Board printed for user, add an o


# Liam
# add cpu peice to the board
def add_comp_peice(grid, cpu_pos, row_pos, board):
    grid[cpu_pos][row_pos] = 2  # Grid used for recursion add a num
    board[row_pos][cpu_pos + 1] = '●'  # Board printed for user, add a ●



# ============================ Global Variables ==============================

flag = True  # flag to begin code is True

# ============================ Code Here =====================================

opening_message()  # display opening message.
# Flag is entire code running, while true:
while flag:
    showMenu()  # show starting menu
    user_choice = getChoice()  # get users choice
    # based on users choice perform desired functions and set appropriate flags
    if user_choice == 2:  # Help Option
        showHelp()
        program_flag = False
        flag = True
    elif user_choice == 3:  # Quit Option
        flag = False
        program_flag = False
    elif user_choice == 1:  # Start Game Option
        flag = False
        program_flag = True
    # if user does not choose a valid option
    else:  # Invalid option
        print('') #print blank line 
        program_flag = False
    
    ##### GLOBAL VARIABLES - reset after each game.
    # create move set list: all available options for columns
    move_set_user = [
        'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g',
        'Q', 'q'
    ]
    move_set_cpu = [
        'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g'
    ]
    # assign bord as a list
    board = []
    # create all columns (2d array) and add them to grid
    column1 = ['0', '0', '0', '0', '0', '0']
    column2 = ['0', '0', '0', '0', '0', '0']
    column3 = ['0', '0', '0', '0', '0', '0']
    column4 = ['0', '0', '0', '0', '0', '0']
    column5 = ['0', '0', '0', '0', '0', '0']
    column6 = ['0', '0', '0', '0', '0', '0']
    column7 = ['0', '0', '0', '0', '0', '0']
    grid = [column1, column2, column3, column4, column5, column6, column7]
    # User has not won yet.
    user_win = False
    # User has not lost yet.
    user_lose = False
    # User has not placed a piece on the grid yet.
    user_pos = 'Undefined'    
    # Inital row number on the board for pieces to fall down ( 5 is the bottom, 0 is top).
    row_pos = 5  # Defualt pos is set to bottom most row
    # Build Lists to define the type of win or loss (horz, vert, diag).
    type_of_win = []
    type_of_lose = []
    # Build list to determine if board is full.
    full_board =[]


    # Game starts
    while program_flag:  # Calls to Fxns.: Prints ASCII title and board then sets game flag to True.
        display_wlcome()
        create_board(board)
        print('')  # print blankline 
        print(' Player = o | CPU = ●')  # print player peices 
        print_board(board)
        gameflag = True
        while gameflag:  # Game begins HERE
            # User picks a column.
            if user_win == False: # User didn't win prev. round, new round starts.
                user_move_flag = True 
            elif user_win == True: # User did win prev. round, game is ended.
                user_move_flag = False
                cpu_move_flag = False
                game_flag = False
                program_flag = False
                flag = True
            elif user_pos == 'Lose': # User lost prev. round, game is ended.
                user_move_flag = False
                cpu_move_flag = False
                game_flag = False
                program_flag = False
                flag = True
            else: # else, game continues, user move starts
                user_move_flag = True 
            
            # User makes a move.        
            while user_move_flag:
                row_pos = 5  # First row is 5 so bottom most.
                up_row_user = False  # Default set to assume no pieces are in placed so the user does not need to move their pieces upward.
                check_column = True  # Loop evaluates user choice to produce a final valid choice.
                while check_column:
                    user_input = ask_userchoice(
                    )  # Gets user input for column.
                    check_input = check_userchoice(
                        user_input, move_set_user
                    )  # call to fxn to check if choice is on the board.
                    user_pos = find_pos(
                        user_input
                    )  # Call to fxn to assign num based off choice.
                    if user_pos == 'Null':  # If user chose anything else but valid choice, then find_pos returns Null, so loop repeats.
                        check_column = True
                    elif user_pos == 'Quit':  # If user chose Q to quit, sets all preceding loops False
                        flag = True
                        program_flag = False
                        gameflag = False
                        up_row_user = False
                        check_column = False
                        check_user_move = False
                        user_pos = 'Quit'
                    else:  # If any other return, the loop repeats.
                        check_column = False
                # If user chose to quit, print quiting statement to acknowledge.
                if user_pos == 'Quit':
                    print('')  # print blank line
                    print(
                        'Quitting Connect 4 now...⏳')  # print quiting message
                else:  # Anything else, and game continues
                    # call to fxn to check if a piece is already in the row and pos the user chose
                    check_user_move = check_move(user_pos, grid, row_pos)
                if check_user_move == True:  # True = a piece was found in the spot.
                    up_row_user = True  # Loop to shift up the piece is True.
                elif check_user_move == 'Null':  # Null = user chose to quit game.
                    check_user_move = True  # True for next iteration, after loop repeats.
                    up_row_user = False  # Loop to shift up the piece is False.
                else:  # Anything else, user stops their move.
                    user_move_flag = False
                while up_row_user:  # Must move up row.
                    row_pos -= 1  # Subtracting moves up vertical list (column)
                    check_user_move = check_move(user_pos, grid, row_pos)
                    if row_pos < 0:  # Less than zero is out of the list/undefined.
                        print('This column is full.')
                        up_row_user = False  # Doesn't need to move up a row.
                        check_user_move = True  # True for next iteration, after loop repeats.
                        check_column = True  # User must choose a new place to move.
                    elif check_user_move == True:  # True = spot is full, must move up
                        up_row_user = True  # Loop repeats.
                    else:  # Anything else and the piece doesn't have to move upward.
                        up_row_user = False
                user_move_flag = check_user_move  # If False, means no need to move up and the user choice is complete, if True means user must repeat turn.

    # User's choice is shown on the board and added to the grid.
            if user_pos == 'Quit':  # If chose quit, CPU turn in skipped.
                cpu_move_flag = False
            else:  # Anything else, calls to function that adds the user's choice to the board and grid.
                add_player_peice(grid, user_pos, row_pos, board)
                cpu_move_flag = True  # CPU move is True            

                user_win = check_win(grid, type_of_win) # Call to fxn. checks if the user won.
                if user_win == True: # User wins
                    print_board(board) # Call to fxn. print winning board.
                    print_win_msg(user_win, type_of_win) # Call to fxn. Prints winning message
 # display the board to the user
                    cpu_move_flag = False # CPU turn is false
                    flag = True  # set flag to True (main menu)
                    program_flag = False  # set program flag to False
                    gameflag = False  # set the gameflag to False
                    up_row_user = False  # set up_row_user to False
                    check_column = False  #  set check_column to False
                    check_user_move = False  # set check_user_move to False
                else: # If not, cont. game
                    print()
                
                            

# Computer turn
            while cpu_move_flag:  # Computer move
                row_pos = 5  # First row is 5 so bottom most.
                up_row = False  # Default set to assume no pieces are in placed so the cpu does not need to move their pieces upward.
                cpu_move = get_cpumove(move_set_cpu)  # call to fxn to randomly get move
                cpu_pos = find_pos(cpu_move) # call to fxn to assign a position based on move.
                full_column = check_fullcol(grid, cpu_pos) # call to fxn, Check if the column is full 
                column_loop = full_column # if column loop is True, column in full.
                while column_loop: # repeats the prev. actions, of generating move, then check pos until valid move.
                    cpu_move = get_cpumove(move_set_cpu)
                    cpu_pos = find_pos(cpu_move)
                    full_column = check_fullcol(grid, cpu_pos)
                    column_loop = full_column
                    if column_loop == True: # Prints when the CPU finds a full column
                        print('This column is full. Choosing a new move...')
                    else:  # Else means column_loop is false, so loop ends. 
                        print()  # Changes row, prints nothing

                cpu_check = check_move(cpu_pos, grid, row_pos) # checks if the CPU piece needs to move up a row.
                if cpu_check == True: # It does need to move up a row.
                    up_row = True
                else: # it doesn't need to move up a row.
                    cpu_move_flag = False
                while up_row: 
                    row_pos -= 1 # row_pos = row_pos - 1, going up the rows.
                    cpu_check = check_move(cpu_pos, grid, row_pos) # checks if this spot is full.
                    if cpu_check == True:  # Spot full, move up a row.
                        up_row = True
                    elif row_pos < 0: # Column has ended, choose a new column.
                        # print if user does not choose valid column
                        print('This Column is full. Choosing a new move...')
                        up_row = False
                        cpu_move_flag = True
                        column_loop = True  # set
                    else:  # anything else, set given flags
                        up_row = False  # set up_row to false
                        cpu_move_flag = False  # set cpu_move_flag to false

                add_comp_peice(grid, cpu_pos, row_pos, board) # Add the final CPU piece to the board.
                user_lose = check_lose(grid, type_of_lose) # Check if the CPU won/ user lost.
                if user_lose == True: # User lost.
                    print_board(board) # print board
                    print_lose_msg(user_lose, type_of_lose) # print lose msg.
                    flag = True # goes back to starting menu.
                    program_flag = False  ## All other loops are set to false
                    gameflag = False
                    up_row_user = False
                    check_column = False
                    check_user_move = False
                else: #Else, continue game.
                    print()
            # User quit the game
            if user_pos == 'Quit' or user_choice == 'Q' or user_choice == 'q': # Game ends and prints goodbye message.
                print('')
                print('Please Play Again Soon!')
                print('')
            # User won the game.
            elif user_win == True:
                print()
                print('Game over')
                print()
            # CPU won the game.
            elif user_lose == True:
                print()
                print('Game over')
                print()
            # Continue the game    
            else:  # Computer's choice is shown on the board and added to the grid.
                add_comp_peice(grid, cpu_pos, row_pos, board)
                print_board(board)
                
                
                # Checks each row for 0 (empty spaces)
                for row in range(0,7):
                    if ('0' in grid[row]) == False:
                        full_board.append('x') # add a tally to the list if there is no empty spaces in row.is
                    else:
                        full_board.clear() # If else, clear the list

                if len(full_board) == 7: # if seven tallies, full board is full.
                    flag = True # goes back to starting menu.
                    program_flag = False  ## All other loops are set to false
                    gameflag = False
                    up_row_user = False
                    check_column = False
                    check_user_move = False  
                    full_board.clear()  
                else:
                    full_board.clear()    # if else clear the list.        
                    
