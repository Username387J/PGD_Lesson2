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


screen.fill("teal")

class Rect:
    def __init__(self,color,dimension):
        self.dimension=dimension
        self.color=color
        self.rectscreen=screen
  #the function that actually draws the rectangle, acconding to |
    def drawRect(self):                                        #V
        self.rect_draw=pygame.draw.rect(self.rectscreen,self.color,self.dimension)
#(color(x,y,width,height))
#(according to the self,color,dimension)
greenRect=Rect(green,(35,200,200,150))
greenRect.drawRect()

blackRect=Rect(black,(395,500,150,80))
blackRect.drawRect()

redRect=Rect(red,(70,20,270,150))
redRect.drawRect()

blueRect=Rect(blue,(470,100,152,129))
blueRect.drawRect()

pinkRect=Rect(pink,(306,294,105,90))
pinkRect.drawRect()

whiteRect=Rect(white,(102,446,295,238))
whiteRect.drawRect()

#Not a variable,therefore given thsi sign ("")
purpleRect=Rect("purple",(535,308,274,196))
purpleRect.drawRect()

yellowRect=Rect("yellow",(270,295,185,397))
yellowRect.drawRect()

orangeRect=Rect("orange",(405,306,184,107))
orangeRect.drawRect()

#Infinite loop that repeats while a function is true
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

