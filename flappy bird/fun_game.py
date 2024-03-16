# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names:
# Erdi Sadiku
# Michael Wood
# Oliver Jansen
# Diego Esquivel
# Section: 527
# Assignment: LAB 8.10
# Date: 11 1 2023
#

import turtle as turt
import pygame as py
from math import sqrt
import random
import sys
import pygame



screen_width = 1534
screen_height = 864
screen = py.display.set_mode((1534,864))




def theflappycat():
    runtheflappycat = True
    while runtheflappycat:


           


        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Flappy Cat")


        global running
        global dead
        global catHeight
        global score
        global scoreString


        catHeight = 0
        gravity = 3
        cVelocity = 160
        score = 0
        scoreString = '0'


        movement = [random.randint(-13, -7),
                    random.randint(-13, -7),
                    random.randint(-13, -7),
                    random.randint(-13, -7),
                    random.randint(-13, -7),
                    random.randint(-13, -7)] #movement speeeds for dogs


        dogX = [1400 - random.randint(-1500, -120),
                1400 - random.randint(-1500, -120),
                1400 - random.randint(-1500, -120),
                1400 - random.randint(-1500, -120),
                1400 - random.randint(-1500, -120),
                1400 - random.randint(-1500, -120), ]


        dogY = [random.randint(0, 300),
                random.randint(350, 500),
                random.randint(550, 700),
                random.randint(710, 1000),
                random.randint(1040, 1200),
                random.randint(1210, 1400)]


        mSize = (1536, 864)
        gSize = (600, 800)
        cSize = (75, 75)
        dSize = (175, 75)


        screenWidth = 1536
        screenHeight = 864
        #loading fonts
        screen = pygame.display.set_mode((screenWidth, screenHeight))
        font = pygame.font.Font("BotsmaticDemo-MXOr.ttf", 30)
        numFont = pygame.font.Font("flappy-bird-font.ttf", 60)
        #loading images
        mountains = pygame.image.load("background_glacial_mountains.png").convert_alpha()
        mountains = pygame.transform.scale(mountains, mSize)


        blurMountains = pygame.image.load("blurMountains.png").convert_alpha()
        blurMountains = pygame.transform.scale(blurMountains, mSize)


        deathScreen = pygame.image.load("deathScreen.png").convert_alpha()
        deathScreen = pygame.transform.scale(deathScreen, mSize)


        goldMountains = pygame.image.load("goldMountains.png").convert_alpha()
        goldMountains = pygame.transform.scale(goldMountains, mSize)


        tColor = (0, 0, 0)


        garfield = pygame.image.load("TIUA5376.JPG")
        garfield = pygame.transform.scale(garfield, gSize)


        cat = pygame.image.load("Cat-1-Sitting1.png").convert_alpha()
        cat = pygame.transform.scale(cat, cSize)
        catRect = pygame.Rect(385, catHeight, cSize[0], cSize[1])


        dog = pygame.image.load("badDog (2)1.png").convert_alpha()
        dog = pygame.transform.scale(dog, dSize)
        dog1 = pygame.image.load("badDog (2)1.png").convert_alpha()
        dog1 = pygame.transform.scale(dog, dSize)


        dog2 = pygame.image.load("badDog (2)1.png").convert_alpha()
        dog2 = pygame.transform.scale(dog, dSize)
        dog3 = pygame.image.load("badDog (2)1.png").convert_alpha()
        dog3 = pygame.transform.scale(dog, dSize)
        dog4 = pygame.image.load("badDog (2)1.png").convert_alpha()
        dog4 = pygame.transform.scale(dog, dSize)
        #setting dog hitbox
        dogRect = pygame.Rect(dogX[0], dogY[0], dSize[0], dSize[1])
        dogRect1 = pygame.Rect(dogX[1], dogY[1], dSize[0], dSize[1])


        dogRect2 = pygame.Rect(dogX[2], dogY[2], dSize[0], dSize[1])
        dogRect3 = pygame.Rect(dogX[3], dogY[3], dSize[0], dSize[1])
        dogRect4 = pygame.Rect(dogX[4], dogY[4], dSize[0], dSize[1])


        listOfDogs = [dog, dog1, dog2, dog3, dog4]


        listOfDogHitboxes = [dogRect, dogRect1, dogRect2, dogRect3, dogRect4, ]


        file = open("highScores.txt", "w")


        def dogs(o, x, y):
            screen.blit(listOfDogs[o], (x, y))


        def createText(text, font, tColor):
            text = font.render(text, True, tColor)
            if (font == numFont):
                textRect = text.get_rect(center=(screenWidth / 2, 100))
            else:
                textRect = text.get_rect(center=(screenWidth / 2, screenHeight / 2))
            screen.blit(text, textRect)


        def intro():
            global score, catHeight
            score = 0
            catHeight = 0


            for i in range(6):
                dogY[i] = dogY[i]
                dogX[i] = 1400 - random.randint(-1500, -120)


            screen.blit(blurMountains, (0, 0))
            dialogue = [
                        "welcome to flappy cat",
                        "your job is to prevent my cat garfield from running into one of those nasty dogs",
                        "you can make garfield fly up by holding the space bar down",
                        "if at any time you want to pause press the escape button",
                        "you gain a point every time you successfully evade an evil dog",
                        "this is what you are fighting for",
                        "",
                        "press the space bar when you are ready to start"
                        ]
            for i in range(len(dialogue)):
                if i < len(dialogue):
                    nextWord = True
                createText(dialogue[i], font, tColor)
                pygame.display.update()
                clock.tick(120)
                if i == 6:
                    screen.blit(garfield, (450, 50))
                    pygame.display.update()
                    clock.tick(120)
                while nextWord:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                nextWord = False
                screen.blit(blurMountains, (0, 0))


        def death(died, num):
            catRect = pygame.Rect(385, catHeight, cSize[0], cSize[1])
            dogRect = pygame.Rect(dogX[0], dogY[0], dSize[0], dSize[1])
            dogRect1 = pygame.Rect(dogX[1], dogY[1], dSize[0], dSize[1])
            dogRect2 = pygame.Rect(dogX[2], dogY[2], dSize[0], dSize[1])
            dogRect3 = pygame.Rect(dogX[3], dogY[3], dSize[0], dSize[1])
            dogRect4 = pygame.Rect(dogX[4], dogY[4], dSize[0], dSize[1])
            dogRect5 = pygame.Rect(dogX[5], dogY[5], dSize[0], dSize[1])


            screen.blit(deathScreen, (0, 0))
            while died:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            running = True
                            dead = True
                            died = False
                createText("            you have died\n\ngarfield will never forgive you\n\n", font, tColor)
                clock.tick(5000)
                Mainmenu()
                pygame.display.update()
                clock.tick(120)


        def pause():
            screen.blit(blurMountains, (0, 0))
            createText("                           paws\n\n          press space to resume your game\n         press the escape button to restart\npress the big red x in the top right to exit out",
                       font, tColor)
            pRun = True
            while pRun:
                pygame.display.update()
                clock.tick(120)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            running = False
                            pRun = False
                        elif event.key == pygame.K_ESCAPE:
                            intro()
                        elif event.key == pygame.K_LCTRL:
                            secret()


        def secret():
            screen.blit(goldMountains, (0, 0))
            pygame.display.update()
            clock.tick(120)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            lore = []
            file = open("garfieldLore.txt", 'r')
            while not (file.readline() == ''):
                lore.append(file.readline())


            for i in range(len(lore)):
                if i < len(lore):
                    nextWord = True
                createText(lore[i], font, tColor)
                pygame.display.update()
                clock.tick(120)
                while nextWord:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_LCTRL:
                                nextWord = False


            file.close()


        menu = True
        running = True
        spaceDown = False
        main = True
        dead = False


        while main:
            intro()


            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            spaceDown = True
                        elif event.key == pygame.K_ESCAPE:
                            pause()
                        else:
                            continue
                        pygame.display.update()
                        clock.tick(120)
                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_SPACE:
                            spaceDown = False


                if spaceDown:
                    catHeight -= 10
                    catRect.y -= 10


                for i in range(len(listOfDogs)):
                    if pygame.Rect.colliderect(catRect, listOfDogHitboxes[i]):
                        dogAttack = listOfDogHitboxes[i]
                        catHeight = 0
                        running = False
                        dead = True
                        print(dogAttack)
                        death(dead, scoreString)


                for i in range(len(listOfDogs)):
                    if (dogX[i] < -200):
                        score += 1
                        dogY[i] = dogY[i]


                        dogX[i] = 1400 - random.randint(-1500, -120)


                        listOfDogHitboxes[i] = pygame.Rect(dogX[i], dogY[i], dSize[0], dSize[1])


                screen.blit(mountains, (0, 0))


                for i in range(len(listOfDogs)):
                    dogX[i] += movement[i]
                    listOfDogHitboxes[i].centerx += movement[i]


                catHeight += gravity
                catRect.centery += gravity


                screen.blit(cat, (385, catHeight))


                for i in range(len(listOfDogs)):
                    dogs(i, dogX[i], dogY[i])


                scoreString = str(score)


                createText(scoreString, numFont, tColor)


                if (catHeight > 800):
                    catHeight = 0
                    running = False
                    dead = True
                    death(dead, scoreString)
                elif (catHeight < -200):
                    catHeight = 0
                    running = False
                    dead = True
                    death(dead, scoreString)


                print("CatRect Position:", catRect)
                print("Cat Position:", 385, catHeight)


                for i in range(len(listOfDogs)):
                    print(f"Dog{i} rect{i} position: {listOfDogHitboxes[i]}")


                pygame.display.update()
                clock.tick(120)


            catRect = pygame.Rect(385, catHeight, cSize[0], cSize[1])
            dogRect = pygame.Rect(dogX[0], dogY[0], dSize[0], dSize[1])
            dogRect1 = pygame.Rect(dogX[1], dogY[1], dSize[0], dSize[1])
            dogRect2 = pygame.Rect(dogX[2], dogY[2], dSize[0], dSize[1])
            dogRect3 = pygame.Rect(dogX[3], dogY[3], dSize[0], dSize[1])
            dogRect4 = pygame.Rect(dogX[4], dogY[4], dSize[0], dSize[1])
            dogRect5 = pygame.Rect(dogX[5], dogY[5], dSize[0], dSize[1])


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
'''
font_size = 36
font_color = (255, 255, 255)
font = py.font.Font(font_path, font_size)
text_content = "Click here to play Flappy Cat"
text_surface = font.render(text_content, True, font_color)
text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2))


'''


#loading my images
upimage = py.image.load('startbutton.png').convert_alpha()
downimage = py.image.load('startbutton.png').convert_alpha()
quitimage = py.image.load('exitbutton.png').convert_alpha()
bar = py.image.load('black bar.png').convert_alpha






'''\turtle.Screen().bgcolor(24 / 255, 43 / 255, 79 / 255)
turtle.color("black")
turtle.width(5)
turtle.penup()
turtle.goto(0,100)
#speech bubble outline
turtle.pendown()
turtle.circle(100, 180)
turtle.forward(200)
turtle.circle(100, 180)


#tail
turtle.begin_fill()
turtle.width(5)  # Adjust the width of the pen
turtle.goto(70, -100)
turtle.goto(0,100)
turtle.done()'''


#all that turtle makes the speach bubble icon
bigspeech =  py.image.load('speach bubble.png')
small_speach = py.transform.scale(bigspeech, (bigspeech.get_width() // 2, bigspeech.get_height() // 3))
#this one is from reed
bigback =  py.image.load('background_glacial_mountains.png')
biggerback = py.transform.scale(bigback, (bigback.get_width() * 2, bigback.get_height() * 3))


smallcat = py.image.load('Cat-1-Sitting.png')
bigcat = py.transform.scale(smallcat, (smallcat.get_width() * 7, smallcat.get_height() * 7))


smalldog =py.image.load('badDog (2).png')
bigdog = py.transform.scale(smalldog, (smalldog.get_width() * 4, smalldog.get_height() * 4))


bigmario = py.image.load('mario.png')
mario = py.transform.scale(bigmario, (bigmario.get_width() // 3, bigmario.get_height() // 3))


bigsunny = py.image.load('sunglasses.png')
sunnies = py.transform.scale(bigsunny, (bigsunny.get_width() // 5, bigsunny.get_height() // 5))


bigguy = py.image.load('pressstart.png')
guy = py.transform.scale(bigguy, (bigguy.get_width() // 3, bigguy.get_height() // 3))


greenbig = py.image.load('greengguy.png')
green = py.transform.scale(greenbig, (greenbig.get_width() // 3, greenbig.get_height() // 3))




#making a button as a class
class Button():
        """function for the button, this will be clickable"""
        def __init__(self,x,y,image):
             self.image = image
             self.rect = self.image.get_rect()
             self.rect.topleft = (x,y)
             self.clicked = False


#the meat of my button function, draws it and checks if it is clicked
        def draw(self):
             action = False
             pos = py.mouse.get_pos()


             if self.rect.collidepoint(pos): #checking if mouse and button collide
                   if py.mouse.get_pressed()[0] == 1 and self.clicked == False:
                        self.clicked = True
                        action = True
                        #print('clicked')
                        return action
                    #so i only click it one time
                   if py.mouse.get_pressed()[0] == 0:
                        self.clicked = False
            #finally draw and return
             screen.blit(self.image, (self.rect.x, self.rect.y))
             return action


def erdiscode():
    Erdi = True
    while Erdi:
        def print_board(board):
            """Prints the board of the connect4 into the terminal"""
            for row in board:
                print("|", end=" ")
                for cell in row:
                    print(cell, end=" | ")
                print()
                print("+---" * len(row) + "+")




        def check_winner(board, player):
            # Check horizontally
            for row in board:
                for i in range(len(row) - 3):
                    if all(cell == player for cell in row[i:i+4]):
                        return True




            # Check vertically
            for col in range(len(board[0])):
                for i in range(len(board) - 3):
                    if all(board[i+j][col] == player for j in range(4)):
                        return True




            # Check diagonally (positive slope)
            for i in range(len(board) - 3):
                for j in range(len(board[0]) - 3):
                    if all(board[i+k][j+k] == player for k in range(4)):
                        return True




            # Check diagonally (negative slope)
            for i in range(len(board) - 3):
                for j in range(3, len(board[0])):
                    if all(board[i+k][j-k] == player for k in range(4)):
                        return True




            return False




        def is_full(board):
            """checks if the board is full"""
            return all(cell != ' ' for row in board for cell in row)




        def drop_piece(board, col, player):
            for row in range(len(board) - 1, -1, -1):
                if board[row][col] == ' ':
                    board[row][col] = player
                    break




        def write_game_result(game_number, winner, final_board):
            with open("snooze_you_lose.txt", "a") as file:
                file.write(f"Game {game_number} - Winner: {winner}\n")
                for row in final_board:
                    file.write('|'.join(row) + '\n')
                file.write("\n")




        def display_options():
            print("\nOptions:")
            print("1. Play game")
            print("2. Display Score")
            print("3. Quit")




        def display_score(game_number, player_x_wins, player_o_wins):
            print(f"\nGame {game_number} - Score:")
            print(f"Player X Wins: {player_x_wins}")
            print(f"Player O Wins: {player_o_wins}")




        def connect4_game():
            player_x_wins = 0
            player_o_wins = 0
            game_number = 1




            while True:
                display_options()




                try:
                    option = int(input("Enter your choice (1-3): "))
                    if option == 1:
                        print("Connect Four Instructions:")
                        print("If you have never played connect 4 before that is kind of sad.\n Basically the instructions are that you and the player that you\n are playing agaisnt will have to take turns placing yalls identifiers\n into the columns. The goal of the game is to get 4 of your identifiers\n next to each other in either a vertical, diagonal, or horizontal manner.\n GOOD LUCK!!!!")
                        # Display instructions
                    elif option == 2:
                        display_score(game_number, player_x_wins, player_o_wins)
                    elif option == 3:
                        Mainmenu()
                        erdi = False
                       
                        break
                    else:
                        print("Invalid option. Please choose a valid option.")
                        continue
                except ValueError:
                    print("Invalid input. Enter a number.")
                    continue




                if option == 3:
                    break




                board = [[' ' for _ in range(7)] for _ in range(6)]
                current_player = 'X'




                while True:
                    print_board(board)




                    try:
                        col = int(input(f"Player {current_player}, choose a column (0-6): "))
                        if 0 <= col <= 6 and board[0][col] == ' ':
                            drop_piece(board, col, current_player)




                            if check_winner(board, current_player):
                                print_board(board)
                                print(f"Player {current_player} wins!")
                                write_game_result(game_number, current_player, board)
                                if current_player == 'X':
                                    player_x_wins += 1
                                else:
                                    player_o_wins += 1
                                break




                            if is_full(board):
                                print_board(board)
                                print("It's a draw!")
                                write_game_result(game_number, 'Draw', board)
                                break




                            current_player = 'O' if current_player == 'X' else 'X'
                        else:
                            print("Invalid move. Choose a valid column.")
                    except ValueError:
                        print("Invalid input. Enter a number.")




                game_number += 1




        connect4_game()








upbutton = Button(740,300, upimage)
downbutton = Button(740,497, downimage)
exitbutton = Button(1480, 0, quitimage)
def Mainmenu():
   
   
    py.init()
    run = True
    while run:
       
     
        for event in py.event.get():
          if event.type == py.QUIT:
               run = False
   




        #loading all the images in the menu
        screen.blit(biggerback, (400, 400))
        screen.blit(py.image.load('black bar.png'), (0, 400))
        screen.blit(small_speach, (60, 500))
        screen.blit(py.image.load('title1.png'), (398, 437))
        screen.blit(py.image.load('exitlabel.png'), (1490, 57))
        screen.blit(bigcat, (110, 560))
        screen.blit(bigdog, (500, 560))
        screen.blit(bigdog, (680, 700))
        screen.blit(bigdog, (900, 500))
        screen.blit(py.image.load('cattext.png'), (90, 520))
        screen.blit(py.image.load('thedogs.png'), (90, 550))
        screen.blit(py.image.load('erdistructions.png'), (450, 0))
        screen.blit(py.image.load('erdispic.png'), (715, 120))
        screen.blit(mario, (1200, 120))
        screen.blit(sunnies, (1223, 111))
        screen.blit(guy, (230, 20))
        screen.blit(green, (0, 150))
        screen.blit(green, (1200, 500))
        screen.blit(guy, (1300, 700))
        screen.blit(sunnies, (1224, 525))




   
        #quit the game
        if exitbutton.draw() == True:
             pygame.QUIT
             sys.exit()
             
        if upbutton.draw() == True:
            pygame.quit()
            erdiscode()


        if downbutton.draw() == True:
             run = False
             theflappycat()
        upbutton.draw()
        downbutton.draw()
        exitbutton.draw()


        py.display.update()
        screen.fill((24,43,79)) #has to be tuple
Mainmenu()













