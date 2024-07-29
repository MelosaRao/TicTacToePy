import sys, pygame
import numpy as np
pygame.init()


WIDTH = 600
HEIGHT = 600
TRACK_SIZE = 200
BACKGROUD_COLOR=(31,41,55)
WHITE = (255, 255, 255)
YELLOW = (255,255,0)
FIGURE_WIDTH = 15
GREEN = (162,228,184)
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BACKGROUD_COLOR)
board = np.zeros((3,3))
player = 1
gameOver = False
#draw required lines
def draw_grid():
    pygame.draw.line(screen, WHITE, (0,200),(600,200), 10)
    pygame.draw.line(screen, WHITE, (0,400),(600,400), 10)
    pygame.draw.line(screen, WHITE, (200,0),(200,600), 10)
    pygame.draw.line(screen, WHITE, (400,0),(400,600), 10)
draw_grid()

def draw_figure(color = WHITE):
    for row in range(3):
        for col in range(3):
            if(board[row][col])==2:
                pygame.draw.circle(screen,YELLOW,(int(row*TRACK_SIZE+TRACK_SIZE/2), int(col*TRACK_SIZE+TRACK_SIZE/2)),TRACK_SIZE/3,10)
            elif(board[row][col])==1:
                pygame.draw.line(screen,GREEN,(int(row*TRACK_SIZE+ TRACK_SIZE//4),int(col*TRACK_SIZE+ TRACK_SIZE//4)), (int(row*TRACK_SIZE+ 3*TRACK_SIZE//4),int(col*TRACK_SIZE+ 3*TRACK_SIZE//4)),FIGURE_WIDTH)
                pygame.draw.line(screen,GREEN,(int(row*TRACK_SIZE+ TRACK_SIZE//4),int(col*TRACK_SIZE+ 3*TRACK_SIZE//4)), (int(row*TRACK_SIZE+ 3*TRACK_SIZE//4),int(col*TRACK_SIZE+ TRACK_SIZE//4)),FIGURE_WIDTH)

def valid_move(row,col):
    if(board[row][col]==0):
        return True
    return False
def update_boord(row,col,player):
    board[row][col] = player
    draw_figure()

def boord_complete(row,col):
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                return False
    return True

def check_win(player):
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_horizontal_winline(col,player)
            return True
    for row in range(3):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_vertical_winline(row,player)
            return True
        
    if board[0][0]==player and board[1][1]==player and board[2][2]==player:
        draw_up_diagonal_winline(player)
        return True
    if board[2][0]==player and board[1][1]==player and board[0][2]==player:
        draw_down_diagonal_winline(player)
        return True
    return False

def draw_vertical_winline(col, player):
    win_color = GREEN
    if(player==2):
         win_color = YELLOW
    pygame.draw.line(screen, win_color, (col*TRACK_SIZE+TRACK_SIZE//2, 15), (col*TRACK_SIZE+TRACK_SIZE//2, 600-15),10)
def draw_horizontal_winline(row,player):
    win_color = GREEN
    if(player==2):
         win_color = YELLOW
    pygame.draw.line(screen, win_color, (15, row*TRACK_SIZE+TRACK_SIZE//2), (600-15, row*TRACK_SIZE+TRACK_SIZE//2),10)
def draw_up_diagonal_winline(player):
    win_color = GREEN
    if(player==2):
         win_color = YELLOW
    pygame.draw.line(screen,win_color,(15,15),(600-15,600-15),10)
def draw_down_diagonal_winline(player):
    win_color = GREEN
    if(player==2):
         win_color = YELLOW
    pygame.draw.line(screen,win_color,(15,600-15),(600-15,15),10)

def reset():
    screen.fill(BACKGROUD_COLOR)
    draw_grid()
    for row in range(3):
        for col in range(3):
            board[row][col] = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not gameOver:
            row_selected = int(event.pos[0]//200)
            col_selected = int(event.pos[1]//200)
            if(player==1):
                if valid_move(row_selected,col_selected):
                    update_boord(row_selected,col_selected,1)
                    if check_win(player):
                        gameOver = True
                    player = 2
            elif(player== 2):
                if valid_move(row_selected,col_selected):
                    update_boord(row_selected,col_selected,2)
                    if check_win(player):
                        gameOver = True
                    player=1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset()
                gameOver = False
    pygame.display.update()

