import pygame
import player
import utils
import random


pygame.init()

width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

snake = player.Snake(width/2, height/2, 10, 15, (random.randint(0, 155), random.randint(0, 155), random.randint(0, 155)))
apple = pygame.image.load("./assets/apple2.png")  
apple = pygame.transform.scale(apple, (40, 40))
pos_apple = (random.randint(0, width-20), random.randint(0, height-20))

surface_maingame = pygame.Surface((width, height))
surface_menu     = pygame.Surface((width, height))

gamemode = "Menu"

running = True

image_grass =       pygame.image.load("./assets/grass1.png")
button_play =       utils.Button(width//2, height//2, 200, 70, (55, 55, 55), (100, 110, 120), utils.Text("Play", 52, (255,255,255)))
scroll_snakespeed = utils.ScrollSwitch(20, 20, 200, 20, 1, 20)
text_highscore =    utils.Text("High Score: 0", 52, (255,255,255), 20, 50)
text_score =        utils.Text("0", 52, (255,255,255), width//2-5, 10)

highscore = 0
score = 0

pygame.mixer.music.load("./assets/background.wav")
pygame.mixer.music.play(-1)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif (gamemode == "Menu"): 
            if (button_play.handle_event(event) == True):
                gamemode = "Maingame"

            elif(scroll_snakespeed.handle_event(event)):
                snake.vel = scroll_snakespeed.get_scroll_val()
            
        elif (gamemode == "Maingame"):
                snake.handle_event(event)

    
    if (gamemode == "Maingame"):
        surface_maingame.blit(image_grass, (0,0))
        surface_maingame.blit(apple, (int(pos_apple[0]-15), int(pos_apple[1]-15)))
        snake.update()
        text_score.updateText(str(score))
        snake.draw(surface_maingame) 
        text_score.draw(surface_maingame)

        if (snake.collide(pos_apple[0], pos_apple[1], 20)):
            pygame.mixer.Channel(1).play(pygame.mixer.Sound("./assets/crunch.wav"))
            snake.grow()
            score+=1
            pos_apple = (random.randint(0, width-40), random.randint(0, height-40))

        if (snake.body[0].x >= width or snake.body[0].y  >= height or snake.body[0].x <= 0 or snake.body[0].y <= 0):
            snake.reset(width//2, height//2)
            highscore = score if highscore < score else highscore
            score = 0
            text_highscore.updateText("HighScore: " + str(highscore))            
            gamemode = "Menu"
            
        screen.blit(surface_maingame, (0,0))

    elif (gamemode == "Menu"):
        surface_menu.blit(image_grass, (0,0))
        button_play.draw(surface_menu)
        text_highscore.draw(surface_menu)
        scroll_snakespeed.draw(surface_menu)
        scroll_snakespeed.update()
        screen.blit(surface_menu, (0,0))


    pygame.time.Clock().tick(40)
    pygame.display.update()


pygame.quit()