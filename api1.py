import os
import sys

import pygame
import requests


delta = 0.002
delta2 = 0.002
coord1 = 37.530887
coord2 = 55.703118
map1 = 'map'
map2 = 'sat'
map3 = 'skl'
mapvse = map1
map_request = f"http://static-maps.yandex.ru/1.x/?ll={coord1},{coord2}&spn={delta},{delta2}&l={mapvse}"
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
running = True
screen = pygame.display.set_mode((600, 450))
while running:
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAGEUP:
                delta += 0.01
                delta2 += 0.01
                map_request = f"http://static-maps.yandex.ru/1.x/?ll={coord1},{coord2}&spn={delta},{delta2}&l={mapvse}"
                response = requests.get(map_request)
                if not response:
                    print("Ошибка выполнения запроса:")
                    print(map_request)
                    print("Http статус:", response.status_code, "(", response.reason, ")")
                    sys.exit(1)

                map_file = "map.png"
                with open(map_file, "wb") as file:
                    file.write(response.content)
            elif event.key == pygame.K_PAGEDOWN:
                delta -= 0.01
                delta2 -= 0.01
                map_request = f"http://static-maps.yandex.ru/1.x/?ll={coord1},{coord2}&spn={delta},{delta2}&l={mapvse}"
                response = requests.get(map_request)
                if not response:
                    print("Ошибка выполнения запроса:")
                    print(map_request)
                    print("Http статус:", response.status_code, "(", response.reason, ")")
                    sys.exit(1)

                map_file = "map.png"
                with open(map_file, "wb") as file:
                    file.write(response.content)
            elif event.key == pygame.K_UP:
                coord2 += 0.02
                map_request = f"http://static-maps.yandex.ru/1.x/?ll={coord1},{coord2}&spn={delta},{delta2}&l={mapvse}"
                response = requests.get(map_request)
                if not response:
                    print("Ошибка выполнения запроса:")
                    print(map_request)
                    print("Http статус:", response.status_code, "(", response.reason, ")")
                    sys.exit(1)

                map_file = "map.png"
                with open(map_file, "wb") as file:
                    file.write(response.content)
            elif event.key == pygame.K_DOWN:
                coord2 -= 0.02
                map_request = f"http://static-maps.yandex.ru/1.x/?ll={coord1},{coord2}&spn={delta},{delta2}&l={mapvse}"
                response = requests.get(map_request)
                if not response:
                    print("Ошибка выполнения запроса:")
                    print(map_request)
                    print("Http статус:", response.status_code, "(", response.reason, ")")
                    sys.exit(1)

                map_file = "map.png"
                with open(map_file, "wb") as file:
                    file.write(response.content)
            elif event.key == pygame.K_RIGHT:
                coord1 += 0.002
                map_request = f"http://static-maps.yandex.ru/1.x/?ll={coord1},{coord2}&spn={delta},{delta2}&l={mapvse}"
                response = requests.get(map_request)
                if not response:
                    print("Ошибка выполнения запроса:")
                    print(map_request)
                    print("Http статус:", response.status_code, "(", response.reason, ")")
                    sys.exit(1)

                map_file = "map.png"
                with open(map_file, "wb") as file:
                    file.write(response.content)
            elif event.key == pygame.K_LEFT:
                coord1 -= 0.02
                map_request = f"http://static-maps.yandex.ru/1.x/?ll={coord1},{coord2}&spn={delta},{delta2}&l={mapvse}"
                response = requests.get(map_request)
                if not response:
                    print("Ошибка выполнения запроса:")
                    print(map_request)
                    print("Http статус:", response.status_code, "(", response.reason, ")")
                    sys.exit(1)

                map_file = "map.png"
                with open(map_file, "wb") as file:
                    file.write(response.content)
            elif event.key == pygame.K_z:
                mapvse = map1
                map_request = f"http://static-maps.yandex.ru/1.x/?ll={coord1},{coord2}&spn={delta},{delta2}&l={mapvse}"
                response = requests.get(map_request)
                if not response:
                    print("Ошибка выполнения запроса:")
                    print(map_request)
                    print("Http статус:", response.status_code, "(", response.reason, ")")
                    sys.exit(1)

                map_file = "map.png"
                with open(map_file, "wb") as file:
                    file.write(response.content)
            elif event.key == pygame.K_x:
                mapvse = map2
                map_request = f"http://static-maps.yandex.ru/1.x/?ll={coord1},{coord2}&spn={delta},{delta2}&l={mapvse}"
                response = requests.get(map_request)
                if not response:
                    print("Ошибка выполнения запроса:")
                    print(map_request)
                    print("Http статус:", response.status_code, "(", response.reason, ")")
                    sys.exit(1)

                map_file = "map.png"
                with open(map_file, "wb") as file:
                    file.write(response.content)
            elif event.key == pygame.K_c:
                map_request = f"http://static-maps.yandex.ru/1.x/?ll={coord1},{coord2}&spn={delta},{delta2}&l={map3}"
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
