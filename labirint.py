# Разработай свою игру в этом файле!
from pygame import *
import pygame

display.set_caption('MiniGame')
window = display.set_mode((500, 500))
background = transform.scale(image.load('background.jpg'), (500, 500))

win = transform.scale(image.load('bitcoin.png'), (500, 500))



class GameSprite(sprite.Sprite):
    def __init__(self, picture, w, h, x, y):
        super().__init__()
        self.image = transform.scale(image.load(picture), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x



    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))



class Player(GameSprite):
    def __init__(self, picture, w, h, x, y, x_speed, y_speed):
        super().__init__(picture, w, h, x, y)
        self.x_speed = x_speed
        self.y_speed = y_speed

    
    def update(self):
        self.rect.x += self.x_speed
        p_touch = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0:
            for p in p_touch:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in p_touch:
                self.rect.left = max(self.rect.left, p.rect.right)
        self.rect.y += self.y_speed
        p_touch = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0:
            for p in p_touch:
                self.rect.bottom = min(self.rect.bottom, p.rect.top)
        elif self.y_speed < 0:
            for p in p_touch:
                self.rect.top = max(self.rect.top, p.rect.bottom)


    def fire(self):
            bullet = ('bitcoin.png', 50, 50, self.rect.right, self.rect.centery, 5)
            bullets.add(bullet)



class Bullet(GameSprite): #---
    def __init__(self, picture, w, h, x, y, speed):
        super().__init__(picture, w, h, x, y)
        self.speed = speed
    def update(self):
        self.rect.x += self.speed
        if self.rect.x >= 510:
            self.kill()



class Enemy(GameSprite):
    def __init__(self, picture, w, h, x, y, x_der, y_der, speed):
        super().__init__(picture, w, h, x, y)
        self.x_der = x_der
        self.y_der = y_der
        self.speed = speed
    

    def update(self):
        if self.x_der == True:
            self.rect.x += self.speed
            if self.rect.x >= 200:
                self.x_der = False
        elif self.x_der == False:
            self.rect.x -= self.speed
            if self.rect.x <= 50:
                self.x_der = True

            


p1 = Player('chip.png', 80, 80, 120, 120, 0, 0)
e1 = Enemy('rub.jpg', 80, 80, 20, 200, True, True, 2)
w1 = GameSprite('wall1.jpg', 500, 10, 0, 0)
w2 = GameSprite('wall1.jpg', 500, 10, 0, 490)
w3 = GameSprite('wall2.jpg', 10, 500, 0, 0)
w4 = GameSprite('wall2.jpg', 10, 500, 490, 0)
w5 = GameSprite('wall4.jpg', 250, 50, 10, 280)
w6 = GameSprite('wall3.jpg', 500, 50, 260, 140)
w7 = GameSprite('wall5.jpg', 50, 450, 240, 410)
fin = GameSprite('fin.png', 50, 50, 10, 440)

barriers = sprite.Group()
barriers.add(w1)
barriers.add(w2)
barriers.add(w3)
barriers.add(w4)
barriers.add(w5)
barriers.add(w6)
barriers.add(w7)

p_touch = sprite.spritecollide(p1, barriers, False)

bullets = sprite.Group()


clock = time.Clock

finish = False
run = True
while run:
    if finish != True:
        window.blit(background, (0, 0))
        p1.update()
        p1.reset()
        e1.update()
        e1.reset()
        bullets.draw(window)
        bullets.update() #---
        barriers.draw(window) #---
        fin.reset()
        sprite.groupcollide(bullets, barriers, True, True)
        if sprite.collide_rect(p1, fin):
            finish = True
            window.blit(win, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_w:
                p1.y_speed = -4
            if e.key == K_s:
                p1.y_speed = 4
            if e.key == K_d:
                p1.x_speed = 4
            if e.key == K_a:
                p1.x_speed = -4
            if e.key == K_SPACE:
                p1.fire()
        
        elif e.type == KEYUP:
            if e.key == K_w:
                p1.y_speed = 0
            if e.key == K_s:
                p1.y_speed = 0
            if e.key == K_d:
                p1.x_speed = 0
            if e.key == K_a:
                p1.x_speed = 0
             
    
    display.update()
    time.delay(50)