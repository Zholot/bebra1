from random import *
import pygame

pygame.init()
mw = pygame.display.set_mode((500, 500))
mw.fill('green')

clock = pygame.time.Clock()
clock.tick(40)
pygame.display.update()


class TextArea():
    def __init__(self, x, y, s, v, color):
        self.rect = pygame.Rect(x, y, v, s)
        self.fill_color = color

    def text(self, text, text_color=(0,0,0)):
        self.text = text

        self.image = pygame.font.Font(None, 70).render(text, True, text_color)

    def draw(self, sx=0, sy=0):
        pygame.draw.rect(mw, self.fill_color, self.rect)

        mw.blit(self.image, (self.rect.x + sx, self.rect.y + sy))


vop = TextArea(0, 0, 10, 10, (0,255,0))
vop.text('Ответ')
vop.draw(0, 0)
vor = TextArea(0, 0, 10, 10, (0,255,0))
vor.text('Вопрос')
vor.draw(0, 0)
for event in pygame.event.get():
    if event.tyre == pygame.key:
        if event.key == pygame.K_q:
            e = randint(1, 3)
    if e == 1:
        vop.text('да,очень люблю')
    if e == 2:
        vop.text('ну смотря в какой ситуации')
    if e == 3:
        vop.text('нет')
    if event.key == pygame.K_w:
        g = randint(1, 3)
    if g == 1:
        vor.text('ты любишь бухать ночами напролет?')
    if g == 2:
        vor.text('ты вообще когда нибудь спишь?')
    if g == 3:
        vor.text('ты лох?')