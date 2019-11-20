import sys,pygame

#游戏初始化
pygame.init()
width = 600
height = 500
speed = [1,1]
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("ball")
ball = pygame.image.load("E:\GitHub\Python123\pygame\PYG02-ball.gif")
ballrect = ball.get_rect()
fps = 300
fclock = pygame.time.Clock()

#游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed[0] -= 1
            elif event.key == pygame.K_RIGHT:
                speed[0] += 1
            elif event.key == pygame.K_UP:
                speed[1] -= 1
            elif event.key == pygame.K_DOWN:
                speed[1] += 1
    ballrect = ballrect.move(speed[0],speed[1])
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    
    screen.fill((0,0,0))
    screen.blit(ball,ballrect)
    pygame.display.update()
    fclock.tick(fps)