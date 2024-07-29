import sys, pygame
import numpy as np
pygame.init()

WIDTH = 600
HEIGHT = 600
TRACK_SIZE = 200
BACKGROUD_COLOR=(31,41,55)
WHITE = (255, 255, 255)
RED =    (205, 92, 92)
YELLOW = (255,255,0)
GREEN = (162,228,184)
FIGURE_WIDTH = 15
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BACKGROUD_COLOR)
board = np.zeros((3,3))
player = 1
gameOver = False
#draw required lines
def draw_grid():
    pygame.draw.line(screen, WHITE, (15,200),(600-15,200), 10)
    pygame.draw.line(screen, WHITE, (15,400),(600-15,400), 10)
    pygame.draw.line(screen, WHITE, (200,15),(200,600-15), 10)
    pygame.draw.line(screen, WHITE, (400,15),(400,600-15), 10)
draw_grid()

def draw_figure(color = WHITE):
    for row in range(3):
        for col in range(3):
            if(board[row][col])==2:
                pygame.draw.circle(screen,RED,(int(row*TRACK_SIZE+TRACK_SIZE/2), int(col*TRACK_SIZE+TRACK_SIZE/2)),TRACK_SIZE/3,10)
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

def boord_complete(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                return False
    return True

def check_win(player,board):
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            #draw_horizontal_winline(col)
            return True
    for row in range(3):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            #draw_vertical_winline(row)
            return True
        
    if board[0][0]==player and board[1][1]==player and board[2][2]==player:
        #draw_up_diagonal_winline()
        return True
    if board[2][0]==player and board[1][1]==player and board[0][2]==player:
        #draw_down_diagonal_winline()
        return True
    return False

def check_win_final(player,board):
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_horizontal_winline(col)
            return True
    for row in range(3):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_vertical_winline(row)
            return True
        
    if board[0][0]==player and board[1][1]==player and board[2][2]==player:
        draw_up_diagonal_winline()
        return True
    if board[2][0]==player and board[1][1]==player and board[0][2]==player:
        draw_down_diagonal_winline()
        return True
    return False

def draw_vertical_winline(col):
    pygame.draw.line(screen, RED, (col*TRACK_SIZE+TRACK_SIZE//2, 15), (col*TRACK_SIZE+TRACK_SIZE//2, 600-15),10)
def draw_horizontal_winline(row):
     pygame.draw.line(screen, RED , (15, row*TRACK_SIZE+TRACK_SIZE//2), (600-15, row*TRACK_SIZE+TRACK_SIZE//2),10)
def draw_up_diagonal_winline():
    pygame.draw.line(screen,RED,(15,15),(600-15,600-15),10)
def draw_down_diagonal_winline():
    pygame.draw.line(screen,RED,(15,600-15),(600-15,15),10)
def reset():
    screen.fill(BACKGROUD_COLOR)
    draw_grid()
    for row in range(3):
        for col in range(3):
            board[row][col] = 0

def minimax(minimax_board, depth, maximising):
    if check_win(2,minimax_board):
        return 1
    elif check_win(1,minimax_board):
        return -1
    elif boord_complete(minimax_board):
        return 0

    if maximising:
        best_score = -2
        for row in range(3):
            for col in range(3):
                if minimax_board[row][col]==0:
                    minimax_board[row][col]=2
                    score = minimax(minimax_board, depth+1, False)
                    minimax_board[row][col]=0
                    best_score = max(score,best_score)
        return best_score
    else:
        best_score = 2
        for row in range(3):
            for col in range(3):
                if minimax_board[row][col]==0:
                    minimax_board[row][col]=1
                    score = minimax(minimax_board, depth+1, True)
                    minimax_board[row][col]=0
                    best_score = min(score,best_score)
        return best_score

def best_move():
    best_score = -2
    move = (-1,-1)
    for row in range(3):
        for col in range(3):
            if board[row][col]==0:
                board[row][col]=2
                score = minimax(board,0,False)
                board[row][col] = 0
                if score>best_score:
                    best_score = score
                    move = (row, col)
    
    return move

                    

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset()
                gameOver = False
        if not gameOver:

            if event.type == pygame.MOUSEBUTTONDOWN and player==1: 
                row_selected = int(event.pos[0]//200)
                col_selected = int(event.pos[1]//200)
                if valid_move(row_selected,col_selected):
                    update_boord(row_selected,col_selected,1)
                    if check_win_final(player, board):
                        gameOver = True
                    player = 2

            if(player== 2):
                move = best_move()
                if valid_move(move[0], move[1]):
                    update_boord(move[0], move[1],2)
                    if check_win_final(player, board):
                        gameOver = True
                    player=1
        
        
    pygame.display.update()

