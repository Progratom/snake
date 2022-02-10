import pygame
import random
import pickle
import os
import math

cell = 20 #velikost samotného čtverce
cell2 = 22 #velikost buněk s okraji
cells = 20 #počet buněk
prostor_score = 100
vyska = cells*cell2
sirka = cells*cell2+prostor_score
pygame.init()

screen = pygame.display.set_mode((sirka, vyska))
clock = pygame.time.Clock()
pressed = pygame.key.get_pressed()
focused = pygame.key.get_focused()
font = pygame.font.Font("ARCADECLASSIC.TTF", 30)
font2 = pygame.font.Font("ARCADECLASSIC.TTF", 20)
font3 = pygame.font.Font("ARCADECLASSIC.TTF", 17)
start_snake = [[1, 1], [1, 1]] #line,place,  line,place
start_direction = "right"
start_speed = 10
start_score = 0
start_fruit = 0
fruit_time = 25
running = True
interupt = False
interupt2 = False
huge_loop = True
start_new_walls = False
start_portals = False
pause = False
start_cheese = False



start_board = [
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
]
new_walls = start_new_walls
board = start_board
speed = start_speed
snake = start_snake
direction = start_direction
score = start_score
fruit = start_fruit
portals = start_portals
cheese = start_cheese
high = len(board)
width = len(board[0])
high_score = 5
active = []
fruit_list = [2, 3, 4, 4, 4, 5, 5, 5, 6]

#hejjjjjj
#pickle.dump(high_score, open("data", "wb"))
high_score = pickle.load(open("data", "rb"))
#print(high_score)


def generate_board():
    #print("board")
    board_line = 0  # číslo momentální linie
    for boardY in board:  # boardY je seznam v seznamu board na pozici board_line
        board_col = 0  # číslo sloupce, začínající 0
        for boardX in boardY:  # boardX je hodnota na pozici board[boardY][]
            if boardX == 0:
                pygame.draw.rect(screen, (128, 128, 128), pygame.Rect(board_col * cell2, board_line * cell2, cell, cell))
            elif boardX == 1:
                pygame.draw.rect(screen, (0, 0, 225), pygame.Rect(board_col * cell2, board_line * cell2, cell, cell))
            elif boardX == 2:
                pygame.draw.rect(screen, (0, 225, 0), pygame.Rect(board_col * cell2, board_line * cell2, cell, cell))
            elif boardX == 3:
                pygame.draw.rect(screen, (225, 0, 0), pygame.Rect(board_col * cell2, board_line * cell2, cell, cell))
            elif boardX == 4:
                pygame.draw.rect(screen, (70, 70, 70), pygame.Rect(board_col * cell2, board_line * cell2, cell, cell))
            elif boardX == 5:
                pygame.draw.rect(screen, (225, 165, 0), pygame.Rect(board_col * cell2, board_line * cell2, cell, cell))
            elif boardX == 6:
                pygame.draw.rect(screen, (139, 0, 225), pygame.Rect(board_col * cell2, board_line * cell2, cell, cell))
            board_col = board_col + 1  # navýšení sloupce o jedna
        board_line = board_line + 1  # navýšení linie o jedna
    # print("board_end")
    pygame.display.flip()

def random_two():
    x = random.choice(range(0, width))
    y = random.choice(range(0, high))
    while board[y][x] != 0:
        x = random.choice(range(0, width))
        y = random.choice(range(0, high))
    return(x, y)

def change(value):
    if value == True:
        return False
    elif value == False:
        return True


def input():
    #print("zdravíčko")
    for event in pygame.event.get(): #reactions on the keys
            if event.type == pygame.KEYDOWN:        
                if event.type == pygame.QUIT:
                    return("quit")
                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print("jakože hej")
                    return(pygame.mouse.get_pos())
                    


#------------------------start loop--------------------------
round = 0
while huge_loop == True:
    round += 1
#-___________________________
    if score > high_score:
        high_score = score
        print("new high score")
        new_high = True
    else:
        new_high = False

    screen.fill((0, 0, 0))
    circle = 0
    add_body = True
    del_body = True
    cheese = start_cheese
    new_walls = start_new_walls
    portals = start_portals
    running = True
    score = start_score
    #board = start_board
    speed = start_speed
    #snake = start_snake
    direction = start_direction
    interupt2 = False
    fruit = start_fruit
    help = False
    triple = False
    penta = False
    double = False
    half = False
    new_fruits = 5
    fruit_circle = 0
    fruitY = 0
    fruitX = 0

    active = []
    snake = [[1, 2], [1, 1]]
    board = [
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    ]
    while interupt2 == False:

        #print("hej")
        screen.fill((0, 0, 0))
        if new_high:
            text = font.render("Congratulation new high score", False, (225, 225, 225))
            screen.blit(text, (20, 70))
        elif round > 1:
            text = font.render("Game over", False, (225, 225, 225))
            screen.blit(text, (20, 70))
        text = font.render("Press space to start", False, (225, 225, 225))
        screen.blit(text, (20, 100))
        text = font2.render("Press 1 for triple mode", False, (225, 225, 225))
        screen.blit(text, (20, 132))
        text = font2.render("Press 2 for penta mode", False, (225, 225, 225))
        screen.blit(text, (20, 164))
        text = font2.render("Press 3 for double speed", False, (225, 225, 225))
        screen.blit(text, (20, 196))
        text = font2.render("Press 4 for half speed", False, (225, 225, 225))
        screen.blit(text, (20, 228))
        text = font2.render("Press 5 for wall mode", False, (225, 225, 225))
        screen.blit(text, (20, 260))
        text = font2.render("Press 6 for portals mode", False, (225, 225, 225))
        screen.blit(text, (20, 292))
        text = font2.render("Press 7 for cheese mode", False, (225, 225, 225))
        screen.blit(text, (20, 324))
        text = font2.render("Press 0 delete of all modes", False, (225, 225, 225))
        screen.blit(text, (20, 356))
        text = font2.render("Press H for help", False, (225, 225, 225))
        screen.blit(text, (385, 420))
        text = font3.render("active  modes"+str(active), False, (225, 225, 225))
        screen.blit(text, (20, 388))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_KP_ENTER:
                    running = True
                    interupt2 = True
                elif event.key == pygame.K_KP0 or event.key == pygame.K_0:
                    active = []
                    speed = start_speed
                    board[6][5] = 0
                    board[15][12] = 0
                    board[10][10] = 0
                    board[3][12] = 0
                    board[18][1] = 0
                    board[1][18] = 0
                    portals = False
                    new_walls = False
                    cheese = False
                elif event.key == pygame.K_KP1 or event.key == pygame.K_1:
                    board[6][5] = 3
                    board[15][12] = 3
                    board[10][10] = 0
                    board[3][12] = 0
                    board[18][1] = 0
                    board[1][18] = 0
                    portals = False
                    tripple = True
                    if 1 not in active:
                        active.append(1)
                    if 6 in active:
                        active.remove(6)
                    if 2 in active:
                        active.remove(2)
                elif event.key == pygame.K_KP2 or event.key == pygame.K_2:
                    board[6][5] = 3
                    board[15][12] = 3
                    board[10][10] = 3
                    board[3][12] = 3
                    board[18][1] = 0
                    board[1][18] = 0
                    portals = False
                    penta = True
                    if 2 not in active:
                        active.append(2)
                        if 1 in active:
                            active.remove(1)
                    if 6 in active:
                        active.remove(6)
                elif event.key == pygame.K_KP3 or event.key == pygame.K_3:
                    if speed != start_speed:
                        speed = start_speed
                    speed = start_speed * 2
                    double = True
                    if 3 not in active:
                        active.append(3)
                        if 4 in active:
                            active.remove(4)
                elif event.key == pygame.K_KP4 or event.key == pygame.K_4:
                    if speed != start_speed:
                        speed = start_speed * 0.5
                    speed = start_speed * 0.5
                    half = True
                    if 4 not in active:
                        active.append(4)
                        if 3 in active:
                            active.remove(3)
                elif event.key == pygame.K_KP5 or event.key == pygame.K_5:
                    new_walls = True
                    board[18][1] = 0
                    board[1][18] = 0
                    portals = False
                    if 5 not in active:
                        active.append(5)
                    if 6 in active:
                        active.remove(6)
                elif event.key == pygame.K_KP6 or event.key == pygame.K_6:
                    portals = True
                    if 6 not in active:
                        active.append(6)
                        if 1 in active:
                            active.remove(1)
                        if 2 in active:
                            active.remove(2)
                        if 5 in active:
                            active.remove(5)
                elif event.key == pygame.K_KP7 or event.key == pygame.K_7:
                    cheese = True
                    if 7 not in active:
                        active.append(7)
                elif event.key == pygame.K_h:
                    help = True
                    while help:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_h:
                                    help = False
                                elif event.key == pygame.K_d:
                                    high_score = 0
                            elif event.type == pygame.QUIT:
                                interupt2 = True
                                huge_loop = False
                                running = False
                                help = False
                        screen.fill((0, 0, 0))
                        text = font2.render("For quit press H", False, (225, 225, 225))
                        screen.blit(text, (380, 420))
                        text = font.render("This game was made by Tom", False, (225, 225, 225))
                        screen.blit(text, (20, 100))
                        text = font3.render("Use WASD or arrows for moving", False, (225, 225, 225))
                        screen.blit(text, (20, 130))
                        text = font3.render("for start a game press a space", False, (225, 225, 225))
                        screen.blit(text, (20, 150))
                        text = font3.render("if you want to choose a  press the number and than press a space", False, (225, 225, 225))
                        screen.blit(text, (20, 170))
                        text = font3.render("you can choose more that one", False, (225, 225, 225))
                        screen.blit(text, (20, 190))
                        text = font3.render("during the game press p for pause and again for resume", False, (225, 225, 225))
                        screen.blit(text, (20, 210))
                        text = font3.render("for delete of high score of high score press d", False, (225, 225, 225))
                        screen.blit(text, (20, 230))
                        pygame.display.flip()

            elif event.type == pygame.QUIT:
                interupt2 = True
                huge_loop = False
                running = False

    if portals == True:
        board[6][5] = 0
        board[15][12] = 0
        board[10][10] = 0
        board[3][12] = 0
        board[7][9] = 0
        board[18][1] = 6
        board[1][18] = 6
        portA = [18, 1]
        portB = [1, 18]
    if cheese:
        snake = [[1, 2]]
        # print(snake)
        # print(snake[0])
        snake_body = [[1, 2]]
        old_snake = snake[0]
#____________________

    screen.fill((0, 0, 0))
    pygame.display.flip()
    #-----------------------loop------------------
    while running:
        #print("start")
        circle += 1 #number of running loop
        generate_board()
        old_direction = direction


        
        for event in pygame.event.get(): #reactions on the keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    if old_direction != "right":
                        direction = "left"
                    #print("left")
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    if old_direction != "left":
                        direction = "right"
                    #print("right")
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    if old_direction != "down":
                        direction = "up"
                    #print("up")
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    if old_direction != "up":
                        direction = "down"
                    #print("down")
                elif event.key == pygame.K_q:
                    running = False
                elif event.key == pygame.K_p: #pause - loop that end, when p is pressed again
                    pause = True
                    while pause:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_p:
                                    pause = False
                        clock.tick(speed)
        

       

        if cheese:
            #print(snake)
            nowLine = snake[-1][0]
            nowPlace = snake[-1][1]
        else:
            #print(snake)
            nowLine = snake[-1][0] #coordinates of head
            nowPlace = snake[-1][1]

        if direction == "left":
            snake.append([nowLine, nowPlace-1])
        elif direction == "right":
            #print("hej")
            #print(snake)
            snake.append([nowLine, nowPlace+1])
            #print(snake)
        elif direction == "up":
            snake.append([nowLine-1, nowPlace])
        elif direction == "down":
            snake.append([nowLine+1, nowPlace])


        if board[snake[-1][0]][snake[-1][1]] == 3:
            score += 1
            fruit += 1
            x, y = random_two()
            board[y][x] = 3
            if fruit >= new_fruits and board[fruitY][fruitX] != 5:
                x, y = random_two()
                board[y][x] = 5
                fruitX = x
                fruitY = y
                fruit_circle = circle
                new_fruits = random.choice(fruit_list)

            if new_walls == True:
                x, y = random_two()
                board[y][x] = 4
            if cheese:
                del_body = False
        elif board[snake[-1][0]][snake[-1][1]] == 4:
            running = False
        elif board[snake[-1][0]][snake[-1][1]] == 1:
            running = False
        elif board[snake[-1][0]][snake[-1][1]] == 5:
            score += 5
            fruit = 0
            #x, y = random_two()
            #board[y][x] = 3
        elif board[snake[-1][0]][snake[-1][1]] == 6:
            #print("2portA: " + str(portA))
            #print("2portB: " + str(portB))
            score += 1
            if snake[-1] == portA:
                snake.append(portB)
            elif snake[-1] == portB:
                snake.append(portA)
            else:
                #print("3portA: "+str(portA))
                #print("3portB: "+str(portB))
                print("hej")
            x, y = random_two()
            board[y][x] = 6
            portA = [y, x]
            if cheese == True:
                del_body = False
            #print("1portA: "+str(portA))
            x, y = random_two()
            board[y][x] = 6
            portB = [y, x]
            #print("1portB: " + str(portB))
            #print(snake)
            board[snake[-3][0]][snake[-3][1]] = 1
            #board[snake[-1][0]][snake[-1][1]] = 1
            board[snake[0][0]][snake[0][1]] = 0
            del snake[0]
            #board[snake[0][0]][snake[0][1]] = 0
            #del snake[0]
            #print(snake)
        elif cheese:
            pass
        else:
            board[snake[0][0]][snake[0][1]] = 0
            del snake[0]

        if cheese:
            if len(snake) > 1:
                board[snake[-1][0]][snake[-1][1]] = 2
                board[snake[0][0]][snake[0][1]] = 0
                del snake[0]
                add_body = change(add_body)
                if add_body == False:
                    old_snake = snake[-1]
                elif add_body == True:
                    snake_body.append(old_snake)
                    #board[snake_body[-2][0]][snake_body[-2][1]] = 0
                    board[snake_body[-1][0]][snake_body[-1][1]] = 1
                    #old_snake = snake[-1]
                    if del_body == True:
                        #print("jaja")
                        board[snake_body[0][0]][snake_body[0][1]] = 0
                        del (snake_body[0])
                        del_body = True
                    elif del_body == False:
                        del_body = True

            else:
                print("hej2")
        else:
            board[snake[-1][0]][snake[-1][1]] = 2
            board[snake[-2][0]][snake[-2][1]] = 1

        if board[fruitY][fruitX] == 5:
            if circle - fruit_circle > fruit_time:
                board[fruitY][fruitX] = 0
                fruit = 0

        screen.fill((0, 0, 0))
        text = font.render("score", False, (225, 225, 225))
        screen.blit(text, (20 * cell2 + 4, 10))
        text = font.render(str(score), False, (225, 225, 225))
        screen.blit(text, (20*cell2 + 4, 40))
        text = font.render("high", False, (225, 225, 225))
        screen.blit(text, (20 * cell2 + 4, 70))
        text = font.render(str(high_score), False, (225, 225, 225))
        screen.blit(text, (20 * cell2 + 4, 100))
        generate_board()
        clock.tick(speed)
    #-------------------------------end of loop------------------------------------------
#print(high_score)
pickle.dump(high_score, open("data", "wb"))
#print(pickle.load(open("data", "rb")))
#print("Loops ended")


"""
    screen.fill((0, 0, 0))
    cheese = start_cheese
    new_walls = start_new_walls
    portals = start_portals
    running = True
    score = start_score
    #board = start_board
    speed = start_speed
    #snake = start_snake
    direction = start_direction
    interupt2 = False
    fruit = start_fruit
    snake = [[1, 2], [1, 1]]
    board = [
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    ]
    while interupt2 == False:
        #print("hej")
        screen.fill((0, 0, 0))
        text = font.render("Game over", False, (225, 225, 225))
        screen.blit(text, (20, 70))
        text = font.render("Press space to start", False, (225, 225, 225))
        screen.blit(text, (20, 100))
        text = font2.render("Press 1 for triple mode", False, (225, 225, 225))
        screen.blit(text, (20, 132))
        text = font2.render("Press 2 for penta mode", False, (225, 225, 225))
        screen.blit(text, (20, 164))
        text = font2.render("Press 3 for double speed", False, (225, 225, 225))
        screen.blit(text, (20, 196))
        text = font2.render("Press 4 for half speed", False, (225, 225, 225))
        screen.blit(text, (20, 228))
        text = font2.render("Press 5 for wall mode", False, (225, 225, 225))
        screen.blit(text, (20, 260))
        text = font2.render("Press 6 for portals mode", False, (225, 225, 225))
        screen.blit(text, (20, 292))
        text = font2.render("Press 7 for cheese mode", False, (225, 225, 225))
        screen.blit(text, (20, 324))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_KP_ENTER:
                    running = True
                    interupt2 = True
                elif event.key == pygame.K_KP1:
                    board[6][5] = 3
                    board[15][12] = 3
                elif event.key == pygame.K_KP2:
                    board[6][5] = 3
                    board[15][12] = 3
                    board[10][10] = 3
                    board[3][12] = 3
                elif event.key == pygame.K_KP3:
                    if speed != start_speed:
                        speed = start_speed
                    speed = start_speed * 2
                elif event.key == pygame.K_KP4:
                    if speed == start_speed:
                        speed = start_speed * 0.5
                    else:
                        speed = start_speed
                elif event.key == pygame.K_KP5:
                    new_walls = True
                elif event.key == pygame.K_KP6:
                    portals = True
                elif event.key == pygame.K_KP7:
                    cheese = True
            elif event.type == pygame.QUIT:
                interupt2 = True
                huge_loop = False
        if portals == True:
            board[6][5] = 0
            board[15][12] = 0
            board[10][10] = 0
            board[3][12] = 0
            board[7][9] = 0
            board[18][1] = 6
            board[1][18] = 6
            portA = [18, 1]
            portB = [1, 18]
        if cheese:
            snake = [[1, 2]]
            # print(snake)
            # print(snake[0])
            snake_body = [[1, 2]]
            old_snake = snake[0]
            
            
            
            
    while interupt == True:
    screen.fill((0, 0, 0)) #render text with options
    text = font.render("Press space to start", False, (225, 225, 225))
    screen.blit(text, (20, 100))
    text = font2.render("Press 1 for triple mode", False, (225, 225, 225))
    screen.blit(text, (20, 132))
    text = font2.render("Press 2 for penta mode", False, (225, 225, 225))
    screen.blit(text, (20, 164))
    text = font2.render("Press 3 for double speed", False, (225, 225, 225))
    screen.blit(text, (20, 196))
    text = font2.render("Press 4 for half speed", False, (225, 225, 225))
    screen.blit(text, (20, 228))
    text = font2.render("Press 5 for wall mode", False, (225, 225, 225))
    screen.blit(text, (20, 260))
    text = font2.render("Press 6 for portals mode", False, (225, 225, 225))
    screen.blit(text, (20, 292))
    text = font2.render("Press 7 for cheese mode", False, (225, 225, 225))
    screen.blit(text, (20, 324))
    pygame.display.flip()
    for event in pygame.event.get(): #reaction on the keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_KP_ENTER:
                interupt = True
            elif event.key == pygame.K_KP1:
                board[6][5] = 3
                board[15][12] = 3
            elif event.key == pygame.K_KP2:
                board[6][5] = 3
                board[15][12] = 3
                board[10][10] = 3
                board[3][12] = 3
            elif event.key == pygame.K_KP3:
                if speed != start_speed:
                    speed = start_speed
                speed = start_speed * 2
            elif event.key == pygame.K_KP4:
                if speed == start_speed:
                    speed = start_speed * 0.5
                else:
                    speed = start_speed
            elif event.key == pygame.K_KP5:
                new_walls = True
            elif event.key == pygame.K_KP6:
                portals = True
            elif event.key == pygame.K_KP7:
                cheese = True
                #pass
        elif event.type == pygame.QUIT:
            interupt = True
            huge_loop = False

if portals == True: #in portals mode is everything else zero
    board[6][5] = 0
    board[15][12] = 0
    board[10][10] = 0
    board[3][12] = 0
    board[7][9] = 0
    board[18][1] = 6
    board[1][18] = 6
    portA = [18, 1]
    portB = [1, 18]
if cheese:
    snake = [[1, 2]]
    #print(snake)
    #print(snake[0])
    snake_body = [[1, 2]]
    old_snake = snake[0]
screen.fill((0, 0, 0))
pygame.display.flip()
"""

