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

    def fall(self):
        self.rect.center = [self.rect.center[0],self.rect.center[1]+1]

alien1 = Alien()

class Player(pygame.sprite.Sprite):
    player_group = pygame.sprite.Group()

    def __init__(self):
        super().__init__()

        super().__init__()

        self.image = pygame.Surface([40, 20])
        self.image.fill((141,255,56))
        self.rect = self.image.get_rect()

        self.rect.center = [300,390]

        self.player_group.add(self)

    def move_left(self):
        self.rect.center = [self.rect.center[0]-10,390]
    def move_right(self):
        self.rect.center = [self.rect.center[0]+10,390]
p1 = Player()

#Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                p1.move_right()
            if event.key == pygame.K_LEFT:
                p1.move_left()



    pygame.display.flip()
    scren.fill((0,0,0))

    alien1.fall()
    alien_group.draw(scren)
    p1.player_group.draw(scren)

    clock.tick(23)