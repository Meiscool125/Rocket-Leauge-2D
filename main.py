#setting everything up
import pygame
import time
import random
# pygame.init starts the code
pygame.init()
# create time
clock = pygame.time.Clock()
# make the name of the window
pygame.display.set_caption("Rocket Leauge in 2D Poorly Made")
icon_img = pygame.image.load("assets/rlsideswipe.jpg")
pygame.display.set_icon(icon_img)

# main fonts
mainfont = pygame.font.Font(None, 35)
NPCfont = pygame.font.Font(None, 25)
# screen setup
screen = pygame.display.set_mode((1000, 500))
# set variable that is true
CurrentlyRunning = True



# make this happen a lot of times per second
while CurrentlyRunning:
    CurrentTime = (pygame.time.get_ticks() / 1000)
    screen.fill((69,69,69))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # user clicked close button
            CurrentlyRunning = False
    #screen.blit(GrassAndDirtBG1, (BGX, BGY))
    CurrentTime = (pygame.time.get_ticks() / 1000)
    clock.tick(60)
    pygame.display.flip()
pygame.quit()


