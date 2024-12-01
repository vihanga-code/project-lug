import pygame
import random
sw,sh,ms,fs=500,400,5,72
pygame.init()
screen=pygame.display.set_mode((sw,sh))
bg=pygame.transform.scale(pygame.image.load("pic.png"),(sw,sh))
font=pygame.font.SysFont("Times New Roman",50)
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,size):
        super().__init__()
        self.image=pygame.Surface(size)
        pygame.draw.rect(self.image,color,self.image.get_rect())
        self.rect=self.image.get_rect()
    def move(self,xc,yc):
        self.rect.x=max(0,min(self.rect.x+xc,sw-self.rect.width))   
        self.rect.y=max(0,min(self.rect.y+yc,sh-self.rect.height))   
sprites=pygame.sprite.Group(
    Sprite("black",(20,30)),Sprite("red",(20,30))
    
)
for sprite in sprites:
    sprite.rect.topleft=(random.randint(0,sw-sprite.rect.width),random.randint(0,sh-sprite.rect.height))
running,won=True,False
clock=pygame.time.Clock()    
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    if not won:
    
        keys = pygame.key.get_pressed()
        sprites.sprites()[0].move((keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * ms,(keys[pygame.K_DOWN] - keys[pygame.K_UP]) *ms)
        if sprites.sprites()[0].rect.colliderect(sprites.sprites()[1].rect):
            sprites.remove(sprites.sprites()[1])
            won = True 
    screen.blit(bg, (0, 0))
    sprites.draw(screen)
    if won:
        win_text = font.render("You win!", True, pygame.Color('black'))
        screen.blit(win_text, ((sw - win_text.get_width()) // 2,(sh - win_text.get_height()) // 2))
    pygame.display.flip()
    clock.tick(90)