# Tic Tac Toe problem
#
# History
# s01 basic structure
# s02 2 player
# s03 easy
# TODO: Use Turtle graphics
import random
import turtle

def printBoard(board):
    #TODO: improve board display
    print(str(board[0])+"|"+str(board[1])+"|"+str(board[2]))
    print("-----")
    print(str(board[3])+"|"+str(board[4])+"|"+str(board[5]))
    print("-----")
    print(str(board[6])+"|"+str(board[7])+"|"+str(board[8]))

def checkForWin (board, who):
    result="Continue"
    if ((board[0]==board[1]==board[2]==who) or \
        (board[3]==board[4]==board[5]==who) or \
        (board[6]==board[7]==board[8]==who) or \
        (board[0]==board[3]==board[6]==who) or \
        (board[1]==board[4]==board[7]==who) or \
        (board[5]==board[2]==board[8]==who) or \
        (board[2]==board[4]==board[6]==who) or \
        (board[0]==board[4]==board[8]==who)):
        result = "Win"
    return (result)

def getMove(board,player):
    goodMove=False
    while goodMove==False:
        #TODO Validate Input
        userMove=input(player+" enter your move: ")
        userMove=int(userMove)
        if board[userMove-1]==userMove:
            goodMove=True
        else:
            print("No no no you can't overlay a move")
    return userMove

def getEasyMove(board,player):
    goodMove=False
    while goodMove==False:
        #TODO Validate Input
        userMove=random.randint(1,9)
        userMove=int(userMove)
        if board[userMove-1]==userMove:
            goodMove=True
    return userMove
    
    

# Main Program starts
#TODO: Validate input
mode= input("do you want to play two player(2) or easy(e) or hard(h) against the computer: ")
if mode=="2":
    player1=input("Enter player one's name: ")
    player2=input("Enter player two's name: ")
else:
    player1=input("Enter your name: ")
    player2="computer"
# Set up


# Loop until user done playing
moreGames=True
while moreGames :

    board=[1,2,3,4,5,6,7,8,9]



# loop on moves until game none or draw
    gameDone=False
    while gameDone==False :

        

        printBoard(board)
        #TODO Validate Input
        userMove=getMove(board,player1)
        board[userMove-1]="X"
        printBoard(board)
        win=checkForWin(board,"X")
        if win  == "Win":
            print ("Congradulations "+player1+" you won!!! ")
            break

        if (mode == "2") :
            userMove=getMove(board,player2)
            board[userMove-1]="O"
            win=checkForWin(board,"O")
            if win  == "Win":
                print ("Congradulations "+player2+" you won!!! ")
                break
        elif (mode == "e") :
            userMove=getEasyMove(board,player2)
            print("the computer's move is "+str(userMove))
            board[userMove-1]="O"
            win=checkForWin(board,"O")
            if win  == "Win":
                print ("Congradulations "+player2+" you won!!! ")
                break
            
        elif (mode == "h") :
            print ("TODO have not done hard yet")
            break
        else :
            print ("panic: should never get here")
            break

            
# User done?
    doneQ = input("done playing, enter q to quit: ") #TODO: Validate input
    if (doneQ == "q") :
        moreGames = False

        

        
