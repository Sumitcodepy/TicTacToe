import random


board = [
    0,0,0,
    0,0,0,
    0,0,0
]

def print_board() :
    display_position = ['_','_','_','_','_','_','_','_','_']
    
    for i in range(9) :
       if board[i] == 1 :
           display_position[i] = "X"
    
       elif board[i] == 2 :
           display_position[i] = "O"

    print('''_____________
| {} | {} | {} |
|---|---|---|
| {} | {} | {} |
|---|---|---|
| {} | {} | {} |
_____________


'''.format(*display_position))
    

def check_win(num) :
    if board[0] == board[1] == board[2] == num :
       return True
    elif board[3] == board[4]  == board[5] == num :
        return True
    
    elif board[6] == board[7] == board[8] == num :
        return True
    
    elif board[0] == board[3] == board[6] == num :
        return True
    
    elif board[1] == board[4] == board[7] == num :
        return True
    
    elif board[2] == board[5] == board[8] == num :
        return True
    
    elif board[0] == board[4] == board[8] == num :
        return True
    elif board[2] == board[4] == board[6] == num :
        return True
    
    else :
        return False
    
    
print("**************TIC TAC TOE**************")
name = input("Enter your name :")
print("")
print(f"Hi {name} , before we start the game choose your sign :")
print('''FOR X : press 1
FOR O : press 2 ''')

choice = int(input("Enter : "))

print("Note the position of matrix :")
print('''_____________
| 0 | 1 | 2 |
|---|---|---|
| 3 | 4 | 5 |
|---|---|---|
| 6 | 7 | 8 |
_____________''')


turn = 0
pos = [0,1,2,3,4,5,6,7,8]
pos_1_col = []

while turn < 9 :
    pos_1 = int(input("Enter the position no. you want to occupy :"))


    while not board[pos_1] == 0 :
        print("This position is already occupied , choose different position ")
        pos_1 = int(input("Enter :")) 

    if board[pos_1] == 0 : 
        board[pos_1] = choice
        pos_1_col.append(pos_1)
        print_board()
    
    


    a = check_win(choice)
    if a == True :
        print("You win")
        break
    
    turn = turn + 1
    print("Computer's move")

    pos_cond = [n for n in range(0,9)  if n not in pos_1_col]
    pos_2 = random.choice(pos_cond)
    while not board[pos_2] == 0 :
        pos_2 = random.choice(pos_cond)

    if board[pos_2] == 0 : 
       if choice == 1 : 
        board[pos_2] = 2
        b = 2
        print_board()
       elif choice == 2 :
        board[pos_2] = 1
        b = 1
        print_board()

    c = check_win(b)
    if c == True :
        print("Computer Wins")
        break   
    
    

if turn == 9 :
    print("Draw")
    print("Come Again")

    