import pygame
pygame.init()

#WITHD AND HEIGHT ist because function and 2nd because tuple
screen=pygame.display.set_mode((800,600))
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
pink = (255,190,203)
white = (255,255,255)



screen.fill(pink)

#Infinite loop that repeats while a function is true
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


