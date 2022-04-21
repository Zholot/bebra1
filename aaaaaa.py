import pygame

window = pygame.display.set_mode((500, 500))
window.fill((24, 8, 164))
clock = pygame.time.Clock()
fill_color = (0, 255, 106)
cub = pygame.Rect(24, 8, 164, 145)
main_font = pygame.font.Font(None, 70)
caption = main_font.render("Открыл", True, (255, 215, 0))


while True:
    pygame.display.update()
    clock.tick(5)
    pygame.draw.rect(window, fill_color, cub)

main_font = pygame.font.Font(None, 70)
caption = main_font.render('Привет!', True, (255, 215, 0))



import pygame
pygame.init()
window = pygame.display.set_mode((500, 500))
window.fill((128, 0, 255))
clock = pygame.time.Clock()
while True:
    pygame.display.update()
    clock.tick(30)
    fill_color = (255, 255, 255)
    rect = pygame.Rect(100, 100, 200, 250)
    pygame.draw.rect(window, fill_color, rect)
    main_font = pygame.font.Font(None, 70)
    caption = main_font.render(
        'Привет!', True, (255, 215, 0)
    )
    window.blit(caption, (100, 100))