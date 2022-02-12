import os
import sys

import pygame
import requests


delta = 0.002
delta2 = 0.002
map_request = f"http://static-maps.yandex.ru/1.x/?ll=37.530887,55.703118&spn={delta},{delta2}&l=map"
response = requests.get(map_request)

if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

pygame.init()
screen = pygame.display.set_mode((600, 450))
while running:
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()
    for event.type == pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.K_PAGEUP:
            delta += 0.001
            delta2 += 0.001
            map_request = f"http://static-maps.yandex.ru/1.x/?ll=37.530887,55.703118&spn={delta},{delta2}&l=map"
            response = requests.get(map_request)
            if not response:
                print("Ошибка выполнения запроса:")
                print(map_request)
                print("Http статус:", response.status_code, "(", response.reason, ")")
                sys.exit(1)

            map_file = "map.png"
            with open(map_file, "wb") as file:
                file.write(response.content)
        elif event.type == pygame.K_PAGEDOWN:
            delta -= 0.001
            delta2 -= 0.001
            map_request = f"http://static-maps.yandex.ru/1.x/?ll=37.530887,55.703118&spn={delta},{delta2}&l=map"
            response = requests.get(map_request)
            if not response:
                print("Ошибка выполнения запроса:")
                print(map_request)
                print("Http статус:", response.status_code, "(", response.reason, ")")
                sys.exit(1)

            map_file = "map.png"
            with open(map_file, "wb") as file:
                file.write(response.content)

pygame.quit()

os.remove(map_file)