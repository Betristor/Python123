import pygame,sys,math,random,time
from pygame.sprite import Sprite

#游戏逻辑设置
#导弹会随机产生，导弹触碰到玩家即结束游戏
#玩家捡取物品以获得积分

def main():
    #设置屏幕
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Escape the Dragon","trail")

    #设置颜色
    WHITE = 255,255,255
    RED = pygame.Color("red")
    SILVER = 192,192,192
    GREEN = pygame.Color("green")
    BLUE = pygame.Color("blue")

    #设置字体
    #font_en = pygame.font.Font("C:\Windows\Fonts\Book Antique.ttf",45)
    #font_cn = pygame.font.Font("C:\Windows\Fonts\msyh.ttc",45)

    #设置背景音乐
    pygame.mixer.init()
    bgmusic = pygame.mixer.music.load("E:\GitHub\Python123\pygame\Control.mp3")
    
    #设置地面
    ground = pygame.draw.rect(screen, BLUE, (0,400,800,200), 0)

    #玩家加载
    girl = pygame.image.load("E:\GitHub\Python123\pygame\girl.png").convert_alpha()
    g_width,g_height = girl.get_size()
    girl = pygame.transform.scale(girl, (g_width//8, g_height//8))
    girl_rect = girl.get_rect()
    girl_rect.bottom = ground.top

    #子弹设置
    class Bullet(Sprite):
        def __init__(self,girl_rect,ground):
            super(Bullet,self).__init__()
            self.rect = pygame.draw.rect(screen, WHITE, (0,0,5,2), 0)
            self.rect.centery = girl_rect.centery
            self.rect.right = ground.rect.right
            self.speed = -20

        def back(self):
            self.rect.centerx += self.speed

    bullets = pygame.sprite.Group()
    
    #设置帧率
    fps = 30
    fpsclock = pygame.time.Clock() 

    #游戏开始标志
    game_over = False

    #游戏开始时间
    start_time = time.perf_counter()

    #main loop begins
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        if not game_over:
            screen.blit(girl,girl_rect)
            current_time = time.perf_counter()
            gap = current_time - start_time
            gap = round(gap)
            if gap % 5 == 0:
                bullet = Bullet(girl_rect,ground)
                bullets.add(bullet)
                bullets.update()
            

        pygame.display.update()
        #bgmusic.play(-1,0.0)
        fpsclock.tick(fps)
main()