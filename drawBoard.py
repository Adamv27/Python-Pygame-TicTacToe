import pygame

#constants
WIDTH = 500
HEIGHT = 500

#colors
BLACK = (0,0,0)
WHITE = (255,255,255)
GREY = (96,96,96)
GREYL = (128,128,128)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
def drawBoard():
     #grey main box
    pygame.draw.rect(screen,(GREY),(10,10,480,480))

    #inside boxes
    BOX_WIDTH = 144
    BOX_HEIGHT = 144


    rowOneX = 20
    rowOneY = 20
    rowTwoX = 20
    rowTwoY = 178
    rowThreeX = 20
    rowThreeY = 336
    for i in range(3):
        pygame.draw.rect(screen, (GREYL), (rowOneX, rowOneY, BOX_WIDTH, BOX_HEIGHT))
        rowOneX += 158
    for i in range(3):
        pygame.draw.rect(screen, (GREYL), (rowTwoX, rowTwoY, BOX_WIDTH, BOX_HEIGHT))
        rowTwoX += 158
    for i in range(3):
        pygame.draw.rect(screen, (GREYL), (rowThreeX, rowThreeY, BOX_WIDTH, BOX_HEIGHT))
        rowThreeX += 158
         

