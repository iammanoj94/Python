board = ["  " for i in range(9)]
P1 = input("Enter Player1 Name : ")
P2 = input("Enter Player 2 Name : ")
def player_move(icon):
    if icon == "X":
        number = 1
        print(f"Player {P1}, its your Turn!!")
    elif icon == "O":
        number = 2
        print(f"Player {P2}, its your Turn!!")
    
    choice = int(input("enter your box number between 1-9 :").strip())
    if choice not in range(9):
        print("you have entered invalid number range")
        player_move(icon)
        
    elif board[choice - 1] == "  ":
        board[choice - 1] = icon
    else:
        print()
        print(" This Space is already taken")
        player_move(icon)
         

def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False
def is_draw():
    if "  " not in board:
        return True
    else:
        return False

def print_board():
    row1 = f"| {board[0]} | {board[1]} | {board[2]} |"
    row2 = f"| {board[3]} | {board[4]} | {board[5]} |"
    row3 = f"| {board[6]} | {board[7]} | {board[8]} |"
    print()
    print("="* 8 + "Tic Tac Toe" + "="*8)
    print(row1)
    print(row2)
    print(row3)
    print("="* 8 + "Tic Tac Toe" + "="*8)
    print()

while True:
    print_board()
    player_move("X")
    if is_victory("X"):
        print(f"Congractulations {P1}!!!!! YOU WON THE MATCH ")
        print_board()
        break
    elif is_draw():
        print("Its a Draw")
        break
    print_board()
    player_move("O")
    if is_victory("O"):
        print(f"Congractulations {P2}!!!!! YOU WON THE MATCH ")
        print_board()
        break
    elif is_draw():
        print("Its a Draw")
        break
    
    

