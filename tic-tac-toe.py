#Tic tac toe game excercise with Python
#programed by David Cui
    #Inspired by TechwithTim
#Completed: 6/26/2023

#Tic Tac Toe
    #The game is inside of a 3x3 matrix
    #the game as one player and one bot
    #goal is to achieve 3 of the same tiles horizontally, diagonally, and vertically

#Create the board
board = [" " for x in range(10)]


def insertLetter(letter, pos):
    board[pos] = letter

def isSpaceFree(pos):
    return board[pos] == " "

def printBoard():
    print("   |   |")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |")
    

def winner(bo, le):
    #3 different kinds of winners: Diagonal, Horizontal, and Vertical
    return (bo[1] == le and bo[2] == le and bo[3] == le) or\
        (bo[4] == le and bo[5] == le and bo[6] == le) or\
        (bo[7] == le and bo[8] == le and bo[9] == le) or\
        (bo[1] == le and bo[4] == le and bo[7] == le) or\
        (bo[2] == le and bo[5] == le and bo[8] == le) or\
        (bo[3] == le and bo[6] == le and bo[9] == le) or\
        (bo[1] == le and bo[5] == le and bo[9] == le) or\
        (bo[3] == le and bo[5] == le and bo[7] == le)

def playerMove():
    run = True
    while run:
        move = input("Please select a position to place an 'X' (1-9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if isSpaceFree(move):
                    run = False
                    insertLetter("X", move)
                else:
                    print("The position chosen does not have space")
            else:
                print("Please type a valid position on the board.")
        except:
            print("Please type a number")

def computerMove():
    #THE AI will
        #take the winning move if present
        #if the player has a possible winning move on their next turn, move into that position
        #Take any one of the corners. If more than one, randomly pick
        #Take the center position
        #Take one of the edges. If more than one, randomly pick
        #IF no possible move is availble, the game is a tie
    possibleMoves = [x for x, letter in enumerate(board) if letter == " " and x != 0] 
        #This will create a list of possible moves
    move = 0
    
    #check for possible winning moves to take or block opponents winning move
    for letter in ["O", "X"]:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = letter
            if winner(boardCopy, letter):
                move = i
                return move
    
    #Try to take one of the corners
    openCorners = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            openCorners.append(i)
    if len(openCorners) > 0:
        move = selectRandom(openCorners)
        return move
    
    #Try to take the center
    if 5 in possibleMoves:
        move = 5
        return move
    
    #Take any edges
    openEdges = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            openEdges.append(i)
    if len(openEdges) > 0:
        move = selectRandom(openEdges)
    
    return move   

def selectRandom(li):
    import random
    length = len(li)
    r = random.randrange(0, length)
    return li[r]

def isBoardFull(board):
    if board.count(" ") > 1:
        return False
    else:
        return True

def main():
    print("Welcome to Tic-Tac-Toe! The board has positions 1-9 starting at the top left")
    printBoard()
    
    while not(isBoardFull(board)):
        if not(winner(board, "O")):
            playerMove()
            printBoard()
        else:
            print("'O' won this time...")
            break
        
        if not(winner(board, "X")):
            move = computerMove()
            if move == 0:
                print("Game is a Tie! No more spaces left to move.")
            else:
                insertLetter("O", move)
                print("Computer placed an 'O' in position", move , ":")
                printBoard()
        else:
            print("'X' wins, noice job :)")
            break
        
    if isBoardFull(board):
        print("Game is a tie. Good Try")
        
while True:
    answer = input("Lets play one more round. (Y/N)")
    if answer.lower() == 'y' or answer.lower() == "yes":
        board = [" " for x in range(10)]
        print("-----------------------------------")
        main()
    else:
        break
