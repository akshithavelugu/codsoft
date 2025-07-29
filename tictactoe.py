import math
board=[' ' for _ in range(9)]
def print_board():
    for i in range(3):
        print('|'.join(board[i*3:(i+1)*3]))
        if i<2:
            print('-'*5)
def check_winner(b,player):
    win_patterns=[(0,1,2),(3,4,5),(6,7,8),
                  (0,3,6),(1,4,7),(2,5,8),
                  (0,4,8),(2,4,6)
                  ]
    return any(b[i]==b[j]==b[k]==player for i,j,k in win_patterns)
def minimax(b,depth,is_maximizing):
        if check_winner(b,'0'):
            return 1
        if check_winner(b,'X'):
            return -1
        if ' ' not in b: 
            return 0
        if is_maximizing:
            best_score=-math.inf
            for i in range(9):
                if b[i]==' ':
                    b[i]='0'
                    score=minimax(b,depth+1,False)
                    b[i]=' '
                    best_score=max(score,best_score)
            return best_score
        else:
            best_score=math.inf
            for i in range(9):
                if b[i]==' ':
                    b[i]='X'
                    score=minimax(b,depth+1,True)
                    b[i]=' '
                    best_score=min(score,best_score)
            return best_score
def best_move(b):
    best_score=-math.inf
    move=None
    for i in range(9):
        if b[i]==' ':
            b[i]='0'
            score=minimax(board,0,False)
            board[i]=' '
            if score>best_score:
                best_score=score
                move=i
    return move 
def play():
    current_player='X'
    print_board()
    while True:
        if check_winner(board,'0'):
            print("AI wins!")
            break
        if check_winner(board,'X'):
            print("You win!")
            break   
        if ' ' not in board:
            print("It's a draw!")
            break   
        if current_player=='X':
            try:
                user_move=int(input("Enter your move(0-8): "))
                if 0<=user_move<9 and board[user_move]==' ':
                    board[user_move]='X'
                    current_player='0'
                else:
                    print("Invalid move, try again.")
            except ValueError:
                print("Please enter a valid number between 0 and 8.")   
        else:
            print("AI is making a move...")
            ai_move=best_move(board)
            if ai_move is not None:
                board[ai_move]='0'
                current_player='X'
                print(f"AI placed '0' at position {ai_move}.")
            else:
                print("No valid moves left for AI.")
if __name__ == "__main__":
    play()
    print_board()
    print("Game Over!")
