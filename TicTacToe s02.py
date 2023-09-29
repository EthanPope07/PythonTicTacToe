# Tic Tac Toe problem
#
# History
# s01 basic structure
# s02 2 player
# TODO: Use Turtle graphics 

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

        userMove=getMove(board,player2)
        board[userMove-1]="O"
        win=checkForWin(board,"O")
        if win  == "Win":
            print ("Congradulations "+player2+" you won!!! ")
            break

            
# User done?
    doneQ = input("done playing, enter q to quit: ") #TODO: Validate input
    if (doneQ == "q") :
        moreGames = False

        

        
