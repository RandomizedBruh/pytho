
from classed.enemy import Enemy

from classed.player import Player


player1 = Player("Фордик", "какойтоguyизфнфмода", 100, 100, 50, 10)
player1.print_infoP()

# player1.say("блин...*cry*")


enemy1 = Enemy("Матр4сс","тожегайсфнфмода", 100, 10)
enemy1.info()
player1.fight(enemy1)
# enemy1.info()


import pygame

# Определение размеров окна
WIDTH = 1200
HEIGHT = 720

# Определение цветов в формате RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)  # Исправлено значение цвета RED
GREEN = (0, 255, 0)  # Исправлено значение цвета GREEN
BLUE = (0, 0, 255)  # Исправлено значение цвета BLUE

FPC = 60
clock = pygame.time.Clock()
# Инициализация модуля pygame
pygame.init()

# Инициализация модуля звука pygame
pygame.mixer.init()

# Создание окна с заданными размерами
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Установка заголовка окна
pygame.display.set_caption("my game")

# Флаг для управления игровым циклом
isGame = True
x = 50
y = 50
# Основной игровой цикл
while isGame:
    # Обработка событий
    for event in pygame.event.get():
        # Если пользователь закрыл окно
        if event.type == pygame.QUIT:
            isGame = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y -= 5
    if keys[pygame.K_s]:
       y += 5
    if keys[pygame.K_a]:
        x -= 5
    if keys[pygame.K_d]:
        x -= 5
    # Заливка фона окна белым цветом
    screen.fill(WHITE)

    pygame.draw.rect(screen, RED, (50, y, 100, 100),border_radius=10)


    # Обновление содержимого окна
    pygame.display.flip()

# Завершение работы модуля pygame
pygame.quit()


  


# ⁣yes     yes  yes yes yes
# yesyes  yes  yes     yes
# yes yes yes  yes     yes
# yes  yesyes  yes     yes
# yes     yes  yes yes yes
