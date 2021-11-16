def display_board(board):
    # MAKE A GAME TABLE.
   
    print('   |    |')
    print(' '+board[7]+' | '+board[8]+'  | '+board[9])
    print('   |    |')
    print('------------')
    print('   |    |')
    print(' '+board[4]+' | '+board[5]+'  | '+board[6])
    print('   |    |')
    print('------------')
    print('   |    |')
    print(' '+board[1]+' | '+board[2]+'  | '+board[3])
    print('   |    |')
test_bord=['#','X','O','X','O','X','O','X','O','X'] #DEFINE A TWO VALUES ,THAT PUT IN GAME.  

def player_input():    #TAKE A PLAYER INPUT AND ASKED TO PLAYER CHOOSE .
    marker=''
    while not (marker=='X' or marker=='O'):
        marker=input('Player 1: Do you want to be x or o ?').upper()
    if marker=='X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board,marker,position):    #TAKE A POSSITION IN TABLE.
    board[position]=marker

def win_check(board,mark):       # MAKE A FUNCTION TO PUT VALUE IN TABLE . 
    return ((board[7]==mark and board[8]==mark and board[9]==mark) or
    (board[4]==mark and board[5]==mark and board[6]==mark) or
    (board[1]==mark and board[2]==mark and board[3]==mark) or
    (board[7]==mark and board[4]==mark and board[1]==mark) or
    (board[8]==mark and board[5]==mark and board[2]==mark) or
    (board[9]==mark and board[6]==mark and board[3]==mark) or
    (board[7]==mark and board[5]==mark and board[3]==mark) or
    (board[9]==mark and board[5]==mark and board[1]==mark))

import random                # CHOOSE RANDOM PLAYER.
def choose_first():
    if random.randint(0,1)==0:
        return 'player 2'
    else:
        return 'player 1'


def space_check(board,position):  #CHECK SPACE IN TABLE .
    return board[position]==' ' 

def full_board_check(board):      # CHECK POSSITION IN TABLE FILL OR BLANK .
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):   #  TAKE INPUT METHOD BY NUMBER .
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
         position=int(input('Choose your next position: (1-9)'))
    return position

def replay():               # ASK TO PLAYER IF WANT TO REPLAY .
    return input('Do you want to play again? Enter Yes or No :').lower().startswith('y')

print('Welcome to Tic Toe !')          # START GAME .
while True:
    theBoard =[' ']*10                  
    player1_marker,player2_marker=player_input()
    turn= choose_first()
    print(turn + 'Will go First .')

    play_game=input('Are you ready to play? Enter Yes or No .')
    
    if play_game.lower()[0]=='y':
        game_on=True
    else:
        game_on=False
    while game_on:
        if turn=='player 1':
            display_board(theBoard)
            position=player_choice(theBoard)
            place_marker(theBoard,player1_marker,position)

            if win_check(theBoard,player1_marker):
                display_board(theBoard)
                print('Congratulation ! you have won the game !')
                game_on=False
            else:
                if full_board_check(theBoard):
                   display_board(theBoard)
                   print('The game is Draw !')
                   break
                else:
                    turn='player 2'
        else:
            display_board(theBoard)
            position=player_choice(theBoard)
            place_marker(theBoard,player2_marker,position)

            if win_check(theBoard,player2_marker):
                display_board(theBoard)
                print('player 2 has won !')
                game_on=False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a Draw !')
                    break
                else:
                    turn='player 1'
    if not replay():
        break                                
