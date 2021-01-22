import pygame
import time
import random

pygame.init()

# color values
green = (0,150,0)
red = (255,0,0)
blue = (0,0,255)

#The screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Car Racing Game")
car_width = 56

#Loading the image
carimg = pygame.image.load("car1.jpg")
intro_img = pygame.image.load("background.jpg")

# def intro_loop():
#     intro  = True
#     while intro:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#                 sys.exit()
#         screen.blit(intro_img,(0,0))
#         font = pygame.font.SysFont(None,190)
#         title = font.render("CAR GAME", True , (0,0,0))
#         screen.blit(title,(50,50))
#         pygame.draw.rect(screen,green,(80,525,150,50))
#         pygame.draw.rect(screen, red, (320, 525, 150, 50))
#         pygame.draw.rect(screen, blue, (580, 525, 150, 50))
#
#
#
#
#         pygame.display.update()

#load all the images
grass = pygame.image.load("grass.jpg")
strip = pygame.image.load("strip.jpg")
yellow = pygame.image.load("yellow_strip.jpg")

#crashed message
myfont = pygame.font.SysFont("None",100)
render_text = myfont.render("CAR CRASHED", 1 ,(0,0,0))

#time module
clock = pygame.time.Clock()

#function for the obstacle
def obstacle(obs_x,obs_y,obs):
    if obs == 0:
        obs_pic = pygame.image.load("car2.jpg")
    elif obs == 1:
        obs_pic = pygame.image.load("car3.jpg")
    elif obs == 2:
        obs_pic = pygame.image.load("car4.jpg")
    elif obs == 3:
        obs_pic = pygame.image.load("car5.jpg")
    elif obs == 4:
        obs_pic = pygame.image.load("car6.jpg")
    elif obs == 5:
        obs_pic = pygame.image.load("car7.jpg")
    screen.blit(obs_pic,(obs_x,obs_y))

# function for adding the background image
def background():
    screen.blit(grass,(0,0))
    screen.blit(grass,(700,0))
    screen.blit(strip,(120,0))
    screen.blit(strip, (680,0))
    screen.blit(yellow, (400, 0))
    screen.blit(yellow, (400, 100))
    screen.blit(yellow, (400, 200))
    screen.blit(yellow, (400, 300))
    screen.blit(yellow, (400, 400))
    screen.blit(yellow, (400, 500))
    screen.blit(yellow, (400, 600))

def score_card(car_passed,score):
    font = pygame.font.SysFont(None,35)
    passed = font.render("Passed: " + str(car_passed), True, (255,255,255))
    score = font.render("Score: " + str(score), True , (0,0,0))
    high_scoree = font.render("High: " + str(score), True , (0,0,0))
    screen.blit(passed, (0,50))
    screen.blit(score,(0,100))
    #screen.blit(high_scoree,(0,150))


#Image appearing
def car(x,y):
    screen.blit(carimg,(x,y))


#the game loop
def game_loop():
    bumped = False
    x_change = 0
    x = 400
    y = 470
    obstacle_speed = 10
    obs = 0
    y_change = 0
    obs_x = random.randrange(200,650)
    obs_y = -750
    enemy_width = 56
    enemy_height = 125
    car_passed = 0
    score = 0
    level = 0
    high_score = 0


    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bumped = True

        # moving in x-y co-ordinates
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            if event.key == pygame.K_RIGHT:
                x_change = 5
            if event.key == pygame.K_s:
                obstacle_speed +=2
            if event.key == pygame.K_b:
                obstacle_speed -=2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

        x += x_change
        # background colour
        screen.fill((119, 119, 119))
        background()
        obs_y -= obstacle_speed/4
        obstacle(obs_x,obs_y,obs)
        obs_y += obstacle_speed

        #calling car function
        car(x,y)

        # calling score_card function
        score_card(car_passed,score)


        if x > 680 - car_width or x < 110:
            screen.blit(render_text,(145,200))
            pygame.display.update()
            time.sleep(5)
            game_loop()

        if obs_y > HEIGHT:
            obs_y = 0 - enemy_height
            obs_x = random.randrange(170, WIDTH-170)
            obs = random.randrange(0,6)
            car_passed +=1
            score = car_passed * 5
            high_score = score

            if int(car_passed) % 10 == 0:
                level +=1
                obstacle_speed +=2
                myfont = pygame.font.SysFont(None,100)
                level_text = myfont.render("Level: " + str(level), 1 , (0,0,0))
                screen.blit(level_text, (275,200))
                pygame.display.update()
                time.sleep(3)


        if y < obs_y + enemy_height:
            if x > obs_x and x < obs_x + enemy_width or x + car_width > obs_x and x + car_width < obs_x + enemy_width:
                screen.blit(render_text, (145, 200))
                pygame.display.update()
                time.sleep(5)
                game_loop()
        #updating display
        pygame.display.update()
        clock.tick(100)

game_loop()
pygame.quit()
quit()