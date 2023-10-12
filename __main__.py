import pygame, sys, random

from pygame.sprite import AbstractGroup

pygame.init()
scren = pygame.display.set_mode((600,400))
clock = pygame.time.Clock()


#creo la clase Alien que hereda de Sprite así como su grupo donde los almacenaré a todos
alien_group = pygame.sprite.Group()
class Alien(pygame.sprite.Sprite):
    def __init__(self,):
        super().__init__()

        self.image = pygame.Surface([40, 20])
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()

        self.rect.center = [random.randint(10,590),10]

        alien_group.add(self)

    def update(self):
        self.rect.center = [self.rect.center[0],self.rect.center[1]+1]
    

alien1 = Alien()


player_group = pygame.sprite.Group()
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        super().__init__()

        self.image = pygame.Surface([40, 20])
        self.image.fill((141,255,56))
        self.rect = self.image.get_rect()

        self.rect.center = [300,390]

        player_group.add(self)

    def move_left(self):
        self.rect.center = [self.rect.center[0]-10,self.rect.center[1]]
    def move_right(self):
        self.rect.center = [self.rect.center[0]+10,self.rect.center[1]]
    def move_top(self):
        self.rect.center = [self.rect.center[0],self.rect.center[1]-10]
    def move_down(self):
        self.rect.center = [self.rect.center[0],self.rect.center[1]+10]

    def shoot(self):
        bullet_group.add(Bullet(self.rect.center[0],self.rect.center[1]))


p1 = Player()

bullet_group = pygame.sprite.Group()
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        self.image = pygame.image.load("dollar.png")
        #sself.image.fill((255,255,255))
        self.rect = self.image.get_rect()

        self.rect.center = [x,y]

        bullet_group.add(self)


    def update(self):
        self.rect.center = [self.rect.center[0],self.rect.center[1]-2]

#Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                p1.move_right()
            if event.key == pygame.K_a:
                p1.move_left()
            if event.key == pygame.K_w:
                p1.move_top()
            if event.key == pygame.K_s:
                p1.move_down()
            if event.key == pygame.K_SPACE:
                p1.shoot()
            

    pygame.display.flip()
    scren.fill((0,0,0))

    alien_group.update()
    bullet_group.update()

    alien_group.draw(scren)
    player_group.draw(scren)
    bullet_group.draw(scren)

    
    for alien in alien_group.sprites():
        for bullet in bullet_group.sprites():
            if alien.rect.colliderect(bullet.rect):
                bullet_group.remove(bullet)
                alien_group.remove(alien)
        
            

    clock.tick(23)