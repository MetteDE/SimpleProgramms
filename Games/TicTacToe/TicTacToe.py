from colored import fg, bg, attr
reset = attr('reset')

from glob import glob



color_x = fg('#C41E3A')
color_o = fg('#336BFF')


board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
player_1 = color_x + "X" + reset
player_2 = color_o + "O" + reset
player = "player1"
board_is_full = False
winner = None

def draw_board():
    print('┌───┬───┬───┐')
    print(f'│ {board[0]} │ {board[1]} │ {board[2]} │')
    print('├───┼───┼───┤')
    print(f'│ {board[3]} │ {board[4]} │ {board[5]} │')
    print('├───┼───┼───┤')
    print(f'│ {board[6]} │ {board[7]} │ {board[8]} │')
    print('└───┴───┴───┘')


def take_input():
    if player == "player1":
        position = int(input("Player 1 (X) where do you wanna start?(1-9) -> "))
        position = position - 1
        valid_move(position)
    elif player == "player2":
        position = int(input("Spieler 2 (O) where do you wanna start?(1-9) -> "))
        position = position - 1 
        valid_move(position)




def valid_move(position):
    if position < 0 or position > 8:
        print("Please select a box inside the field!")
        take_input()
    elif board[position] != " ": 
        print("This box is already in use. Try again!")
        take_input()
    else: 
        if player == "player1":
            place_X(position)
        elif player == "player2":
            place_O(position)


def place_X(position):
    board[position] = player_1

def place_O(position):
    board[position] = player_2

def check_if_board_is_full():
    global board_is_full
    if " " not in board:
        board_is_full = True
    else:
        board_is_full = False

def switching_players():
    global player 
    if player == "player1":
        player = "player2"
    elif player == "player2":
        player = "player1"


def check_for_win():
    global winner
    
    if player_1 == board[0] == board[1] == board[2]:
        winner = player_1
    elif player_1 == board[3] == board[4] == board[5]:
        winner = player_1
    elif player_1 == board[6] == board[7] == board[8]:
        winner = player_1

    elif player_1 == board[0] == board[3] == board[6]:
        winner = player_1
    elif player_1 == board[1] == board[4] == board[7]:
        winner = player_1
    elif player_1 == board[2] == board[5] == board[8]:
        winner = player_1
    elif player_1 == board[0] == board[4] == board[8]:
        winner = player_1
    elif player_1 == board[2] == board[4] == board[6]:
        winner = player_1

    # Check for O winner
    if player_2 == board[0] == board[1] == board[2]:
        winner = player_2
    elif player_2 == board[3] == board[4] == board[5]:
        winner = player_2
    elif player_2 == board[6] == board[7] == board[8]:
        winner = player_2

    elif player_2 == board[0] == board[3] == board[6]:
        winner = player_2
    elif player_2 == board[1] == board[4] == board[7]:
        winner = player_2
    elif player_2 == board[2] == board[5] == board[8]:
        winner = player_2
    elif player_2 == board[0] == board[4] == board[8]:
        winner = player_2
    elif player_2 == board[2] == board[4] == board[6]:
        winner = player_2




print("Welcome to this TicTacToe game.")
print("Enjoy!")
print("This is the board ->")
print('┌───┬───┬───┐')
print('│ 1 │ 2 │ 3 │')
print('├───┼───┼───┤')
print('│ 4 │ 5 │ 6 │')
print('├───┼───┼───┤')
print('│ 7 │ 8 │ 9 │')
print('└───┴───┴───┘')

print('To start just chose a box to put your sign in.')
i = 0
while not board_is_full:
        draw_board()
        i += 1 
        check_if_board_is_full()
        check_for_win()
        if winner == player_1 or winner == player_2:
            break
        if board_is_full:
            break
        take_input()
        draw_board()
        check_if_board_is_full()
        check_for_win()
        if winner == player_1 or winner == player_2:
            break
        if board_is_full:
            break
        switching_players()
        take_input()
        check_if_board_is_full()
        check_for_win()
        if winner == player_1 or winner == player_2:
            break
        if board_is_full:
            break
        switching_players()


if winner == player_1:
    draw_board()
    print("Player 1 won!")
elif winner == player_2:
    draw_board()
    print("Player 2 won!")
else:
    draw_board()
    print("It's a tie!")
print("The game ended! Go for another round!")