import pygame
import sys
import random
import drawBoard
import time

pygame.init()

#constants
WIDTH = 500
HEIGHT = 500

#colors
BLACK = (0,0,0)
WHITE = (255,255,255)
PURPLE = (138,43,226)
GREEN = (127,255,0)
GREY = (96,96,96)
GREYL = (128,128,128)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def displayMove(turn, space):
    # centers of each box for the circles
    oCords = [(92,92), (250,92), (408,92), (92,250), (250,250), (408,250), (92,408), (250,408), (408,408)]

    # corners and the middle of each box for the x's
    xCords = [((24,24),(160,160),(92,92),(24,160),(160,24)),
              ((182,24),(318,160),(250,92),(182,160),(318,24)),
              ((340,24),(476,160),(408,92),(340,160),(476,24)),
              ((24,182),(160,318),(92,250),(24,318),(160,182)),
              ((182,182),(318,318),(250,250),(182,318),(318,182)),
              ((340,182),(476,318),(408,250),(340,318),(476,182)),
              ((24,340),(160,476),(92,408),(24,476),(160,340)),
              ((182,340),(318,476),(250,408),(182,476),(318,340)),
              ((340,340),(476,476),(408,408),(340,476),(476,340))]
                                                             
    if turn == 'computer':
        pygame.draw.circle(screen, GREEN, (oCords[space]), 60, 3)
        pygame.display.update()
        print('drawn!')

    elif turn == 'player':
        pygame.draw.lines(screen, PURPLE, False, (xCords[space]), 5)
        pygame.display.update()
        print('draw')

def updateBoard(board, boardCopy):
    print('updating board')
    for i in range(9):
        if boardCopy[i] != board[i]:
            displayMove('computer',i)

def getPlayerMove(board):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                if event.button == 1:
                    for area in areas:
                        if areas[area].collidepoint(event.pos):
                            playerMove = area[4:]
                            if playerMove in board:
                                board[int(playerMove)] = 'X'
                                displayMove('player', int(playerMove))
                                return board

def winState(board):
    #horizontal
    if list(board[i] for i in [0,1,2]) == ['X','X','X'] or list(board[i] for i in [0,1,2]) == ['O','O','O']:
        return 'win'
    if list(board[i] for i in [3,4,5]) == ['X','X','X'] or list(board[i] for i in [3,4,5]) == ['O','O','O']:
        return 'win'
    if list(board[i] for i in [6,7,8]) == ['X','X','X'] or list(board[i] for i in [6,7,8]) == ['O','O','O']:
        return 'win'

    #vertical
    if list(board[i] for i in [0,3,6]) == ['X','X','X'] or list(board[i] for i in [0,3,6]) == ['O','O','O']:
        return 'win'
    if list(board[i] for i in [1,4,7]) == ['X','X','X'] or list(board[i] for i in [1,4,7]) == ['O','O','O']:
        return 'win'
    if list(board[i] for i in [2,5,8]) == ['X','X','X'] or list(board[i] for i in [2,5,8]) == ['O','O','O']:
        return 'win'

    #diagonal
    if list(board[i] for i in [0,4,8]) == ['X','X','X'] or list(board[i] for i in [0,4,8]) == ['O','O','O']:
        return 'win'
    if list(board[i] for i in [2,4,6]) == ['X','X','X'] or list(board[i] for i in [2,4,6]) == ['O','O','O']:
        return 'win'

# if there are no more moves then it is a draw
def drawState(board):
    num = ['0','1','2','3','4','5','6','7','8']
    count = 0
    for i in num:
        if i not in board:
            count += 1
    if count == 9:
        return 'draw'

# makes a copy of the board based on the current board
def copyBoard(board):
    boardCopy = []
    for space in board:
        boardCopy.append(space)
    return boardCopy

# simulates playing a move on a copy of the board
def simMove(boardCopy, move, cChar):
    boardCopy[int(move)] = cChar
    return boardCopy

def winningMove(board, cChar):
    # check all moves
    for move in board:
        if move != 'X' and move != 'O':
            # if there is a winning move take it
            if winState(simMove(copyBoard(board), move, cChar)) == 'win':
                return move
    return False

def getComputerMove(board, cChar, pChar, turn):
    corners = [0, 2, 6, 8]
    edges = [1,3,5,7]
    
    # if first turn play in a random corner
    if turn == 0:
        move = random.choice(corners)
        board[move] = cChar
        return board

    # play in opposite corner from the one played
    # if its blocked then play in a different one
    elif turn == 1:
        for i in corners:
            if board[i] == cChar:
                if i == 8:
                    if board[0] == '0':
                        board[0] = cChar
                        return board
                    else:
                        board[6] = cChar
                        return board

                elif i == 6:
                    if board[2] == '2':
                        board[2] = cChar
                        return board
                    else:
                        board[8] = cChar
                        return board
                        
                elif i == 2:
                    if board[6] == '6':
                        board[6] = cChar
                        return board
                    else:
                        board[8] = cChar
                        return board
                        
                elif i == 0:
                    if board[8] == '8':
                        board[8] = cChar
                        return board
                    else:
                        board[2] = cChar
                        return board

    elif turn == 2:
        # play a winning move
        if (winningMove(board, cChar)) != False:
            board[int(winningMove(board, cChar))] = cChar
            return board

        # else if the player has a winning move then block it
        elif (winningMove(board, pChar)) != False:
            board[int(winningMove(board, pChar))] = cChar
            return board
        
        # go through all corners and play on an open one
        else:
            for i in corners:
                if board[i] != pChar and board[i] != cChar:
                    board[i] = cChar
                    return board

    elif turn >= 3:
        # if there is a winning move then play it
        if (winningMove(board, cChar)) != False:
            board[int(winningMove(board, cChar))] = cChar
            return board

        # else if the player has a winning move then block it
        elif (winningMove(board, pChar)) != False:
            board[int(winningMove(board, pChar))] = cChar
            return board
        
        else:
            # random move 
            for move in board:
                if move != 'X' and move != 'O':
                    board[int(move)] = cChar
                    return board  
     
    else:
        # random move 
        for move in board:
            if move != 'X' and move != 'O':
                board[int(move)] = cChar
                return board
    
#main game loop

areas = {'area0': pygame.Rect(20, 20, 144, 144), 'area1': pygame.Rect(178, 20, 144, 144), 'area2': pygame.Rect(336, 20, 144, 144), 'area3': pygame.Rect(20, 178, 144, 144), 'area4': pygame.Rect(178, 178, 144, 144), 'area5': pygame.Rect(336, 178, 144, 144), 'area6': pygame.Rect(20, 336, 144, 144), 'area7': pygame.Rect(178, 336, 144, 144), 'area8': pygame.Rect(336, 336, 144, 144)}
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #draw the board
    drawBoard.drawBoard()
    pygame.display.update()

    boardCopy = ['0','1','2',
         '3','4','5',
         '6','7','8']
    
    board = ['0','1','2',
         '3','4','5',
         '6','7','8']
    
    pChar = 'X'
    cChar = 'O'

    turn = 0
    
    while True:
        getComputerMove(board, cChar, pChar, turn)

        updateBoard(board, boardCopy)

        boardCopy = []
        for space in board:
            boardCopy.append(space)
            
        time.sleep(1)
        turn += 1   
        if winState(board) == 'win':
            print('computer win')         
            pygame.display.update()
            sys.exit()           
        elif drawState(board) == 'draw':
            print('computer tie')
            pygame.display.update()
            sys.exit()
            
        getPlayerMove(board)
        boardCopy = []
        for space in board:
            boardCopy.append(space)
        if drawState(board) == 'draw':
            print('player tie')
            sys.exit()            
        time.sleep(1)

        
            
