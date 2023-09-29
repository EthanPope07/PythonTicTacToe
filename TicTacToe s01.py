# Tic Tac Toe problem
#
# History
# s01 basic structure
# TODO: Use Turtle graphics 

def printBoard(board):
    #TODO: improve board display
    print(str(board[0])+"|"+str(board[1])+"|"+str(board[2]))
    print("-----")
    print(str(board[3])+"|"+str(board[4])+"|"+str(board[5]))
    print("-----")
    print(str(board[6])+"|"+str(board[7])+"|"+str(board[8]))

# Set up
board=[1,2,3,4,5,6,7,8,9]

# Loop until user done playing
moreGames=True
while moreGames :




# loop on moves until game none or draw
    gameDone=False
    while gameDone==False :

        printBoard(board)
        #TODO Validate Input
        userMove=input("enter your move: ")
        userMove=int(userMove)
        board[userMove-1]="X"
        printBoard(board)

        userMove=input("enter computer move: ")
        userMove=int(userMove)
        board[userMove-1]="O"      


        gameStatus= input("TODO: Game done yes? ")
        if (gameStatus== "y") :
            gameDone = True
            
# User done?
    doneQ = input("done playing, enter q to quit: ") #TODO: Validate input
    if (doneQ == "q") :
        moreGames = False

        

        
