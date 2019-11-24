import pygame,sys

pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("drawing")

#set up the colors
BLACK = 0,0,0
RED = pygame.Color("red")
SILVER = 192,192,192
GREEN = pygame.Color("green")
WHITE = 255,255,255
BLUE = pygame.Color("blue")

#draw on the surface
screen.fill(WHITE)
#pygame.draw.polygon(screen, BLACK, [(0,0),(45,90),(86,90),(67,46),(6,10),(0,0)])
pygame.draw.line(screen, SILVER, (7,38), (78,80),1)
pygame.draw.circle(screen, BLUE, (400,200),100,5)
pygame.draw.ellipse(screen, RED,(400,200,200,300),0)
pygame.draw.rect(screen, GREEN, (200,100,80,90),0)
pygame.draw.arc(screen, BLACK, (389,400,35,70), 54, 178, 1)
pygame.draw.aaline(screen, BLACK, (0,0), (90,90),1)

#main loop begins
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()