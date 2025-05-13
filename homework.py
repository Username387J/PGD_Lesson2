import pygame
pygame.init()

screen = pygame.display.set_mode((600, 600))
screen.fill("black")

class Circle:
    def __init__(self,screen,color,position,radius):
        self.screen=screen
        self.color=color
        self.position=position
        self.radius=radius

    def drawCircle(self):
        pygame.draw.circle(self.screen,self.color,self.position,self.radius)

redCirc = Circle(screen,"red", (500, 400), 90)
redCirc.drawCircle()

yellowCirc = Circle(screen,"yellow", (100, 150), 70)
yellowCirc.drawCircle()

orangeCirc = Circle(screen,"orange", (200,390), 95)
orangeCirc.drawCircle()

greenCirc = Circle(screen,"green", (350, 260), 40)
greenCirc.drawCircle()

blueCirc = Circle(screen,"blue", (150, 350), 85)
blueCirc.drawCircle()

purpCirc = Circle(screen,"purple", (200, 100), 70)
purpCirc.drawCircle()


while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
