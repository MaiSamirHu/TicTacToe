import random
board=[" " for x in range(10)]

#assign value on position
def assignValue(letter,pos):
    board[pos]=letter

#checks weather that particular space is available on board or not
def space_In_Board(pos):
    return board[pos]==" "


#prints the board
def printBoard(board):
    print("   |   |   ")
    print(" "+ board[1]+" | "+ board[2]+" | "+board[3])
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" "+ board[4]+" | "+ board[5]+" | "+board[6])

    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" "+ board[7]+" | "+ board[8]+" | "+board[9])
    print("   |   |   ")
#checks weather board is full or not
def boardFull(board):
    if board.count(" ")>1:
        return False
    else :
        return True


#checks the computer or player is winner or not
def winner(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))

def playerMove():
    run=True
    while run:
        move=int(input("Enter the position between 1-9 :"))
        try:
            if move>0 and move<10:
                
                if space_In_Board(move):
                    run=False
                    assignValue("X",move)
                else:
                    print("Sorry,That position is occupied")
        except:
                print("please enter the number instead of other character")
                
            
def computerMove():
    possibleMoves=[x for x,letter in enumerate(board) if letter==" " and x!=0]
    move=0
    
    for let in["X","O"]:
        for i in possibleMoves:
            boardCopy=board[:] 
            boardCopy[i]=let

            if winner(boardCopy,let):
                move=i
                return move

    cornerMoves=[]
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornerMoves.append(i)
    if len(cornerMoves)>0:        
        move=selectRandom(cornerMoves)  
        return move

    if 5 in possibleMoves:
        move=5
        return move
    
    edgeMoves=[]
    for i in possibleMoves:
        if i in[2,4,6,8]:
            edgeMoves.append(i)
    if len(edgeMoves)>0:
        move=selectRandom(edgeMoves)
        return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]


def main():
    print("***************\nTIC TAC TOE\n***************\n")
    printBoard(board)
    while not(boardFull(board)):
        if not(winner(board,"O")):
            playerMove()
            printBoard(board)
        else:
            print("sorry you lose!!!")
            break

        if not(winner(board,"X")):
            move=computerMove()
            if boardFull(board):
                print("tie game")
            else:
                assignValue("O",move)
                print(f"computer played on position {move}  ")
                printBoard(board)

        else :
            print("you win!!!")
            break

main()    
while True:
    x=input("want to play (y/n) :")
    if x.lower()=="y":
        board=[" " for x in range(10)]
        main()
    else:
        break



    





